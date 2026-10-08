import re

with open('home-2.html', 'r') as f:
    content = f.read()

# Using regex to target the color specifically within .reel-card-tag
pattern = r"(\.reel-card-tag \{[^}]*)color:\s*var\(--accent\);"
replacement = r"\1color: #FFFFFF;"

new_content = re.sub(pattern, replacement, content)

with open('home-2.html', 'w') as f:
    f.write(new_content)
