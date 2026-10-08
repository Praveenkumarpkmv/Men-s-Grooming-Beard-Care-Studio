import re

with open('home-2.html', 'r') as f:
    content = f.read()

old_tag = """        .reel-card-tag {
            position: absolute;
            top: 1.5rem;
            left: 1.5rem;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: var(--accent);"""

new_tag = """        .reel-card-tag {
            position: absolute;
            top: 1.5rem;
            left: 1.5rem;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #FFFFFF;"""

content = content.replace(old_tag, new_tag)

with open('home-2.html', 'w') as f:
    f.write(content)
