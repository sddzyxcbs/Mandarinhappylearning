"""Hand-written long-form guides. English-first, aimed at the head terms the
generated lesson pages cannot rank for. Rendered by build_seo_pages.py."""

GUIDES = [
    {
        "slug": "chinese-tones",
        "title": "Chinese Tones for Beginners: The 4 Tones (Plus Neutral) Explained",
        "h1": "Chinese Tones for Beginners",
        "dek": "Why mā, má, mǎ and mà are four different words — and how to hear and say all four.",
        "description": "A beginner's guide to Mandarin tones: the four pitch contours plus the neutral tone, tone changes you meet in week one, common mistakes, and daily practice drills.",
        "keywords": ["chinese tones", "mandarin tones", "tone practice", "third tone sandhi"],
        "intro": "Mandarin is not hard because the grammar is complicated — it is hard because the same syllable at four different pitches means four different things. <b>妈 mā</b> is mother, <b>麻 má</b> is hemp, <b>马 mǎ</b> is horse, <b>骂 mà</b> is to scold. Get the tone wrong and the sentence survives; get it wrong consistently and people stop guessing. This guide covers what tones physically are, how to produce them, and the two or three changes that trip up every beginner in the first week.",
        "sections": [
            {
                "h2": "What a tone actually is",
                "p": [
                    "A tone is a pitch contour across one syllable, not a musical note you hold. The pitch of your voice rises, falls, stays level, or dips and rises within roughly the time it takes to say one syllable. Mandarin has four of these contours plus a fifth, the neutral tone, which is short and depends on the tone before it.",
                    "Tones are written above the vowel in pinyin: <b>ā á ǎ à</b>. If you are reading Chinese text without tone marks, you are guessing.",
                ],
                "examples": [
                    ["妈", "mā", "mother — high and level"],
                    ["麻", "má", "hemp — rising, like a question in English"],
                    ["马", "mǎ", "horse — dips low then rises"],
                    ["骂", "mà", "to scold — sharp fall, like an annoyed 'no!'"],
                    ["吗", "ma", "question particle — neutral, short and flat"],
                ],
            },
            {
                "h2": "The four tones, one at a time",
                "table": {
                    "head": ["Tone", "Name", "Contour", "English anchor"],
                    "rows": [
                        ["1st", "阴平 yīn píng", "High and flat (55)", "Saying 'ah' at the doctor, held steady"],
                        ["2nd", "阳平 yáng píng", "Rising (35)", "The 'huh?' you say when you didn't hear"],
                        ["3rd", "上声 shǎng shēng", "Low, dipping (214)", "A reluctant, creaky 'well…'"],
                        ["4th", "去声 qù shēng", "Sharp fall (51)", "A firm 'no'"],
                        ["Neutral", "轻声 qīng shēng", "Short, flat, no stress", "The 'a' in 'about'"],
                    ],
                },
                "p": ["The numbers in brackets are the standard five-point pitch scale: 5 is the top of your comfortable range, 1 the bottom. You do not need to memorise them — they are just a way of writing down what your voice does."],
            },
            {
                "h2": "Three tone changes you meet immediately",
                "p": [
                    "<b>1. Two third tones in a row.</b> The first one becomes a second tone. <b>你好</b> is written <i>nǐ hǎo</i> but pronounced <i>ní hǎo</i>. <b>我很好</b> (wǒ hěn hǎo) comes out <i>wó hén hǎo</i>.",
                    "<b>2. 不 bù before a fourth tone</b> becomes second tone: <b>不是</b> <i>bú shì</i>, <b>不要</b> <i>bú yào</i>. Before everything else it stays fourth: <b>不去</b> <i>bú qù</i> is wrong — it is <i>bú qù</i> only because 去 is fourth tone; <b>不吃</b> is <i>bù chī</i>.",
                    "<b>3. 一 yī changes with what follows.</b> Before a fourth tone it becomes second (<b>一个</b> <i>yí ge</i>), before first, second or third tone it becomes fourth (<b>一天</b> <i>yì tiān</i>), and when counting or at the end it stays first (<b>一二三</b> <i>yī èr sān</i>).",
                ],
                "note": "Textbooks write the original tone; your mouth should not. If a native speaker repeats a word back to you with a different tone than you expected, this is usually why.",
            },
            {
                "h2": "The mistakes English speakers actually make",
                "list": [
                    "<b>Making the first tone too low.</b> English speakers anchor 'level' at their normal speaking pitch. The first tone sits near the top of your comfortable range and stays there.",
                    "<b>Turning the third tone into a deep dive.</b> In connected speech the third tone is mostly just low and slightly creaky; the full dip-and-rise mostly happens when a word is said alone.",
                    "<b>Confusing second and third.</b> Both feel 'not flat'. The second goes up; the third goes down first. If you are unsure, exaggerate: rising vs. low-then-rising.",
                    "<b>Skipping the neutral tone.</b> 吗, 的, 了, 呢, 得 are short and unstressed. Pronouncing them with full tone makes you sound like you are reading a dictionary aloud.",
                ],
            },
            {
                "h2": "How to practise without a teacher",
                "p": [
                    "Ten minutes a day beats an hour on Sunday. The routine that works: (1) say a tone pair aloud while recording, (2) listen back within the same session — the gap between what you think you said and what you said closes fast, (3) repeat with a word you already know rather than a nonsense syllable.",
                    "Minimal pairs are the useful drill, because they force you to hear the difference rather than guess from context:",
                ],
                "examples": [
                    ["妈 / 马", "mā / mǎ", "mother / horse"],
                    ["买 / 卖", "mǎi / mài", "to buy / to sell"],
                    ["问 / 闻", "wèn / wén", "to ask / to smell"],
                    ["书 / 树", "shū / shù", "book / tree"],
                    ["水 / 睡", "shuǐ / shuì", "water / to sleep"],
                ],
                "p": ["Then move to two-syllable words, which is where real speech lives: <b>中国</b> Zhōngguó (1-2), <b>美国</b> Měiguó (3-2), <b>再见</b> zàijiàn (4-4), <b>谢谢</b> xièxie (4-neutral)."],
            },
            {
                "h2": "Where tones fit in your first month",
                "p": [
                    "Do not try to master tones before learning words — that project never ends. Learn thirty high-frequency words with their tones attached, and let every new word carry its contour from day one. Tones are a habit, not a subject.",
                ],
            },
        ],
        "related": ["greetings", "numbers-one-to-five", "chinese-classroom", "polite-requests"],
        "next": "Start with the words where a tone mistake is most expensive: greetings and numbers.",
    },
    {
        "slug": "how-to-say-hello-in-chinese",
        "title": "How to Say Hello in Chinese: 18 Greetings for Every Situation",
        "h1": "How to Say Hello in Chinese",
        "dek": "你好 is correct — and often the wrong choice. Here is what people actually say, by time of day and by relationship.",
        "description": "Learn how to say hello in Chinese properly: 你好, 您好, time-of-day greetings, casual options, phone greetings, and the phrases Chinese speakers use instead of hello.",
        "keywords": ["how to say hello in chinese", "chinese greetings", "nihao", "chinese hello"],
        "intro": "<b>你好 nǐ hǎo</b> is the first phrase every learner meets, and it is genuinely useful — with strangers, in shops, at the start of a language exchange. It is also slightly formal and slightly textbook, which is why a friend you message every day will not open with it. Chinese greetings lean on context: the time of day, whether you have met before, and whether you are speaking or typing.",
        "sections": [
            {
                "h2": "The default: 你好 and 您好",
                "examples": [
                    ["你好！", "nǐ hǎo!", "Hello (neutral, works almost anywhere)"],
                    ["您好！", "nín hǎo!", "Hello (polite — to elders, clients, officials)"],
                    ["大家好！", "dà jiā hǎo!", "Hello everyone (to a group)"],
                ],
                "p": ["您 is the polite 'you'. It matters more than learners expect: using 你 with a much older person or a customer is a small rudeness, and using 您 with a close friend is a small joke. When in doubt in a service or professional setting, use 您好."],
            },
            {
                "h2": "By time of day",
                "table": {
                    "head": ["Chinese", "Pinyin", "When"],
                    "rows": [
                        ["早上好", "zǎo shang hǎo", "Morning, roughly before 10am"],
                        ["上午好", "shàng wǔ hǎo", "Late morning, 10am–noon"],
                        ["中午好", "zhōng wǔ hǎo", "Around midday"],
                        ["下午好", "xià wǔ hǎo", "Afternoon"],
                        ["晚上好", "wǎn shang hǎo", "Evening"],
                        ["晚安", "wǎn ān", "Goodnight — only when parting at night"],
                    ],
                },
                "note": "晚安 is a farewell, not a greeting. Saying it when you arrive at 8pm gets a puzzled look.",
            },
            {
                "h2": "Casual and in-between",
                "list": [
                    "<b>嗨 hāi / 嘿 hēi</b> — borrowed from English, common among younger speakers and in messages.",
                    "<b>喂 wèi</b> — only on the phone. Say it when you pick up, exactly like 'hello?'.",
                    "<b>好久不见 hǎo jiǔ bú jiàn</b> — 'long time no see', for someone you have not met in months.",
                    "<b>最近怎么样？ zuì jìn zěn me yàng?</b> — 'how have you been lately?', a real conversation starter.",
                    "<b>早 zǎo</b> — a clipped 'morning', used between colleagues who pass each other daily.",
                ],
            },
            {
                "h2": "Greetings that are not 'hello'",
                "p": [
                    "Chinese daily life uses observations instead of the word hello, and this is where learners feel the culture gap most.",
                ],
                "examples": [
                    ["吃了吗？", "chī le ma?", "Have you eaten? (friendly, not an invitation)"],
                    ["去哪儿？", "qù nǎr?", "Where are you off to? (casual, not nosy)"],
                    ["上班啊？", "shàng bān a?", "Off to work? (said to a neighbour)"],
                    ["忙吗？", "máng ma?", "Busy? (before asking for something)"],
                ],
                "note": "These are phatic — greetings, not questions. 'Not yet' or 'just out for a walk' is a complete answer. Do not launch into a full account of your day.",
            },
            {
                "h2": "Saying goodbye",
                "examples": [
                    ["再见", "zài jiàn", "Goodbye (standard)"],
                    ["拜拜", "bái bái", "Bye (casual, very common)"],
                    ["明天见", "míng tiān jiàn", "See you tomorrow"],
                    ["回头见", "huí tóu jiàn", "See you later"],
                    ["慢走", "màn zǒu", "Take care (said by host/shop staff as you leave)"],
                ],
            },
            {
                "h2": "Two things to get right",
                "p": [
                    "<b>Tone sandhi.</b> 你好 is written <i>nǐ hǎo</i>, both third tone, but you say <i>ní hǎo</i> — the first one rises. Nobody will misunderstand you either way; getting it right is what makes it sound natural.",
                    "<b>你好吗？ nǐ hǎo ma?</b> Most textbooks teach it. Most Chinese speakers do not say it. It reads like 'how do you do' in English: correct, dated, and slightly translated. Use 最近怎么样 or 你最近好吗 instead.",
                ],
            },
        ],
        "related": ["greetings", "introductions", "polite-requests", "people-and-pronouns"],
        "next": "Learn the greetings lesson properly, including how to introduce yourself in the same breath.",
    },
    {
        "slug": "chinese-numbers",
        "title": "Chinese Numbers 1–100: Counting, Prices and Phone Numbers",
        "h1": "Chinese Numbers from 1 to 100",
        "dek": "The counting system is more regular than English. The traps are 两, 万, money, and reading a phone number aloud.",
        "description": "Learn Chinese numbers 1–100 with pinyin: the 1–10 base, how 11–99 are built, 百 and 万, when to use 两 instead of 二, money, and phone numbers.",
        "keywords": ["chinese numbers", "count in chinese", "chinese numbers 1-100", "liang vs er"],
        "intro": "Mandarin numbers are refreshingly logical: learn ten words and you can say any number under a hundred by stacking them. Then a few irregularities appear — 两 instead of 二, ten thousand instead of a million, and 幺 on the phone — and those are exactly the ones that come up when you are paying for something.",
        "sections": [
            {
                "h2": "1 to 10",
                "table": {
                    "head": ["Number", "Chinese", "Pinyin"],
                    "rows": [
                        ["1", "一", "yī"], ["2", "二", "èr"], ["3", "三", "sān"], ["4", "四", "sì"], ["5", "五", "wǔ"],
                        ["6", "六", "liù"], ["7", "七", "qī"], ["8", "八", "bā"], ["9", "九", "jiǔ"], ["10", "十", "shí"],
                    ],
                },
                "p": ["四 sì (four) and 十 shí (ten) are the two that English speakers mix up. 四 is a sharp falling tone; 十 is a rising one."],
            },
            {
                "h2": "11 to 99: stacking",
                "p": [
                    "Eleven is 'ten one' — <b>十一 shí yī</b>. Twenty is 'two ten' — <b>二十 èr shí</b>. Twenty-five is 'two ten five' — <b>二十五 èr shí wǔ</b>. There are no irregulars in this range at all, which is why counting to 99 is a one-afternoon job.",
                ],
                "examples": [
                    ["十五", "shí wǔ", "15"],
                    ["三十八", "sān shí bā", "38"],
                    ["九十九", "jiǔ shí jiǔ", "99"],
                ],
            },
            {
                "h2": "Hundreds, thousands, and the 万 trap",
                "p": [
                    "Chinese groups numbers by four digits, not three. <b>百 bǎi</b> is hundred, <b>千 qiān</b> is thousand, <b>万 wàn</b> is ten thousand, and <b>亿 yì</b> is a hundred million. There is no word for 'million' — 100,000 is <b>十万 shí wàn</b>.",
                ],
                "examples": [
                    ["一百", "yì bǎi", "100"],
                    ["三百五", "sān bǎi wǔ", "350 (the final digit is dropped in speech)"],
                    ["一千", "yì qiān", "1,000"],
                    ["一万", "yí wàn", "10,000"],
                    ["两万五", "liǎng wàn wǔ", "25,000"],
                ],
                "note": "Spoken Chinese routinely omits the last unit: 三百五 means 350, not 305. In prices and quantities this is the normal form, and it is a common source of confusion for learners.",
            },
            {
                "h2": "二 or 两?",
                "p": [
                    "Both mean two. <b>二 èr</b> is used for counting, in dates, in phone numbers, and in numbers above 100 when it is not followed by a measure word. <b>两 liǎng</b> is used before a measure word — which is most of the time when you are actually buying something.",
                ],
                "examples": [
                    ["两个人", "liǎng ge rén", "two people"],
                    ["两杯咖啡", "liǎng bēi kā fēi", "two cups of coffee"],
                    ["二月二号", "èr yuè èr hào", "February 2nd"],
                    ["二十", "èr shí", "twenty (never 两十)"],
                ],
            },
            {
                "h2": "Money",
                "p": [
                    "The currency unit is <b>元 yuán</b>, but in speech everyone says <b>块 kuài</b>. One tenth is <b>毛 máo</b> (written 角), one hundredth is <b>分 fēn</b>, which is now effectively gone.",
                ],
                "examples": [
                    ["多少钱？", "duō shao qián?", "How much is it?"],
                    ["三十五块", "sān shí wǔ kuài", "35 yuan"],
                    ["八块五", "bā kuài wǔ", "8.50 yuan"],
                    ["太贵了", "tài guì le", "Too expensive"],
                ],
            },
            {
                "h2": "Phone numbers",
                "p": [
                    "Phone numbers are read digit by digit, and 1 is usually <b>幺 yāo</b> rather than 一 yī — because 一 and 七 can blur on a bad line. 0 is <b>零 líng</b>.",
                ],
                "examples": [
                    ["幺三八零零", "yāo sān bā líng líng", "1-3-8-0-0 (start of a mobile number)"],
                    ["你的电话号码是多少？", "nǐ de diàn huà hào mǎ shì duō shao?", "What is your phone number?"],
                ],
            },
            {
                "h2": "Ordinals and floors",
                "p": ["Add <b>第 dì</b> for 'the nth': 第一 dì yī (first), 第三 dì sān (third). Floors are the exception — 一楼 yī lóu is the ground floor, and buildings often skip floors containing 4 because 四 sì sounds like 死 sǐ (to die)."],
            },
        ],
        "related": ["numbers-one-to-five", "numbers-six-to-ten", "vocab-unit-046", "paying-and-shopping", "basic-time-words"],
        "next": "Drill the two number lessons, then use them where they matter: prices and time.",
    },
    {
        "slug": "chinese-sentence-structure",
        "title": "Chinese Sentence Structure: A Beginner's Guide to Word Order",
        "h1": "Chinese Sentence Structure",
        "dek": "Chinese is subject-verb-object — until time, place and aspect particles start moving things around. Here is the frame.",
        "description": "A clear guide to Chinese word order: subject-verb-object, where time and place go, why adjectives need 很, and how 吗, 不, 没, 了 and 过 change a sentence.",
        "keywords": ["chinese sentence structure", "chinese word order", "mandarin grammar", "svo chinese"],
        "intro": "The good news is that Chinese word order is closer to English than most languages: subject, then verb, then object. <b>我喝茶</b> — I drink tea. The work starts when you add when, where, how, and whether the action is finished, because Chinese handles all four with position and small particles rather than with verb endings.",
        "sections": [
            {
                "h2": "The base: subject + verb + object",
                "examples": [
                    ["我喝茶。", "wǒ hē chá.", "I drink tea."],
                    ["他学中文。", "tā xué Zhōngwén.", "He studies Chinese."],
                    ["我们看电影。", "wǒ men kàn diàn yǐng.", "We watch a film."],
                ],
                "p": ["No conjugation, no articles, no plural endings. 我 hē chá works for I drink, you drink, we drank, they will drink — tense comes from context words like 昨天, 明天, or from aspect particles."],
            },
            {
                "h2": "Time goes before the verb, not at the end",
                "examples": [
                    ["我明天去北京。", "wǒ míng tiān qù Běijīng.", "I'm going to Beijing tomorrow."],
                    ["他昨天没来。", "tā zuó tiān méi lái.", "He didn't come yesterday."],
                ],
                "p": ["English puts 'tomorrow' anywhere; Chinese wants it after the subject and before the verb. The same slot holds longer time phrases: <b>我每天早上七点起床</b> — I get up at seven every morning."],
            },
            {
                "h2": "Place uses 在 and sits before the verb too",
                "examples": [
                    ["我在家吃饭。", "wǒ zài jiā chī fàn.", "I eat at home."],
                    ["他住在上海。", "tā zhù zài Shànghǎi.", "He lives in Shanghai."],
                    ["书在桌子上。", "shū zài zhuō zi shang.", "The book is on the table."],
                ],
                "note": "Where English says 'eat at home', Chinese says 'at home eat'. Putting the place after the verb (我吃饭在家) is one of the most recognisable beginner errors.",
            },
            {
                "h2": "Adjectives need 很 — and never 是",
                "examples": [
                    ["我很好。", "wǒ hěn hǎo.", "I'm fine."],
                    ["今天很冷。", "jīn tiān hěn lěng.", "It's cold today."],
                    ["这个菜很好吃。", "zhè ge cài hěn hǎo chī.", "This dish is delicious."],
                ],
                "p": ["In Chinese an adjective is a verb-like predicate; a bare adjective sounds unfinished, so 很 fills the slot. It does not necessarily mean 'very'. And do not say 我是好 — 是 links nouns to nouns, not nouns to adjectives."],
            },
            {
                "h2": "Possession with 的",
                "examples": [
                    ["我的书", "wǒ de shū", "my book"],
                    ["老师的名字", "lǎo shī de míng zi", "the teacher's name"],
                    ["红色的车", "hóng sè de chē", "a red car"],
                ],
            },
            {
                "h2": "Questions: three shapes",
                "list": [
                    "<b>Yes/no with 吗:</b> 你喜欢茶吗？ nǐ xǐ huan chá ma? — statement plus 吗, word order unchanged.",
                    "<b>Question words stay in place:</b> 你叫什么名字？ nǐ jiào shén me míng zi? — literally 'you called what name'. There is no do-support and no inversion.",
                    "<b>Choice with 还是:</b> 你喝茶还是咖啡？ nǐ hē chá hái shi kā fēi? — tea or coffee?",
                ],
            },
            {
                "h2": "Negation splits in two",
                "p": [
                    "<b>不 bù</b> negates present, habitual and future, and adjectives: 我不喝酒 (I don't drink), 他不高 (he isn't tall). <b>没 méi</b> negates 有 and completed actions: 我没有钱 (I don't have money), 我没去 (I didn't go). Saying 不有 or 没去 for a habitual action both mark a beginner.",
                ],
            },
            {
                "h2": "Aspect: 了, 过, 正在",
                "examples": [
                    ["我吃了。", "wǒ chī le.", "I've eaten / I ate."],
                    ["我去过中国。", "wǒ qù guo Zhōngguó.", "I've been to China."],
                    ["他正在打电话。", "tā zhèng zài dǎ diàn huà.", "He's on the phone right now."],
                ],
                "p": ["了 marks a completed action, 过 marks experience, 正在 marks something in progress. None of them is a past tense — Chinese does not have one. <b>明天我吃了饭就去</b> is perfectly normal Chinese about the future."],
            },
            {
                "h2": "The order of everything",
                "p": ["When a sentence gets busy, the skeleton is: <b>subject + time + [在 + place] + [跟 + person] + verb + aspect + object</b>. 我明天在家跟他吃饭 — I'm eating with him at home tomorrow. Fix the skeleton and the vocabulary can be replaced freely."],
            },
        ],
        "related": ["basic-word-order", "questions-with-ma", "adjectives-with-hen", "bu-and-mei", "completed-action-le", "measure-words"],
        "next": "Work through the word-order and question lessons in order — each one adds a slot to the skeleton.",
    },
    {
        "slug": "chinese-measure-words",
        "title": "Chinese Measure Words: 20 You Need, with Examples",
        "h1": "Chinese Measure Words",
        "dek": "You cannot say 'two book' or 'three coffee'. Every number needs a measure word — here are the twenty that cover most of daily life.",
        "description": "Learn Chinese measure words (量词) with pinyin and examples: 个, 本, 张, 只, 条, 件, 杯, 位 and more, plus when 个 is acceptable and when it isn't.",
        "keywords": ["chinese measure words", "liangci", "chinese classifiers", "ge ben zhang"],
        "intro": "English has a few of these — two <i>sheets</i> of paper, three <i>cups</i> of coffee — but Chinese requires one before almost every noun, including nouns where English uses none. 'Two books' is 两本书, never 两书. The measure word is chosen by the shape, container, or category of the thing, and getting it wrong is understood but heard.",
        "sections": [
            {
                "h2": "The structure",
                "p": ["<b>Number + measure word + noun.</b> 一个人 (one person), 三本书 (three books), 两杯咖啡 (two coffees). The same slot is filled by 这/那 (this/that) and 哪 (which): 这个人, 那本书."],
                "examples": [
                    ["一个人", "yí ge rén", "one person"],
                    ["三本书", "sān běn shū", "three books"],
                    ["这杯茶", "zhè bēi chá", "this cup of tea"],
                ],
            },
            {
                "h2": "个: the default you will overuse",
                "p": ["个 gè is the general-purpose measure word and it covers a huge range: people, problems, ideas, apples, companies. Beginners can survive on 个 alone. Native speakers use it constantly too — but they switch to a specific measure word when shape or politeness matters, and those switches are what you want to learn."],
            },
            {
                "h2": "The twenty that do most of the work",
                "table": {
                    "head": ["Measure word", "Pinyin", "Used for", "Example"],
                    "rows": [
                        ["个", "gè", "general default", "一个人 yí ge rén — one person"],
                        ["本", "běn", "books, notebooks", "两本书 liǎng běn shū — two books"],
                        ["张", "zhāng", "flat things: paper, tickets, tables, beds", "一张票 yì zhāng piào — one ticket"],
                        ["只", "zhī", "animals, one of a pair, some objects", "一只猫 yì zhī māo — one cat"],
                        ["条", "tiáo", "long thin things: roads, fish, trousers, news", "一条鱼 yì tiáo yú — one fish"],
                        ["件", "jiàn", "clothing tops, matters, luggage", "一件衣服 yí jiàn yī fu — one piece of clothing"],
                        ["杯", "bēi", "cups and glasses of drink", "一杯水 yì bēi shuǐ — a glass of water"],
                        ["瓶", "píng", "bottles", "两瓶啤酒 liǎng píng pí jiǔ — two bottles of beer"],
                        ["碗", "wǎn", "bowls of food", "一碗面 yì wǎn miàn — a bowl of noodles"],
                        ["双", "shuāng", "pairs: shoes, socks, chopsticks", "一双鞋 yì shuāng xié — a pair of shoes"],
                        ["位", "wèi", "people, politely", "三位客人 sān wèi kè rén — three guests"],
                        ["名", "míng", "people, in writing or formal lists", "两名学生 liǎng míng xué sheng — two students"],
                        ["辆", "liàng", "vehicles", "一辆车 yí liàng chē — one car"],
                        ["台", "tái", "machines, computers, TVs", "一台电脑 yì tái diàn nǎo — one computer"],
                        ["间", "jiān", "rooms", "一间房 yì jiān fáng — one room"],
                        ["家", "jiā", "companies, shops, restaurants", "一家公司 yì jiā gōng sī — one company"],
                        ["份", "fèn", "portions, copies, documents", "一份工作 yí fèn gōng zuò — one job"],
                        ["次", "cì", "times (occurrences)", "去过两次 qù guo liǎng cì — been twice"],
                        ["遍", "biàn", "times, complete repetitions", "再说一遍 zài shuō yí biàn — say it again"],
                        ["场", "chǎng", "events: films, games, rain", "一场雨 yì chǎng yǔ — a rain shower"],
                    ],
                },
            },
            {
                "h2": "个 or 位 for people?",
                "p": ["个 is neutral; 位 is polite and slightly formal, used for customers, guests, and people you are serving. 这位先生 (this gentleman) is respectful; 这个人 (this person) can sound dismissive depending on tone. In a restaurant you will hear 几位？ — 'how many (people)?'"],
            },
            {
                "h2": "Questions about quantity",
                "examples": [
                    ["几个人？", "jǐ ge rén?", "How many people? (expected answer under ten)"],
                    ["多少钱？", "duō shao qián?", "How much money? (open-ended)"],
                    ["你要几个？", "nǐ yào jǐ ge?", "How many do you want?"],
                ],
                "p": ["几 jǐ expects a small number and needs a measure word. 多少 duō shao is open-ended and can drop it: 多少人 (how many people), 多少钱 (how much money)."],
            },
            {
                "h2": "The mistakes worth fixing first",
                "list": [
                    "<b>Dropping the measure word.</b> 两书 and 三咖啡 are not 'casual' — they are ungrammatical.",
                    "<b>Using 个 for everything in a shop.</b> Understandable, but 一件衣服 and 一双鞋 are what a shop assistant expects.",
                    "<b>Forgetting the tone change.</b> 一个 is pronounced <i>yí ge</i>, not <i>yī ge</i>, because 一 before a fourth tone becomes second tone.",
                ],
            },
        ],
        "related": ["measure-words", "classifiers-ben-zhang", "food-and-measures", "shopping-basics", "grammar-033"],
        "next": "Do the measure-word lesson, then buy something in the shopping lesson and watch how often they appear.",
    },
    {
        "slug": "learn-chinese-characters",
        "title": "How to Learn Chinese Characters: Radicals, Stroke Order and the First 300",
        "h1": "How to Learn Chinese Characters",
        "dek": "Characters are not 5,000 drawings. They are a few hundred components, recombined — which changes the whole learning plan.",
        "description": "A practical method for learning Chinese characters: how components and radicals work, stroke order rules, how many characters you actually need, and how to review them.",
        "keywords": ["learn chinese characters", "chinese radicals", "stroke order", "hsk characters"],
        "intro": "The number that scares people is 50,000 — the size of a large dictionary. The number that matters is smaller: about 3,000 characters cover 99% of modern written Chinese, and the 300 most frequent ones already cover roughly half of the characters you will meet on a page. Characters are built from components, and once you can see the components the shapes stop being arbitrary.",
        "sections": [
            {
                "h2": "Characters are components, not pictures",
                "p": ["Most characters are made of two or more parts, each carrying either meaning or sound. <b>妈 mā</b> (mother) is 女 'woman' + 马 mǎ, which is there for the sound. <b>钱 qián</b> (money) is 钅 'metal' + 戋. Once you learn 女, 马, 钅, you stop memorising 妈 and 钱 as unique drawings."],
                "examples": [
                    ["妈 = 女 + 马", "mā = nǚ + mǎ", "mother: meaning 'woman' + sound 'ma'"],
                    ["想 = 相 + 心", "xiǎng = xiāng + xīn", "to think: 'appearance' + 'heart'"],
                    ["河 = 氵 + 可", "hé = shuǐ + kě", "river: water radical + sound"],
                ],
            },
            {
                "h2": "The radicals worth learning on day one",
                "table": {
                    "head": ["Radical", "Meaning", "Where it sits", "Examples"],
                    "rows": [
                        ["氵", "water", "left", "河 海 洗 — river, sea, wash"],
                        ["亻", "person", "left", "你 他 住 — you, he, live"],
                        ["讠", "speech", "left", "说 话 请 — speak, words, please"],
                        ["扌", "hand", "left", "打 拿 找 — hit, take, look for"],
                        ["心 / 忄", "heart", "bottom / left", "想 忙 怕 — think, busy, fear"],
                        ["口", "mouth", "left / around", "吃 喝 叫 — eat, drink, call"],
                        ["木", "wood", "left", "树 桌 椅 — tree, table, chair"],
                        ["火", "fire", "left / bottom", "热 灯 烧 — hot, lamp, burn"],
                        ["金 / 钅", "metal", "left", "钱 银 铁 — money, silver, iron"],
                        ["目", "eye", "left", "看 眼 睛 — look, eye, eyeball"],
                    ],
                },
            },
            {
                "h2": "Stroke order: five rules",
                "list": [
                    "Top to bottom: 三, 言.",
                    "Left to right: 你, 好.",
                    "Horizontal before vertical: 十, 干.",
                    "Outside before inside: 月, 问 — then close the box: 国, 回.",
                    "Middle before the two sides: 小, 水.",
                ],
                "p": ["Stroke order is not decoration. It decides how handwriting looks, how handwriting recognition reads your input, and how you remember the shape. Learn it while the character count is small — relearning it at 800 characters is miserable."],
            },
            {
                "h2": "How many characters do you need?",
                "table": {
                    "head": ["Characters", "What it unlocks"],
                    "rows": [
                        ["100", "Signs, menus, numbers, the most common function words"],
                        ["300", "About half of the characters on a news page; everyday SMS"],
                        ["600", "Short articles with a dictionary at hand — roughly HSK 3–4 reading"],
                        ["1,000", "Comfortable reading of simple fiction and news — roughly HSK 5"],
                        ["3,000", "99% of modern written text"],
                    ],
                },
            },
            {
                "h2": "A method that survives month three",
                "p": [
                    "<b>Learn words, not characters.</b> 银行 yínháng (bank) is one word made of two characters you may already know; memorising 银 and 行 separately costs twice the effort and teaches half the usage.",
                    "<b>Recognition before production.</b> Reading and typing need recognition; handwriting needs production. Most learners need handwriting for a few hundred characters at most. Type pinyin and let the input method do the rest.",
                    "<b>Review on a schedule, not on mood.</b> Ten new characters a day with spaced repetition beats fifty on Sunday. Review is where the learning actually happens; the first pass is just exposure.",
                    "<b>Read something you can almost read.</b> Graded readers and the lessons on this site exist for this: text where you know 80–90% of the characters and the rest is guessable from context.",
                ],
            },
            {
                "h2": "What not to do",
                "list": [
                    "Copying characters twenty times each. It feels productive and teaches your hand, not your memory.",
                    "Learning characters in frequency-list order with no words attached.",
                    "Waiting until you 'know pinyin properly' before starting characters. They reinforce each other.",
                ],
            },
        ],
        "related": ["chinese-classroom", "classroom-words", "study-tools", "campus-life"],
        "next": "Try the classroom lesson — it is built from characters you have just seen explained.",
    },
    {
        "slug": "chinese-pinyin-guide",
        "title": "Pinyin Guide: How to Read, Type and Pronounce Mandarin",
        "h1": "A Practical Guide to Pinyin",
        "dek": "Pinyin looks like English spelling and is not. Here are the sounds that actually differ, and the rules that make the rest predictable.",
        "description": "Learn how to read pinyin properly: initials and finals, the ü sound, tone mark placement, spelling rules, the English-speaker traps (x, q, zh, c, r), and how to type Chinese.",
        "keywords": ["pinyin guide", "how to read pinyin", "pinyin pronunciation", "type chinese pinyin"],
        "intro": "Pinyin is a romanisation system, not English spelling. Most syllables sound close to what an English speaker would guess, which is exactly the problem: the dozen that don't are the ones you will mispronounce for years if nobody tells you. This guide is about those dozen.",
        "sections": [
            {
                "h2": "The shape of a syllable",
                "p": ["Every syllable is an optional initial (consonant) plus a final (vowel or vowel + nasal). <b>mā</b> = initial m + final a. <b>zhōng</b> = initial zh + final ong. There are 21 initials and about 35 finals, and only around 400 syllables in total — which is why Chinese has so many homophones."],
            },
            {
                "h2": "The initials that are not what they look like",
                "table": {
                    "head": ["Pinyin", "Sounds like", "Not like", "Example"],
                    "rows": [
                        ["x", "soft 'sh' with lips spread — <i>shy</i> without the tongue curl", "English 'ks'", "谢谢 xièxie"],
                        ["q", "hard 'ch' — <i>cheese</i>", "English 'k'", "请 qǐng"],
                        ["c", "ts as in <i>cats</i>", "English 'k' or 's'", "菜 cài"],
                        ["z", "ds as in <i>reads</i>", "English 'z'", "早上 zǎoshang"],
                        ["zh", "retroflex 'j' — tongue curled back", "'z' + 'h'", "中文 Zhōngwén"],
                        ["ch", "retroflex 'ch' — tongue curled back", "'c' + 'h'", "吃 chī"],
                        ["sh", "retroflex 'sh'", "'s' + 'h'", "书 shū"],
                        ["r", "between English 'r' and 'zh'", "rolled or English r", "人 rén"],
                        ["j", "like 'j' in <i>jeep</i>, but softer", "'y'", "几 jǐ"],
                    ],
                },
                "note": "The single most useful correction: x/q/j are made with the tongue flat behind the lower teeth, not curled back. zh/ch/sh are the curled-back versions of the same places.",
            },
            {
                "h2": "Finals worth extra attention",
                "list": [
                    "<b>ü</b> — say 'ee' then round your lips without moving your tongue. <b>女 nǚ</b>, <b>绿 lǜ</b>. After j, q, x, y it is written <b>u</b> but still pronounced ü: <b>去 qù</b>, <b>鱼 yú</b>.",
                    "<b>-n vs -ng</b> — <b>安 ān</b> ends with the tongue on the ridge behind the teeth; <b>昂 áng</b> ends in the back of the mouth. <b>分 fēn</b> vs <b>风 fēng</b>.",
                    "<b>-ian</b> — not 'ee-an' but closer to 'yen': <b>天 tiān</b>, <b>钱 qián</b>.",
                    "<b>-ong</b> — like 'oong': <b>中 zhōng</b>, <b>红 hóng</b>.",
                    "<b>e</b> — a back, unrounded 'uh': <b>喝 hē</b>, <b>很 hěn</b>.",
                ],
            },
            {
                "h2": "Where the tone mark goes",
                "p": ["Tone marks sit on the vowel in this priority order: <b>a, o, e, i, u, ü</b>. So <b>hǎo</b> (on a), <b>duì</b> (on i), <b>liù</b> (on u), <b>lǜ</b> (on ü). When i carries a mark, the dot disappears: <b>nǐ</b>. Neutral tone takes no mark at all."],
            },
            {
                "h2": "Spelling rules that surprise people",
                "list": [
                    "No syllable starts with i or u alone: <b>yi</b> for i, <b>wu</b> for u, <b>yu</b> for ü.",
                    "<b>j, q, x</b> take <b>u</b> where the sound is ü: ju, qu, xu — never jü.",
                    "After <b>y</b>, ü loses its dots: <b>yuan</b>, <b>yun</b>.",
                    "Syllables are separated with an apostrophe when ambiguity would result: <b>Xī'ān</b> (Xi'an) vs <b>xiān</b> (fresh).",
                    "Names and places capitalise each syllable: <b>Běijīng</b>, <b>Zhāng Wěi</b>.",
                ],
            },
            {
                "h2": "Typing Chinese",
                "p": ["You do not need to learn a keyboard layout. Every major OS ships a pinyin input method: type <i>nihao</i>, pick 你好 from the candidate list. Type whole words rather than single characters — <i>zhongwen</i> gives 中文 immediately, while <i>zhong</i> asks you to choose among dozens. Tones are not typed; the input method guesses from context."],
            },
            {
                "h2": "A 10-minute daily routine",
                "list": [
                    "Read one short passage aloud with tone marks — slow enough to hear yourself.",
                    "Record 30 seconds of it, then listen once. Do not loop on it.",
                    "Pick three syllables you fumbled and say minimal pairs for them.",
                    "Add any new word to your review list with its pinyin attached.",
                ],
            },
        ],
        "related": ["greetings", "chinese-classroom", "numbers-one-to-five", "polite-requests"],
        "next": "Read pinyin aloud from the greetings lesson — it is the highest-frequency vocabulary there is.",
    },
    {
        "slug": "ordering-food-in-chinese",
        "title": "How to Order Food in Chinese: 25 Phrases for Restaurants",
        "h1": "How to Order Food in Chinese",
        "dek": "From 'table for two' to 'doggy bag', the phrases that get you fed — with spice levels, dietary limits and the bill.",
        "description": "Order food in Chinese with confidence: getting a table, asking for a menu, ordering, adjusting spice, saying you are vegetarian, and paying — with pinyin and examples.",
        "keywords": ["order food in chinese", "chinese restaurant phrases", "chinese menu", "mai dan"],
        "intro": "Restaurant Chinese is one of the best places to start speaking, because the script is predictable: someone asks how many, hands you a menu, takes your order, brings the bill. Learn ten exchanges and you can eat anywhere from a noodle shop to a banquet hall.",
        "sections": [
            {
                "h2": "Getting seated",
                "examples": [
                    ["几位？", "jǐ wèi?", "How many (people)? — what staff ask you first"],
                    ["两位。", "liǎng wèi.", "Two, please."],
                    ["有位置吗？", "yǒu wèi zhi ma?", "Do you have a table?"],
                    ["我们想坐靠窗的位置。", "wǒ men xiǎng zuò kào chuāng de wèi zhi.", "We'd like a table by the window."],
                ],
                "p": ["Answer with 位 wèi rather than 个 ge in a restaurant — it is the polite measure word for people and it is what the staff used."],
            },
            {
                "h2": "The menu",
                "examples": [
                    ["菜单", "cài dān", "menu"],
                    ["有英文菜单吗？", "yǒu Yīngwén cài dān ma?", "Do you have an English menu?"],
                    ["有什么推荐的？", "yǒu shén me tuī jiàn de?", "What do you recommend?"],
                    ["招牌菜是什么？", "zhāo pai cài shì shén me?", "What's your signature dish?"],
                    ["这个是什么？", "zhè ge shì shén me?", "What is this?"],
                ],
            },
            {
                "h2": "Ordering",
                "examples": [
                    ["我要一个…", "wǒ yào yí ge…", "I'd like one…"],
                    ["请给我…", "qǐng gěi wǒ…", "Please give me…"],
                    ["来两个啤酒。", "lái liǎng ge pí jiǔ.", "Two beers, please."],
                    ["再来一份米饭。", "zài lái yí fèn mǐ fàn.", "Another bowl of rice, please."],
                    ["够了，谢谢。", "gòu le, xiè xie.", "That's enough, thanks."],
                ],
                "p": ["<b>来 lái</b> ('bring') is the workhorse verb for ordering: 来一碗面 — a bowl of noodles, please. <b>要 yào</b> is more direct. Adding <b>请 qǐng</b> or <b>麻烦你 má fan nǐ</b> softens either."],
            },
            {
                "h2": "Spice and adjustments",
                "table": {
                    "head": ["Chinese", "Pinyin", "Meaning"],
                    "rows": [
                        ["不要辣", "bú yào là", "not spicy"],
                        ["微辣", "wēi là", "mildly spicy"],
                        ["中辣", "zhōng là", "medium"],
                        ["很辣", "hěn là", "very spicy"],
                        ["不要放香菜", "bú yào fàng xiāng cài", "no coriander"],
                        ["少放盐", "shǎo fàng yán", "less salt"],
                        ["不要冰", "bú yào bīng", "no ice"],
                        ["打包", "dǎ bāo", "to take away / doggy bag"],
                    ],
                },
                "note": "In Sichuan and Hunan, 微辣 is still hot by most visitors' standards. If you mean 'not spicy at all', say 一点辣都不要 — not even a little.",
            },
            {
                "h2": "Dietary limits",
                "examples": [
                    ["我吃素。", "wǒ chī sù.", "I'm vegetarian."],
                    ["我不吃肉。", "wǒ bù chī ròu.", "I don't eat meat."],
                    ["我对花生过敏。", "wǒ duì huā shēng guò mǐn.", "I'm allergic to peanuts."],
                    ["里面有猪肉吗？", "lǐ miàn yǒu zhū ròu ma?", "Does it contain pork?"],
                ],
                "p": ["Vegetarianism is less common in mainland China than in many other places, so 素 dishes may still be cooked with meat stock or lard. 全素 (fully vegetarian) and 不要放肉 (no meat) are worth adding if it matters."],
            },
            {
                "h2": "Drinks and extras",
                "examples": [
                    ["一杯热水", "yì bēi rè shuǐ", "a glass of hot water (the default in many restaurants)"],
                    ["一瓶矿泉水", "yì píng kuàng quán shuǐ", "a bottle of mineral water"],
                    ["有纸巾吗？", "yǒu zhǐ jīn ma?", "Do you have tissues? (often charged separately)"],
                    ["再来点米饭", "zài lái diǎn mǐ fàn", "a bit more rice"],
                ],
            },
            {
                "h2": "Paying",
                "examples": [
                    ["买单。", "mǎi dān.", "The bill, please. (southern China)"],
                    ["结账。", "jié zhàng.", "The bill, please. (northern China)"],
                    ["多少钱？", "duō shao qián?", "How much?"],
                    ["可以刷卡吗？", "kě yǐ shuā kǎ ma?", "Can I pay by card?"],
                    ["可以用微信支付吗？", "kě yǐ yòng Wēi xìn zhī fù ma?", "Can I pay with WeChat Pay?"],
                    ["我要发票。", "wǒ yào fā piào.", "I need a receipt (official tax invoice)."],
                ],
                "p": ["Mobile payment is dominant in mainland China; many small restaurants no longer keep cash. 发票 fāpiào is the official tax receipt, and it is a different document from a printed order slip."],
            },
            {
                "h2": "Three phrases that carry the whole meal",
                "list": [
                    "<b>麻烦你 má fan nǐ</b> — 'sorry to trouble you', the universal polite opener before any request.",
                    "<b>一下 yí xià</b> — softens a verb: 看一下 (take a look), 等一下 (wait a moment). Requests with 一下 sound much less blunt.",
                    "<b>谢谢 xiè xie</b> — said to staff on the way out, not after every plate.",
                ],
            },
        ],
        "related": ["at-the-cafe", "meals-and-food", "food-and-measures", "polite-requests", "payment-details"],
        "next": "Practise with the café and meals lessons, then run the same script the next time you eat out.",
    },
]


