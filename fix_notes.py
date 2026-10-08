import re

with open('rituals.html', 'r') as f:
    content = f.read()

old_note = """        .note {
            background: var(--paper);
            border: 1px solid var(--line);
            border-radius: 1rem;
            padding: 1.6rem 1.4rem 1.4rem;
            position: relative;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }"""

new_note = """        .note {
            background: var(--paper);
            border: 1px solid var(--line);
            border-radius: 1rem;
            padding: 1.6rem 1.4rem 1.4rem;
            position: relative;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            display: flex;
            flex-direction: column;
        }"""

content = content.replace(old_note, new_note)

old_quote = """        .note-quote {
            font-family: var(--heading-font);
            font-size: 1.02rem;
            font-style: italic;
            color: var(--ink);
            line-height: 1.55;
            margin-bottom: 1.2rem;
            padding-bottom: 1.2rem;
            border-bottom: 1px dashed var(--line);
        }"""

new_quote = """        .note-quote {
            font-family: var(--heading-font);
            font-size: 1.02rem;
            font-style: italic;
            color: var(--ink);
            line-height: 1.55;
            margin-bottom: 1.2rem;
            padding-bottom: 1.2rem;
            border-bottom: 1px dashed var(--line);
            flex-grow: 1;
        }"""

content = content.replace(old_quote, new_quote)

with open('rituals.html', 'w') as f:
    f.write(content)
