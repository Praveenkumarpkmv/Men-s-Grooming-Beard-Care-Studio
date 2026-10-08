import re

with open('home-2.html', 'r') as f:
    content = f.read()

old_css = """        .reel-card-body p {
            font-size: 0.78rem;
            color: rgba(255,255,255,0.75);
            line-height: 1.5;
            margin-bottom: 0.9rem;
        }"""

new_css = """        .reel-card-body p {
            font-size: 0.78rem;
            color: rgba(255,255,255,0.75);
            line-height: 1.5;
            margin-bottom: 0.9rem;
            min-height: 5.5rem;
        }"""

content = content.replace(old_css, new_css)

with open('home-2.html', 'w') as f:
    f.write(content)
