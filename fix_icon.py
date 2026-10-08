import re

with open('home-2.html', 'r') as f:
    content = f.read()

old_css = """        .reserve-card.accent .reserve-card-icon {
            background: rgba(10,10,10,0.15);
            border-color: rgba(10,10,10,0.2);
            color: #0A0A0A;
        }"""

new_css = """        .reserve-card.accent .reserve-card-icon {
            background: rgba(10,10,10,0.15);
            border-color: rgba(10,10,10,0.2);
            color: #FFFFFF;
        }"""

content = content.replace(old_css, new_css)

with open('home-2.html', 'w') as f:
    f.write(content)
