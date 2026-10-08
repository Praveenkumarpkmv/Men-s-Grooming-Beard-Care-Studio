import re
import os

css_to_add = """
        /* ══════════════════════════════════════════
           PAGE HERO
           ══════════════════════════════════════════ */
        .page-hero {
            position: relative;
            padding: 9rem 0 5rem;
            background:
                linear-gradient(135deg, rgba(17,17,17,0.92) 0%, rgba(17,17,17,0.7) 60%, rgba(200,122,59,0.25) 100%),
                url('{bg_image}') center/cover;
            text-align: center;
            border-bottom: 1px solid var(--border-dim);
        }
        [data-theme="light"] .page-hero {
            background: linear-gradient(135deg, #FFFFFF 0%, #F3F4F6 100%), url('{bg_image}') center/cover;
            background-blend-mode: overlay;
        }
        [data-theme="light"] .page-hero h1,
        [data-theme="light"] .page-hero p { color: #111; }
        .page-hero::after {
            content: '';
            position: absolute;
            left: 0; right: 0; bottom: 0;
            height: 3px;
            background: linear-gradient(90deg, transparent, var(--accent), transparent);
            opacity: 0.6;
        }
        .page-hero-inner { position: relative; z-index: 2; }
        .page-hero .crumb {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.78rem;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: var(--accent);
            background: rgba(0,0,0,0.5);
            padding: 0.4rem 1.1rem;
            border-radius: 40px;
            margin-bottom: 1.2rem;
            backdrop-filter: blur(6px);
            font-weight: 700;
        }
        [data-theme="light"] .page-hero .crumb { background: var(--accent-soft); }
        .page-hero h1 {
            font-size: clamp(2.4rem, 5vw, 3.8rem);
            color: #fff;
            margin-bottom: 1rem;
            font-weight: 800;
        }
        .page-hero h1 span {
            background: linear-gradient(135deg, var(--accent), #F0B27A);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .page-hero p {
            color: rgba(255,255,255,0.85);
            max-width: 640px;
            margin: 0 auto;
            font-size: 1.02rem;
        }
"""

hero_template = """<section class="page-hero">
    <div class="container page-hero-inner">
        <span class="crumb"><i class="fas fa-{icon}"></i> {eyebrow}</span>
        <h1>{title1} <span>{title2}</span></h1>
        <p>{desc}</p>
    </div>
</section>"""

pages = [
    {
        "file": "about.html",
        "class": "ab-hero",
        "bg_image": "asserts/about1.avif",
        "icon": "info-circle",
        "eyebrow": "The Story",
        "title1": "We didn't open",
        "title2": "a barbershop",
        "desc": "We built a room where men can sit still and be taken seriously for forty-five minutes. – Marcus Hale, Founder"
    },
    {
        "file": "beard-care.html",
        "class": "bd-hero",
        "bg_image": "asserts/bc1.avif",
        "icon": "leaf",
        "eyebrow": "Beard Care · Apothecary",
        "title1": "Treat your beard like",
        "title2": "it's got a job to do.",
        "desc": "A beard is a daily thing. Oils to soften it, balms to shape it, blades to line it, and a barber who actually knows the difference. This is the whole ritual, laid out plainly."
    },
    {
        "file": "blade-and-bone.html",
        "class": "bb-hero",
        "bg_image": "asserts/bb1.avif",
        "icon": "cut",
        "eyebrow": "Craft · Chapter 02",
        "title1": "The blade.",
        "title2": "& The bone.",
        "desc": "Two things decide every cut before a single hair is touched — the edge doing the work, and the shape underneath it. This is what we actually think about when you sit down."
    },
    {
        "file": "grooming.html",
        "class": "gr-hero",
        "bg_image": "asserts/grm1.avif",
        "icon": "star",
        "eyebrow": "Grooming · Est. 2018",
        "title1": "Every cut has a",
        "title2": "reason behind it",
        "desc": "Not a menu of options — a set of decisions made for your hair, your face, and how you actually live. We talk first, cut second."
    },
    {
        "file": "lookbook.html",
        "class": "lb-hero",
        "bg_image": "asserts/bb4.avif",
        "icon": "camera",
        "eyebrow": "Lookbook · Vol. 04",
        "title1": "Sharp cuts.",
        "title2": "Sharper character.",
        "desc": "A collection of recent cuts, fades, and beard sculpts from the Iron & Oak chairs. This is what the work actually looks like."
    },
    {
        "file": "rituals.html",
        "class": "rt-hero",
        "bg_image": "asserts/rit1.avif",
        "icon": "book-open",
        "eyebrow": "The Field Guide · Vol. 01",
        "title1": "The modern",
        "title2": "grooming rituals.",
        "desc": "The things you should be doing, the things you can stop doing, and exactly how to maintain what we built in the chair."
    }
]

for p in pages:
    with open(p["file"], "r", encoding="utf-8") as f:
        content = f.read()

    # Inject CSS before </style>
    css_injected = css_to_add.replace("{bg_image}", p["bg_image"])
    
    if ".page-hero {" not in content:
        content = content.replace("</style>", css_injected + "\n</style>")

    # Replace hero section
    new_html = hero_template.format(
        icon=p["icon"],
        eyebrow=p["eyebrow"],
        title1=p["title1"],
        title2=p["title2"],
        desc=p["desc"]
    )
    
    pattern = r'<section class="' + p["class"] + r'">.*?</section>'
    content = re.sub(pattern, new_html, content, flags=re.DOTALL)

    with open(p["file"], "w", encoding="utf-8") as f:
        f.write(content)

print("Updated heroes!")
