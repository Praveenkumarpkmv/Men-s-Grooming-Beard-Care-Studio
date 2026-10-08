import re

with open('grooming.html', 'r') as f:
    content = f.read()

# Fix process-card to be flex column
old_card = """        .process-card {
            flex: 0 0 320px;
            scroll-snap-align: start;
            background: var(--card-bg);
            border: 1px solid var(--border-dim);
            border-radius: 1.3rem;
            padding: 2rem 1.6rem 1.6rem;
            position: relative;
            transition: transform 0.35s ease, border-color 0.3s ease, box-shadow 0.35s ease;
            overflow: hidden;
        }"""

new_card = """        .process-card {
            flex: 0 0 320px;
            scroll-snap-align: start;
            background: var(--card-bg);
            border: 1px solid var(--border-dim);
            border-radius: 1.3rem;
            padding: 2rem 1.6rem 1.6rem;
            position: relative;
            transition: transform 0.35s ease, border-color 0.3s ease, box-shadow 0.35s ease;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }"""

content = content.replace(old_card, new_card)

# Fix process-time to stick to bottom and align left
old_time = """        .process-time {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            margin-top: 1.2rem;
            font-size: 0.72rem;
            color: var(--accent);
            font-weight: 700;
            letter-spacing: 0.05em;
            padding: 0.3rem 0.75rem;
            border-radius: 40px;
            background: rgba(200,122,59,0.15);
            border: 1px solid rgba(200,122,59,0.3);
        }"""

new_time = """        .process-time {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            margin-top: auto;
            align-self: flex-start;
            font-size: 0.72rem;
            color: var(--accent);
            font-weight: 700;
            letter-spacing: 0.05em;
            padding: 0.3rem 0.75rem;
            border-radius: 40px;
            background: rgba(200,122,59,0.15);
            border: 1px solid rgba(200,122,59,0.3);
        }"""

content = content.replace(old_time, new_time)

with open('grooming.html', 'w') as f:
    f.write(content)
