#!/usr/bin/env python3
"""Generate crawlable, unique HTML pages and an XML sitemap from content.js."""
from __future__ import annotations

import html
import json
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

ROOT = Path(__file__).resolve().parent
BASE = "https://mandarinhappylearning.top"
DATA = json.loads((ROOT / "content.js").read_text(encoding="utf-8").removeprefix("window.CN_CONTENT="))


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def page_for(lesson: dict) -> str:
    slug = lesson["slug"]
    title = lesson["title"]
    kind = "汉语语法" if lesson["type"] == "grammar" else "汉语词汇"
    description = f"{lesson.get('goal', '')} 学习{title}，附拼音、例句和练习。"[:155]
    url = f"{BASE}/lessons/{slug}.html"
    tags = "".join(f'<span class="pill">{e(tag)}</span>' for tag in lesson.get("tags", []))
    body = [
        f'<div class="crumb"><a href="../index.html">首页</a>　/　<a href="../{ "grammar" if lesson["type"] == "grammar" else "vocabulary" }.html">{kind}课程</a></div>',
        f'<div class="lesson-title"><div class="section-kicker">{e(lesson.get("level", "中文课程"))}</div><h1>{e(title)}</h1><div class="subtitle">{e(lesson.get("subtitle", ""))}</div><div class="lesson-meta"><span class="pill">{e(lesson.get("duration", ""))}</span>{tags}</div></div>',
        f'<section class="lesson-section"><h2>本课目标 · Lesson goal</h2><p>{e(lesson.get("goal", ""))}</p><p>{e(lesson.get("intro", ""))}</p></section>',
    ]
    if lesson.get("words"):
        cards = []
        for w in lesson["words"]:
            cards.append(f'<article class="lesson-word"><button class="play" data-say="{e(w[0])}" aria-label="播放{e(w[0])}">▶</button><strong>{e(w[0])}</strong><span class="py">{e(w[1])}</span><div class="meaning">{e(w[2])}</div><div class="example">{e(w[3])}</div><div class="translation">{e(w[4])}</div></article>')
        body.append('<section class="lesson-section"><h2>重点词汇 · Key words</h2><div class="lesson-words">' + "".join(cards) + '</div></section>')
    if lesson.get("pattern"):
        body.append(f'<section class="lesson-section"><h2>表达结构 · Sentence pattern</h2><div class="pattern">{e(lesson["pattern"])}<small>{e(lesson.get("patternEn", ""))}</small></div></section>')
    if lesson.get("examples"):
        items = "".join(f'<li><b>{e(row[0])}</b><span>{e(row[1])}</span></li>' for row in lesson["examples"])
        body.append('<section class="lesson-section"><h2>例句 · Examples</h2><ul class="example-list">' + items + '</ul></section>')
    tip = lesson.get("tip")
    if tip:
        body.append(f'<section class="lesson-section"><h2>学习提示 · Study tip</h2><p>{e(tip)}</p></section>')
    exercise = lesson.get("exercise", {})
    if exercise:
        options = "".join(f'<li>{e(option)}</li>' for option in exercise.get("options", []))
        body.append(f'<section class="lesson-section"><h2>小练习 · Quick check</h2><p>{e(exercise.get("q", ""))}</p><ol>{options}</ol><details><summary>查看答案 · Show answer</summary><p>{e(exercise.get("options", [""])[exercise.get("answer", 0)])} — {e(exercise.get("why", ""))}</p></details></section>')
    body.append(f'<nav class="lesson-nav"><a href="../{ "grammar" if lesson["type"] == "grammar" else "vocabulary" }.html">← 返回课程目录 · Back to lessons</a><a href="../practice.html">去互动练习 · Practice →</a></nav>')
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "首页", "item": BASE + "/"},
        {"@type": "ListItem", "position": 2, "name": kind + "课程", "item": f'{BASE}/{"grammar" if lesson["type"] == "grammar" else "vocabulary"}.html'},
        {"@type": "ListItem", "position": 3, "name": title, "item": url},
    ]}
    breadcrumb_json = json.dumps(breadcrumb, ensure_ascii=False).replace("</", "<\\/")
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)} · {kind} · 汉语慢慢学</title><meta name="description" content="{e(description)}">
<link rel="canonical" href="{e(url)}"><meta name="robots" content="index,follow">
<meta property="og:type" content="article"><meta property="og:site_name" content="汉语慢慢学"><meta property="og:title" content="{e(title)} · {kind} · 汉语慢慢学"><meta property="og:description" content="{e(description)}"><meta property="og:url" content="{e(url)}"><meta property="og:locale" content="zh_CN">
<meta name="twitter:card" content="summary"><meta name="twitter:title" content="{e(title)} · {kind} · 汉语慢慢学"><meta name="twitter:description" content="{e(description)}">
<script type="application/ld+json">{breadcrumb_json}</script><link rel="stylesheet" href="../styles.css?v=20261020"></head>
<body><header class="wrap topbar"><a class="brand" href="../index.html"><span class="seal">汉</span><span>汉语慢慢学<small>CHINESE, ONE MOMENT AT A TIME</small></span></a><nav class="nav"><a href="../index.html">首页 <span class="nav-en">Home</span></a><a href="../vocabulary.html">词汇 <span class="nav-en">Vocabulary</span></a><a href="../grammar.html">语法 <span class="nav-en">Grammar</span></a><a href="../practice.html">互动练习 <span class="nav-en">Practice</span></a></nav></header>
<main class="lesson-shell">{"".join(body)}</main><footer class="footer"><div class="wrap footer-inner"><a class="brand" href="../index.html"><span class="seal">汉</span><span>汉语慢慢学<small>CHINESE, ONE MOMENT AT A TIME</small></span></a><p>从一个词开始，慢慢认识一种语言。　© 2026 汉语慢慢学</p><div class="footer-links"><a href="../vocabulary.html">课程目录</a></div></div></footer>
<script>document.querySelectorAll('[data-say]').forEach(b=>b.addEventListener('click',()=>{{if(!('speechSynthesis'in window))return;const u=new SpeechSynthesisUtterance(b.dataset.say);u.lang='zh-CN';u.rate=.82;speechSynthesis.cancel();speechSynthesis.speak(u)}}));</script></body></html>'''


lesson_dir = ROOT / "lessons"
lesson_dir.mkdir(exist_ok=True)
for lesson in DATA["lessons"]:
    (lesson_dir / f'{lesson["slug"]}.html').write_text(page_for(lesson), encoding="utf-8")

pages = ["/", "/vocabulary.html", "/grammar.html", "/practice.html"]
pages.extend(f'/lessons/{lesson["slug"]}.html' for lesson in DATA["lessons"])
urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
for path in pages:
    item = SubElement(urlset, "url")
    SubElement(item, "loc").text = BASE + path
xml = minidom.parseString(tostring(urlset, encoding="utf-8")).toprettyxml(indent="  ", encoding="UTF-8")
(ROOT / "sitemap.xml").write_bytes(xml)
print(f'Generated {len(DATA["lessons"])} standalone lesson pages and sitemap with {len(pages)} canonical URLs.')