FAQ_BY_SLUG = {
    "chinese-tones": [
        ("Do I really have to learn tones?",
         "If you want to be understood without effort, yes. Context rescues a lot, but a learner who ignores tones makes every sentence a small puzzle for the listener — and the listener usually switches to English rather than ask you to repeat."),
        ("How long until I can hear the four tones?",
         "Hearing the four-way contrast usually takes a few weeks of daily listening. Producing them reliably, without thinking, takes a few months. The gap between the two is normal."),
        ("Are tones the same in Taiwan?",
         "Taiwanese Mandarin uses the same four tones and largely the same system. Vocabulary differs, 儿化 is much rarer, and some neutral tones are pronounced more fully."),
        ("What is the fifth tone?",
         "The neutral tone — short, unstressed syllables such as 吗, 的, 了, and the second syllable of 谢谢. It is not a fixed pitch; it follows the tone before it."),
    ],
    "how-to-say-hello-in-chinese": [
        ("Is 你好 rude or too formal?",
         "Neither. It is neutral and safe with strangers, in shops, and in writing. Between close friends it can sound slightly distant, the way 'good day' does in English."),
        ("How do I greet an older person or a teacher?",
         "Use 您好 and add the title: 王老师，您好. Dropping 您 with someone clearly senior to you reads as careless rather than friendly."),
        ("Why do people ask 吃了吗 instead of hello?",
         "It is a phatic greeting, roughly 'how are you getting on'. It is not an invitation to dinner, and 'not yet' is a complete answer."),
        ("Should I use 你好吗?",
         "Rarely. It is grammatically fine and textbook-common, but native speakers mostly say 最近怎么样 or 你最近好吗 instead."),
    ],
    "chinese-numbers": [
        ("Why is two sometimes 二 and sometimes 两?",
         "两 goes before a measure word (两个人, 两杯咖啡). 二 is used for counting, dates, phone numbers, and in numbers like 二十. Before 十 it is always 二."),
        ("What is 万 in English?",
         "Ten thousand. Chinese groups by four digits, so a million is 一百万 (one hundred ten-thousands), and there is no single word for million."),
        ("How do I read 19.9 yuan?",
         "十九块九 — nineteen kuai nine. The unit after the decimal is 毛 for one digit, so 8.50 is 八块五."),
        ("Is 一 always pronounced yī?",
         "No. Before a fourth tone it becomes yí (一个 yí ge); before first, second or third tone it becomes yì (一天 yì tiān). When counting it stays yī."),
    ],
    "chinese-sentence-structure": [
        ("Is Chinese really subject-verb-object?",
         "The basic order is SVO, but topic-comment structures are extremely common: 这个菜，我很喜欢 (this dish, I like very much). Learn SVO first; topic-comment comes with exposure."),
        ("Why can't I say 我是高 for 'I am tall'?",
         "是 links nouns to nouns. Adjectives are predicates on their own and take 很 as a placeholder: 我很高."),
        ("Where does 了 go?",
         "After the verb for a completed action (我吃了饭), or at the end of the sentence when it marks a change of state (下雨了)."),
        ("Do Chinese verbs conjugate?",
         "No. There are no tense or person endings at all. Time is carried by words like 昨天, 明天, and by aspect particles such as 了 and 过."),
    ],
    "chinese-measure-words": [
        ("Can I just use 个 for everything?",
         "You will be understood, and beginners do it constantly. It sounds casual with books, clothing, and vehicles — 一本书, 一件衣服, 一辆车 are what people expect."),
        ("Do measure words change tone?",
         "They follow normal tone sandhi. 一个 is pronounced yí ge because 一 becomes second tone before a fourth-tone syllable."),
        ("Which measure word is polite for people?",
         "位 for customers, guests and strangers; 名 in formal lists and writing; 个 as the neutral default. Restaurant staff will ask 几位?"),
        ("Is there a measure word for 'times'?",
         "次 for occurrences (去过两次) and 遍 for complete repetitions of an action (再说一遍)."),
    ],
    "learn-chinese-characters": [
        ("How many characters do I need to read a newspaper?",
         "About 3,000 covers roughly 99% of modern written text. Around 1,000 is enough for simple news and graded readers."),
        ("Simplified or traditional characters?",
         "Mainland China and Singapore use simplified; Taiwan, Hong Kong and Macau use traditional. Learn the system used by the people you actually talk to — the shared core is large."),
        ("Do I need to handwrite?",
         "Not for most goals. Reading and typing need recognition only. Handwriting helps memory and is required for exams and forms, so most learners handwrite a few hundred characters and recognise the rest."),
        ("Why do characters look like pictures but aren't?",
         "A small number are pictographic (日 sun, 山 mountain). Most are compounds of a meaning component and a sound component, which is why learning components pays off so quickly."),
    ],
    "chinese-pinyin-guide": [
        ("Do Chinese people use pinyin?",
         "Yes — as the input method for typing, for children learning characters, and in dictionaries. Taiwan uses zhuyin (bopomofo) for the same job, though pinyin is standard for learners."),
        ("Why is 去 written qu and not qü?",
         "After j, q, x and y the ü sound is written u. It is still pronounced ü. The dots only appear after n and l: 女 nǚ, 绿 lǜ."),
        ("Do I type tones?",
         "No. Pinyin input methods take unmarked letters and predict the characters from context. Type whole words — zhongwen gives 中文 faster than zhong."),
        ("Can I learn Chinese without pinyin?",
         "You can learn to speak from audio, but pinyin is how you look words up, type them, and remember pronunciation. It is worth two weeks of focused attention early."),
    ],
    "ordering-food-in-chinese": [
        ("How do I say 'not spicy'?",
         "不要辣 or 不辣. If you want reassurance, add 一点辣都不要 — not even a little. 微辣 still means mild spice, which is hot for many visitors."),
        ("Is it rude to call the waiter 服务员?",
         "It is common and not offensive, but it can sound like summoning. 你好 or 麻烦你 plus eye contact is softer, and 老板 works in small shops."),
        ("How do I ask for the bill?",
         "买单 (southern China) or 结账 (northern China). Add 谢谢, and expect to pay at the counter in smaller restaurants."),
        ("Should I tip?",
         "No. Tipping is not customary in mainland China. Service charges appear only in upscale hotels and some foreign restaurants."),
    ],
}
