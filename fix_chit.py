import re

with open('home-2.html', 'r') as f:
    content = f.read()

old_num = """        .chit-num {
            font-family: var(--heading-font);
            font-size: 2.2rem;
            font-weight: 900;
            color: var(--accent);
            opacity: 0.25;"""

new_num = """        .chit-num {
            font-family: var(--heading-font);
            font-size: 2.2rem;
            font-weight: 900;
            color: var(--text-heading);
            opacity: 0.15;"""

content = content.replace(old_num, new_num)

old_price = """        .chit-price {
            font-family: var(--heading-font);
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--accent);
            line-height: 1;
        }"""

new_price = """        .chit-price {
            font-family: var(--heading-font);
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--text-heading);
            line-height: 1;
        }"""

content = content.replace(old_price, new_price)

with open('home-2.html', 'w') as f:
    f.write(content)
