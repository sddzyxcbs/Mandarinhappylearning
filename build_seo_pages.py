#!/usr/bin/env python3
"""Generate crawlable, unique HTML pages, hub catalogs, a word index, and sitemap.xml.

Regenerating is safe to rerun: every file it owns is rewritten from content.js.
"""
from __future__ import annotations

import datetime
import html
import json
import re
from pathlib import Path
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring

ROOT = Path(__file__).resolve().parent
BASE = "https://mandarinhappylearning.top"
SITE = "汉语慢慢学"
OG_IMAGE = f"{BASE}/assets/og-default.png"
BUILD_DATE = datetime.date.today().isoformat()

DATA = json.loads((ROOT / "content.js").read_text(encoding="utf-8").removeprefix("window.CN_CONTENT="))
SITE_JS = (ROOT / "site.js").read_text(encoding="utf-8")

# Curated English-first metadata for the highest-intent lessons.
SEO_META = {
    "greetings": {
        "title": "Mandarin Greetings: Hello, Thank You & Polite Phrases | 汉语慢慢学",
        "description": "Learn essential Mandarin greetings, thank-you phrases, and polite requests with pinyin, examples, and a quick beginner exercise. Free lesson.",
    },
    "basic-word-order": {
        "title": "Chinese Word Order for Beginners: Subject, Verb & Object",
        "description": "Learn basic Mandarin sentence order with clear subject-verb-object examples, English translations, and a quick practice question.",
    },
    "measure-words": {
        "title": "Chinese Measure Words: How to Use 个 and 杯",
        "description": "Learn why Mandarin uses measure words and how to use 个 and 杯 with numbers and nouns. Includes examples and a quick exercise.",
    },
    "bu-and-mei": {
        "title": "不 (Bù) vs. 没 (Méi): Negation in Mandarin",
        "description": "Understand when to use 不 and 没 in Mandarin for general negation, not having something, and actions that have not happened.",
    },
    "shi-and-you": {
        "title": "是 (Shì) vs. 有 (Yǒu): Be and Have in Chinese",
        "description": "Learn when to use 是 for identity and category, and 有 for possession or existence, with practical Mandarin examples.",
    },
}

LESSONS = DATA["lessons"]
BY_SLUG = {lesson["slug"]: lesson for lesson in LESSONS}
ORDER = {lesson["slug"]: i for i, lesson in enumerate(LESSONS)}


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def js_json(obj: object) -> str:
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


# ---------------------------------------------------------------- stage metadata
def parse_stages() -> list[dict]:
    pattern = re.compile(
        r"\{id:'([^']+)',title:'([^']*)',englishTitle:'([^']*)',description:'([^']*)',"
        r"englishDescription:'([^']*)',slugs:\[([^\]]*)\]"
    )
    stages = []
    for match in pattern.finditer(SITE_JS):
        stages.append(
            {
                "id": match.group(1),
                "title": match.group(2),
                "englishTitle": match.group(3),
                "description": match.group(4),
                "englishDescription": match.group(5),
                "slugs": re.findall(r"'([^']+)'", match.group(6)),
            }
        )
    if len(stages) != 5:
        raise SystemExit(f"expected 5 stage definitions in site.js, found {len(stages)}")
    return stages


def parse_vocab_grammar_links() -> dict[str, list[str]]:
    block = re.search(r"const VOCAB_GRAMMAR_LINKS=\{(.*?)\n?\};", SITE_JS, re.S)
    if not block:
        return {}
    return {slug: re.findall(r"'([^']+)'", group) for slug, group in re.findall(r"'([^']+)':\[([^\]]*)\]", block.group(1))}


STAGES = parse_stages()
VOCAB_GRAMMAR_LINKS = parse_vocab_grammar_links()
SLUG_STAGE = {slug: stage["id"] for stage in STAGES for slug in stage["slugs"]}


def stage_of(lesson: dict) -> str:
    return lesson.get("stage") or SLUG_STAGE.get(lesson["slug"]) or "more"


