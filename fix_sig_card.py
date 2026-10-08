import re

with open('lookbook.html', 'r') as f:
    content = f.read()

old_card = """        .sig-card {
            background: var(--card-bg);
            border: 1px solid var(--border-dim);
            border-radius: 1.3rem;
            overflow: hidden;
            transition: transform 0.35s ease, border-color 0.3s ease, box-shadow 0.35s ease;
            position: relative;
        }"""

new_card = """        .sig-card {
            background: var(--card-bg);
            border: 1px solid var(--border-dim);
            border-radius: 1.3rem;
            overflow: hidden;
            transition: transform 0.35s ease, border-color 0.3s ease, box-shadow 0.35s ease;
            position: relative;
            display: flex;
            flex-direction: column;
        }"""
content = content.replace(old_card, new_card)

old_body = """        .sig-card-body {
            padding: 1.5rem 1.4rem 1.6rem;
        }"""

new_body = """        .sig-card-body {
            padding: 1.5rem 1.4rem 1.6rem;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }"""
content = content.replace(old_body, new_body)

old_foot = """        .sig-card-foot {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 0.9rem;
            border-top: 1px dashed var(--border-dim);
        }"""

new_foot = """        .sig-card-foot {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 0.9rem;
            border-top: 1px dashed var(--border-dim);
            margin-top: auto;
        }"""
content = content.replace(old_foot, new_foot)

with open('lookbook.html', 'w') as f:
    f.write(content)
