import re

with open('beard-care.html', 'r') as f:
    content = f.read()

old_jar = """        .jar {
            background: var(--card-bg);
            border: 1px solid var(--border-dim);
            border-radius: 1.2rem;
            padding: 1.6rem 1.4rem 1.5rem;
            position: relative;
            overflow: hidden;
            transition: transform 0.35s ease, border-color 0.3s ease, box-shadow 0.35s ease;
        }"""

new_jar = """        .jar {
            background: var(--card-bg);
            border: 1px solid var(--border-dim);
            border-radius: 1.2rem;
            padding: 1.6rem 1.4rem 1.5rem;
            position: relative;
            overflow: hidden;
            transition: transform 0.35s ease, border-color 0.3s ease, box-shadow 0.35s ease;
            display: flex;
            flex-direction: column;
        }"""

content = content.replace(old_jar, new_jar)

old_foot = """        .jar-foot {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 0.9rem;
            border-top: 1px dashed var(--border-dim);
        }"""

new_foot = """        .jar-foot {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-top: 0.9rem;
            border-top: 1px dashed var(--border-dim);
            margin-top: auto;
        }"""

content = content.replace(old_foot, new_foot)

with open('beard-care.html', 'w') as f:
    f.write(content)