def unit_no(lesson: dict) -> int:
    match = re.search(r"Unit (\d+)", lesson.get("level", "") or "")
    return int(match.group(1)) if match else 0


STAGE_ORDER = {stage["id"]: i for i, stage in enumerate(STAGES)}
STAGE_ORDER["more"] = len(STAGES)


def group_key(lesson: dict) -> tuple:
    return (
        0 if lesson["type"] == "vocabulary" else 1,
        STAGE_ORDER.get(stage_of(lesson), 99),
        unit_no(lesson),
        ORDER[lesson["slug"]],
    )


VOCAB = sorted((l for l in LESSONS if l["type"] == "vocabulary"), key=group_key)
GRAMMAR = sorted((l for l in LESSONS if l["type"] == "grammar"), key=group_key)


# ---------------------------------------------------------------- relations
def related_slugs(lesson: dict, limit: int = 5) -> list[str]:
    slugs: list[str] = []

    def add(slug: str) -> None:
        if slug != lesson["slug"] and slug in BY_SLUG and slug not in slugs:
            slugs.append(slug)

    if lesson["type"] == "grammar":
        for slug in lesson.get("relatedLessons", []) or []:
            add(slug)
        for other in GRAMMAR:
            if lesson["slug"] in (other.get("relatedLessons") or []):
                add(other["slug"])
    else:
        for slug in VOCAB_GRAMMAR_LINKS.get(lesson["slug"], []) or []:
            add(slug)
        for other in GRAMMAR:
            if lesson["slug"] in (other.get("relatedLessons") or []):
                add(other["slug"])

    if len(slugs) < limit:
        tags = set(lesson.get("tags") or [])
        for other in VOCAB + GRAMMAR:
            if len(slugs) >= limit:
                break
            if other["type"] == lesson["type"] and tags & set(other.get("tags") or []):
                add(other["slug"])

    if len(slugs) < limit:
        pool = VOCAB if lesson["type"] == "vocabulary" else GRAMMAR
        same_stage = [o for o in pool if stage_of(o) == stage_of(lesson)]
        for other in same_stage:
            if len(slugs) >= limit:
                break
            add(other["slug"])

    return slugs[:limit]


def neighbours(lesson: dict) -> tuple[dict | None, dict | None]:
    pool = VOCAB if lesson["type"] == "vocabulary" else GRAMMAR
    same_stage = [item for item in pool if stage_of(item) == stage_of(lesson)]
    if len(same_stage) < 2:
        same_stage = pool
    index = same_stage.index(lesson)
    prev_lesson = same_stage[index - 1] if index > 0 else None
    next_lesson = same_stage[index + 1] if index + 1 < len(same_stage) else None
    return prev_lesson, next_lesson


# ---------------------------------------------------------------- shared head
def head_block(*, title: str, description: str, url: str, page_type: str = "article", schema: list[dict] | None = None) -> str:
    ld = "".join(f'<script type="application/ld+json">{js_json(block)}</script>' for block in (schema or []))
    return (
        f'<title>{e(title)}</title><meta name="description" content="{e(description)}">'
        f'<link rel="canonical" href="{e(url)}">'
        '<meta name="robots" content="index,follow,max-image-preview:large">'
        f'<meta property="og:type" content="{e(page_type)}"><meta property="og:site_name" content="{e(SITE)}">'
        f'<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(description)}">'
        f'<meta property="og:url" content="{e(url)}"><meta property="og:locale" content="zh_CN">'
        f'<meta property="og:image" content="{e(OG_IMAGE)}"><meta property="og:image:width" content="1200">'
        '<meta property="og:image:height" content="630"><meta property="og:image:alt" content="汉语慢慢学 · Learn Chinese slowly">'
        '<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:title" content="{e(title)}"><meta name="twitter:description" content="{e(description)}">'
        f'<meta name="twitter:image" content="{e(OG_IMAGE)}">'
        '<meta name="theme-color" content="#245d4b">'
        f'{ld}'
    )


