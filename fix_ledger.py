import re

with open('rituals.html', 'r') as f:
    content = f.read()

old_row = """        .ledger-row {
            display: grid;
            grid-template-columns: 60px 1fr auto auto;
            gap: 1.5rem;
            align-items: center;
            padding: 1.4rem 0;
            border-bottom: 1px dashed var(--line);
            transition: background 0.25s ease;
        }"""

new_row = """        .ledger-row {
            display: grid;
            grid-template-columns: 60px 1fr 65px 115px;
            gap: 1.5rem;
            align-items: center;
            padding: 1.4rem 0;
            border-bottom: 1px dashed var(--line);
            transition: background 0.25s ease;
        }"""

content = content.replace(old_row, new_row)

old_use = """        .ledger-use {
            font-family: 'Inter', sans-serif;
            font-size: 0.62rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            font-weight: 800;
            padding: 0.3rem 0.7rem;
            border-radius: 40px;
            background: var(--wax);
            color: var(--ink);
            text-align: center;
        }"""

new_use = """        .ledger-use {
            font-family: 'Inter', sans-serif;
            font-size: 0.62rem;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            font-weight: 800;
            padding: 0.3rem 0.7rem;
            border-radius: 40px;
            background: var(--wax);
            color: var(--ink);
            text-align: center;
            justify-self: start;
        }"""

content = content.replace(old_use, new_use)

with open('rituals.html', 'w') as f:
    f.write(content)
