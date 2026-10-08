import re

with open('index.html', 'r') as f:
    index_lines = f.readlines()

with open('home-2.html', 'r') as f:
    home_lines = f.readlines()

for i in range(len(home_lines)):
    line = home_lines[i]
    if 'color: #FFFFFF;' in line or 'border-color: #FFFFFF;' in line or 'background-color: #FFFFFF;' in line:
        # Find matching line in index.html (ignoring the color part)
        clean_home = re.sub(r'#FFFFFF', '___', line.strip())
        for j in range(max(0, i-500), min(len(index_lines), i+500)):
            clean_idx = re.sub(r'var\(--accent\)', '___', index_lines[j].strip())
            if clean_home == clean_idx and 'var(--accent)' in index_lines[j]:
                home_lines[i] = index_lines[j]
                print(f"Fixed line {i}: {home_lines[i].strip()}")
                break

with open('home-2.html', 'w') as f:
    f.writelines(home_lines)
