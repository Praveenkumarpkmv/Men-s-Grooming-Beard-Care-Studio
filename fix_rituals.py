import re

with open("rituals.html", "r", encoding="utf-8") as f:
    content = f.read()

# I want to replace the first 14 lines of :root with the light theme vars.
old_root = """        :root {
            --bg-black: #111111;
            --text-white: #FFFFFF;
            --accent: #C87A3B;
            --accent-soft: rgba(200, 122, 59, 0.15);
            --border-dim: rgba(200, 122, 59, 0.2);
            --card-bg: #1A1A1A;
            --heading-font: 'Playfair Display', serif;
            --navbar-bg: rgba(17, 17, 17, 0.85);
            --bg-primary: #111111;
            --bg-secondary: #1A1A1A;
            --text-main: #E0DEC8;
            --text-heading: #FFFFFF;
            --footer-text: #A9A48C;"""

new_root = """        :root {
            --bg-black: #FFFFFF;
            --text-white: #111111;
            --accent: #C87A3B;
            --accent-soft: rgba(200, 122, 59, 0.12);
            --border-dim: rgba(0, 0, 0, 0.1);
            --card-bg: #FFFFFF;
            --heading-font: 'Playfair Display', serif;
            --navbar-bg: rgba(255, 255, 255, 0.9);
            --bg-primary: #FFFFFF;
            --bg-secondary: #F3F4F6;
            --text-main: #333333;
            --text-heading: #111111;
            --footer-text: #666666;"""

content = content.replace(old_root, new_root)

with open("rituals.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated root variables to light theme in rituals.html")
