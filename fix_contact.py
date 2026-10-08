import re

with open('contact.html', 'r') as f:
    content = f.read()

old_card = """        .contact-card {
            background: var(--card-bg);
            border: 1px solid var(--border-dim);
            border-radius: 1.3rem;
            padding: 2rem 1.6rem;
            text-align: center;
            transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
            position: relative;
            overflow: hidden;
        }"""

new_card = """        .contact-card {
            background: var(--card-bg);
            border: 1px solid var(--border-dim);
            border-radius: 1.3rem;
            padding: 2rem 1.6rem;
            text-align: center;
            transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }"""

content = content.replace(old_card, new_card)

old_a = """        .contact-card a {
            color: var(--accent);
            font-weight: 700;
            font-size: 0.9rem;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: gap 0.2s ease;
        }"""

new_a = """        .contact-card a {
            color: var(--accent);
            font-weight: 700;
            font-size: 0.9rem;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: gap 0.2s ease;
            margin-top: auto;
            justify-content: center;
        }"""

content = content.replace(old_a, new_a)

with open('contact.html', 'w') as f:
    f.write(content)
