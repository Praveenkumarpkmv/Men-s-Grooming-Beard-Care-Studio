import re

with open('home-2.html', 'r') as f:
    content = f.read()

old_css = """        .reel-card-tag {
            display: inline-block;
            font-size: 0.6rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            font-weight: 800;
            color: var(--accent);
            padding: 0.25rem 0.7rem;
            border-radius: 40px;
            background: rgba(200,122,59,0.2);
            border: 1px solid var(--accent);
            margin-bottom: 0.7rem;
        }"""

new_css = """        .reel-card-tag {
            display: inline-block;
            font-size: 0.6rem;
            letter-spacing: 0.2em;
            text-transform: uppercase;
            font-weight: 800;
            color: #FFFFFF;
            padding: 0.25rem 0.5rem 0.25rem 0.7rem;
            border-radius: 40px;
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.6);
            margin-bottom: 0.7rem;
        }"""

content = content.replace(old_css, new_css)

with open('home-2.html', 'w') as f:
    f.write(content)