# ---------------------------------------------------------------- lesson pages
def page_for(lesson: dict) -> str:
    slug = lesson["slug"]
    title = lesson["title"]
    is_grammar = lesson["type"] == "grammar"
    kind = "汉语语法" if is_grammar else "汉语词汇"
    kind_en = "Chinese Grammar" if is_grammar else "Chinese Vocabulary"
    hub = "grammar" if is_grammar else "vocabulary"
    seo = SEO_META.get(slug, {})
    meta_title = seo.get("title") or f"{title} · {kind_en} Lesson with Pinyin & Examples | {SITE}"
    description = seo.get("description") or (
        f"{lesson.get('subtitle', '')} Beginner {kind_en.lower()} lesson with pinyin, English meanings, "
        "example sentences, and a quick practice question."
    )
    description = re.sub(r"\s+", " ", description).strip()[:158]
    url = f"{BASE}/lessons/{slug}.html"
    tags = "".join(f'<span class="pill">{e(tag)}</span>' for tag in lesson.get("tags", []))

    body = [
        f'<div class="crumb"><a href="../index.html">首页</a>　/　<a href="../{hub}.html">{kind}课程</a>　/　{e(title)}</div>',
        f'<div class="lesson-title"><div class="section-kicker">{e(lesson.get("level", "中文课程"))}</div><h1>{e(title)}</h1>'
        f'<div class="subtitle">{e(lesson.get("subtitle", ""))}</div><div class="lesson-meta"><span class="pill">{e(lesson.get("duration", ""))}</span>{tags}</div></div>',
        f'<section class="lesson-section"><h2>本课目标 · Lesson goal</h2><p>{e(lesson.get("goal", ""))}</p><p>{e(lesson.get("intro", ""))}</p></section>',
    ]
    if lesson.get("words"):
        cards = []
        for word in lesson["words"]:
            cards.append(
                f'<article class="lesson-word"><button class="play" data-say="{e(word[0])}" aria-label="播放{e(word[0])}">▶</button>'
                f'<strong>{e(word[0])}</strong><span class="py">{e(word[1])}</span><div class="meaning">{e(word[2])}</div>'
                f'<div class="example">{e(word[3])}</div><div class="translation">{e(word[4])}</div></article>'
            )
        body.append('<section class="lesson-section"><h2>重点词汇 · Key words</h2><div class="lesson-words">' + "".join(cards) + "</div></section>")
    if lesson.get("pattern"):
        body.append(
            f'<section class="lesson-section"><h2>表达结构 · Sentence pattern</h2>'
            f'<div class="pattern">{e(lesson["pattern"])}<small>{e(lesson.get("patternEn", ""))}</small></div></section>'
        )
    if lesson.get("examples"):
        items = "".join(f"<li><b>{e(row[0])}</b><span>{e(row[1])}</span></li>" for row in lesson["examples"])
        body.append('<section class="lesson-section"><h2>例句 · Examples</h2><ul class="example-list">' + items + "</ul></section>")
    if lesson.get("tip"):
        body.append(f'<section class="lesson-section"><h2>学习提示 · Study tip</h2><p>{e(lesson["tip"])}</p></section>')
    exercise = lesson.get("exercise", {})
    if exercise:
        options = "".join(f"<li>{e(option)}</li>" for option in exercise.get("options", []))
        answer = exercise.get("options", [""])[exercise.get("answer", 0)]
        body.append(
            f'<section class="lesson-section"><h2>小练习 · Quick check</h2><p>{e(exercise.get("q", ""))}</p><ol>{options}</ol>'
            f'<details><summary>查看答案 · Show answer</summary><p>{e(answer)} — {e(exercise.get("why", ""))}</p></details></section>'
        )

    related = related_slugs(lesson)
    if related:
        links = "".join(
            f'<a href="{e(slug_)}.html">{e(BY_SLUG[slug_]["title"])}　↗</a>' for slug_ in related
        )
        body.append(
            '<section class="lesson-section related-section"><h2>继续学习 · Continue learning</h2>'
            '<p>想再多练一点？这些课程和你刚学的内容相关。More lessons that build on this one.</p>'
            f'<div class="related-links"><b>相关课程 · Related lessons</b>{links}</div></section>'
        )

    prev_lesson, next_lesson = neighbours(lesson)
    nav_left = (
        f'<a href="{e(prev_lesson["slug"])}.html">← 上一课 · {e(prev_lesson["title"])}</a>'
        if prev_lesson
        else f'<a href="../{hub}.html">← 返回课程目录 · Back to lessons</a>'
    )
    nav_right = (
        f'<a href="{e(next_lesson["slug"])}.html">下一课 · {e(next_lesson["title"])} →</a>'
        if next_lesson
        else '<a href="../practice.html">去互动练习 · Practice →</a>'
    )
    body.append(f'<nav class="lesson-nav">{nav_left}{nav_right}</nav>')

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "首页", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": kind + "课程", "item": f"{BASE}/{hub}.html"},
            {"@type": "ListItem", "position": 3, "name": title, "item": url},
        ],
    }
    resource = {
        "@context": "https://schema.org",
        "@type": "LearningResource",
        "name": title,
        "description": description,
        "url": url,
        "inLanguage": ["zh-CN", "en"],
        "learningResourceType": "Lesson",
        "educationalLevel": "Beginner",
        "isAccessibleForFree": True,
        "teaches": [word[0] for word in (lesson.get("words") or [])][:10] or [lesson.get("pattern", title)],
        "provider": {"@type": "Organization", "name": SITE, "url": BASE + "/"},
        "isPartOf": {"@type": "WebSite", "name": SITE, "url": BASE + "/"},
    }

    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
{head_block(title=meta_title, description=description, url=url, schema=[breadcrumb, resource])}
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="../styles.css?v=20261023"></head>
<body><header class="wrap topbar"><a class="brand" href="../index.html"><span class="seal">汉</span><span>汉语慢慢学<small>CHINESE, ONE MOMENT AT A TIME</small></span></a><nav class="nav"><a href="../index.html">首页 <span class="nav-en">Home</span></a><a href="../vocabulary.html">词汇 <span class="nav-en">Vocabulary</span></a><a href="../grammar.html">语法 <span class="nav-en">Grammar</span></a><a href="../practice.html">互动练习 <span class="nav-en">Practice</span></a></nav></header>
<main class="lesson-shell">{"".join(body)}</main><footer class="footer"><div class="wrap footer-inner"><a class="brand" href="../index.html"><span class="seal">汉</span><span>汉语慢慢学<small>CHINESE, ONE MOMENT AT A TIME</small></span></a><p>从一个词开始，慢慢认识一种语言。　© 2026 汉语慢慢学</p><div class="footer-links"><a href="../vocabulary.html">课程目录</a><a href="../words.html">词汇总表</a></div></div></footer>
<script>document.querySelectorAll('[data-say]').forEach(b=>b.addEventListener('click',()=>{{if(!('speechSynthesis'in window))return;const u=new SpeechSynthesisUtterance(b.dataset.say);u.lang='zh-CN';u.rate=.82;speechSynthesis.cancel();speechSynthesis.speak(u)}}));</script></body></html>'''


# ---------------------------------------------------------------- hub catalogs
def card(lesson: dict) -> str:
    return (
        f'<a class="catalog-card" href="lessons/{e(lesson["slug"])}.html"><div class="tag">{e(lesson.get("level", ""))}</div>'
        f'<h2>{e(lesson["title"])}</h2><p>{e(lesson.get("subtitle", ""))}</p>'
        f'<div class="meta">{e(lesson.get("duration", ""))}　·　{" / ".join(e(t) for t in lesson.get("tags", []))}</div></a>'
    )


def stage_section(stage: dict, items: list[dict]) -> str:
    return (
        f'<section class="course-stage" id="stage-{stage["id"]}"><div class="course-stage-head"><div>'
        f'<div class="section-kicker">{e(stage["title"])}</div><h2>{e(stage["description"])}</h2>'
        f'<div class="stage-english"><b>{e(stage["englishTitle"])}</b><span>{e(stage["englishDescription"])}</span></div>'
        f'</div><span>{len(items)} 节 · {len(items)} lessons</span></div>'
        f'<div class="catalog-grid">{"".join(card(i) for i in items)}</div></section>'
    )


def vocabulary_catalog() -> str:
    sections = []
    assigned = set()
    for stage in STAGES:
        items = [l for l in VOCAB if stage_of(l) == stage["id"]]
        assigned.update(l["slug"] for l in items)
        if items:
            sections.append(stage_section(stage, items))
    extra = [l for l in VOCAB if l["slug"] not in assigned]
    if extra:
        sections.append(
            '<section class="course-stage" id="stage-more"><div class="course-stage-head"><div>'
            '<div class="section-kicker">更多课程 · More lessons</div><h2>继续探索实用场景</h2>'
            '<div class="stage-english"><b>More beginner lessons</b>'
            '<span>Explore more useful topics for everyday Chinese.</span></div></div>'
            f'<span>{len(extra)} 节 · {len(extra)} lessons</span></div>'
            f'<div class="catalog-grid">{"".join(card(l) for l in extra)}</div></section>'
        )
    return "".join(sections)


def grammar_catalog() -> str:
    return f'<div class="catalog-grid">{"".join(card(l) for l in GRAMMAR)}</div>'


def inject_catalog(path: Path, markup: str) -> None:
    text = path.read_text(encoding="utf-8")
    block = f'<!--STATIC_CATALOG_START-->{markup}<!--STATIC_CATALOG_END-->'
    if "<!--STATIC_CATALOG_START-->" in text:
        new = re.sub(
            r"<!--STATIC_CATALOG_START-->.*?<!--STATIC_CATALOG_END-->",
            lambda _: block,
            text,
            flags=re.S,
        )
    elif '<div class="catalog-grid" id="catalogGrid"></div>' in text:
        new = text.replace(
            '<div class="catalog-grid" id="catalogGrid"></div>',
            f'<div class="catalog-grid" id="catalogGrid">{block}</div>',
            1,
        )
    else:
        raise SystemExit(f"no catalog injection target found in {path.name}")
    path.write_text(new, encoding="utf-8")


# ---------------------------------------------------------------- word index
WINDEX_CSS = """
.word-cat{margin:34px 0}
.word-cat h2{font:600 22px var(--serif);border-bottom:1px solid var(--line);padding-bottom:10px}
.word-cat h2 small{font:10px var(--sans);color:#9aa49a;margin-left:8px}
.word-cat ul{list-style:none;padding:0;margin:0;columns:2;column-gap:34px}
.word-cat li{padding:9px 0;border-bottom:1px dotted #e4e9df;font-size:12px;color:#6f7d73;break-inside:avoid}
.word-cat b{font:500 19px var(--serif);color:var(--ink)}
.word-cat .py{color:#d27b5b;font-size:11px;margin-left:5px}
.word-cat .mean{display:block;color:#5f7167;margin-top:3px}
.word-cat .ex{display:block;font-family:var(--serif);color:#87938b;margin-top:2px}
.word-cat li a{font-size:10px;color:var(--green);margin-left:6px;text-decoration:none;border-bottom:1px solid #b3c0ac}
.cat-jump{display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 6px}
.cat-jump a{border:1px solid var(--line);border-radius:99px;padding:6px 11px;font-size:10px;color:#78867c;text-decoration:none;background:var(--white)}
@media(max-width:720px){.word-cat ul{columns:1}}
"""


def word_index_page() -> str:
    words = DATA["words"]
    owner: dict[str, str] = {}
    for lesson in LESSONS:
        for word in lesson.get("words") or []:
            owner.setdefault(word[0], lesson["slug"])

    categories: dict[str, list[dict]] = {}
    for word in words:
        categories.setdefault(word.get("cat", "其他"), []).append(word)
    order = sorted(categories, key=lambda c: (-len(categories[c]), c))

    blocks = []
    for cat in order:
        items = []
        for word in categories[cat]:
            slug = owner.get(word["han"])
            source = (
                f'<a href="lessons/{e(slug)}.html">本课</a>' if slug else '<a href="vocabulary.html">课程目录</a>'
            )
            items.append(
                f'<li><b>{e(word["han"])}</b><span class="py">{e(word["py"])}</span> '
                f'<span class="mean">{e(word.get("en", ""))}</span>'
                f'<span class="ex">{e(word.get("ex", ""))}</span>{source}</li>'
            )
        blocks.append(
            f'<section class="word-cat" id="cat-{e(cat)}"><h2>{e(cat)} <small>{len(categories[cat])} 词</small></h2>'
            f'<ul>{"".join(items)}</ul></section>'
        )

    title = f"Chinese Vocabulary List: {len(words)} Everyday Words with Pinyin"
    description = (
        f"A free index of {len(words)} beginner Mandarin words with pinyin, English meanings, and example sentences, "
        "grouped by everyday topic."
    )
    nav_links = "".join(f'<a href="#cat-{e(cat)}">{e(cat)} {len(categories[cat])}</a>' for cat in order)
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
{head_block(title=title, description=description, url=BASE + "/words.html", page_type="website")}
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="stylesheet" href="styles.css?v=20261023">
<style>{WINDEX_CSS}</style></head>
<body><header class="wrap topbar"><a class="brand" href="index.html"><span class="seal">汉</span><span>汉语慢慢学<small>CHINESE, ONE MOMENT AT A TIME</small></span></a><nav class="nav"><a href="index.html">首页 <span class="nav-en">Home</span></a><a href="vocabulary.html">词汇 <span class="nav-en">Vocabulary</span></a><a href="grammar.html">语法 <span class="nav-en">Grammar</span></a><a href="practice.html">互动练习 <span class="nav-en">Practice</span></a></nav></header>
<main class="wrap"><section class="page-intro"><div class="section-kicker">Word index · 词汇总表</div><h1>全部词汇总表</h1><p>{len(words)} 个基础词条，按主题整理，含拼音、英文释义和例句。Full index of beginner Mandarin words with pinyin, meanings, and example sentences. <a href="vocabulary.html">按课程学习 →</a></p></section>
<nav class="cat-jump">{nav_links}</nav>
{"".join(blocks)}
</main><footer class="footer"><div class="wrap footer-inner"><a class="brand" href="index.html"><span class="seal">汉</span><span>汉语慢慢学<small>CHINESE, ONE MOMENT AT A TIME</small></span></a><p>从一个词开始，慢慢认识一种语言。　© 2026 汉语慢慢学</p><div class="footer-links"><a href="vocabulary.html">课程目录</a><a href="grammar.html">语法课程</a></div></div></footer></body></html>'''


