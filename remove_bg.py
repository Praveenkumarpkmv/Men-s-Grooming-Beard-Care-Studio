import re
import os

files = [
    "about.html", "beard-care.html", "blade-and-bone.html", 
    "grooming.html", "lookbook.html", "rituals.html", "contact.html"
]

def replace_background(content):
    # This will match the `background:` property in `.page-hero { ... }` up to the semicolon
    # We replace it with just the linear-gradient.
    
    # Let's find the .page-hero block
    block_pattern = r'(\.page-hero\s*\{[^}]*?background:\s*)(.*?)(;)'
    
    def repl(m):
        bg_val = m.group(2)
        # Remove any url(...)
        bg_val = re.sub(r',\s*url\([^\)]+\)\s*center/cover', '', bg_val)
        return m.group(1) + bg_val + m.group(3)
        
    content = re.sub(block_pattern, repl, content, flags=re.DOTALL)
    
    # Also for light theme
    light_pattern = r'(\[data-theme="light"\] \.page-hero\s*\{[^}]*?background:\s*)(.*?)(;)'
    content = re.sub(light_pattern, repl, content, flags=re.DOTALL)
    
    return content

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = replace_background(content)

    with open(file, "w", encoding="utf-8") as f:
        f.write(new_content)

print("Background images removed correctly.")
