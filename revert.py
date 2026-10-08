import re

with open('home-2.html', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    # Skip lines 15-40 which are the :root and [data-theme="light"] variable definitions
    if 10 <= i <= 50:
        new_lines.append(line)
        continue
    
    # Otherwise replace color: #FFFFFF; with color: var(--accent);
    if 'color: #FFFFFF;' in line:
        line = line.replace('color: #FFFFFF;', 'color: var(--accent);')
    # and border-color: #FFFFFF; with border-color: var(--accent); (if I did that too)
    if 'border-color: #FFFFFF;' in line:
        line = line.replace('border-color: #FFFFFF;', 'border-color: var(--accent);')
    
    new_lines.append(line)

with open('home-2.html', 'w') as f:
    f.writelines(new_lines)