# ---------------------------------------------------------------- static page heads
def upgrade_page(path: Path, *, title: str, description: str, url: str, schema: list[dict] | None = None, page_type: str = "website") -> None:
    text = path.read_text(encoding="utf-8")
    head = head_block(title=title, description=description, url=url, page_type=page_type, schema=schema)
    icons = (
        '<link rel="icon" href="/favicon.svg" type="image/svg+xml">'
        '<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">'
    )
    if "<!--HEAD_MANAGED_START-->" in text:
        text = re.sub(r"<!--HEAD_MANAGED_START-->.*?<!--HEAD_MANAGED_END-->", lambda _: f"<!--HEAD_MANAGED_START-->{head}{icons}<!--HEAD_MANAGED_END-->", text, flags=re.S)
    else:
        # drop the legacy title/description/canonical lines, then insert the managed block
        text = re.sub(r"<title>.*?</title>", "", text, flags=re.S)
        text = re.sub(r'<meta name="description"[^>]*>', "", text)
        text = re.sub(r'<link rel="canonical"[^>]*>', "", text)
        text = text.replace("</head>", f"<!--HEAD_MANAGED_START-->{head}{icons}<!--HEAD_MANAGED_END-->\n</head>", 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    lesson_dir = ROOT / "lessons"
    lesson_dir.mkdir(exist_ok=True)
    for lesson in LESSONS:
        (lesson_dir / f'{lesson["slug"]}.html').write_text(page_for(lesson), encoding="utf-8")

    inject_catalog(ROOT / "vocabulary.html", vocabulary_catalog())
    inject_catalog(ROOT / "grammar.html", grammar_catalog())
    (ROOT / "words.html").write_text(word_index_page(), encoding="utf-8")

    upgrade_page(
        ROOT / "index.html",
        title="Learn Mandarin Chinese for Beginners | 汉语慢慢学",
        description=(
            f"Free Mandarin lessons for beginners: {len(DATA['words'])} words with pinyin and English meanings, "
            f"{len(LESSONS)} step-by-step lessons, and interactive practice. No sign-up needed."
        ),
        url=BASE + "/",
        page_type="website",
        schema=[
            {
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": SITE,
                "alternateName": "Mandarin Happy Learning",
                "url": BASE + "/",
                "inLanguage": "zh-CN",
                "description": "Free beginner Mandarin lessons with pinyin, examples, and interactive practice.",
            },
            {
                "@context": "https://schema.org",
                "@type": "EducationalOrganization",
                "name": SITE,
                "url": BASE + "/",
                "logo": OG_IMAGE,
            },
        ],
    )
    upgrade_page(
        ROOT / "vocabulary.html",
        title="Mandarin Vocabulary for Beginners | Pinyin & Examples",
        description="Learn practical Mandarin vocabulary with pinyin, English meanings, audio, and real-life examples. Browse free beginner lessons by topic.",
        url=BASE + "/vocabulary.html",
        schema=[{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Mandarin Vocabulary for Beginners", "url": BASE + "/vocabulary.html", "inLanguage": "zh-CN"}],
    )
    upgrade_page(
        ROOT / "grammar.html",
        title="Mandarin Grammar for Beginners | Simple Chinese Lessons",
        description="Learn Mandarin grammar step by step with clear English explanations, everyday sentence patterns, examples, and quick exercises.",
        url=BASE + "/grammar.html",
        schema=[{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Mandarin Grammar for Beginners", "url": BASE + "/grammar.html", "inLanguage": "zh-CN"}],
    )
    upgrade_page(
        ROOT / "practice.html",
        title="Free Mandarin Practice Games | Vocabulary & Listening",
        description="Practice Mandarin with free vocabulary, tone, listening, and sentence-building games. Short rounds for beginner learners.",
        url=BASE + "/practice.html",
    )

    pages = ["/", "/vocabulary.html", "/grammar.html", "/practice.html", "/words.html"]
    pages.extend(f'/lessons/{lesson["slug"]}.html' for lesson in LESSONS)
    urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for path in pages:
        item = SubElement(urlset, "url")
        SubElement(item, "loc").text = BASE + path
        SubElement(item, "lastmod").text = BUILD_DATE
    xml = minidom.parseString(tostring(urlset, encoding="utf-8")).toprettyxml(indent="  ", encoding="UTF-8")
    (ROOT / "sitemap.xml").write_bytes(xml)
    print(f'Generated {len(LESSONS)} lesson pages, {len(DATA["words"])} indexed words, sitemap with {len(pages)} URLs.')


if __name__ == "__main__":
    main()
