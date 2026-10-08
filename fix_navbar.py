import re

with open('rituals.html', 'r') as f:
    content = f.read()

# Fix navbar bg back to white
content = content.replace('--navbar-bg: rgba(246, 239, 228, 0.9);', '--navbar-bg: rgba(255, 255, 255, 0.9);')
content = content.replace('--navbar-bg: rgba(23, 19, 15, 0.85);', '--navbar-bg: rgba(17, 17, 17, 0.85);')

# Fix logo-mark icon colors to match other pages precisely
# Other pages: dark (default) = #0A0A0A, light = #FFFFFF
# Rituals: light (default) = #FFFFFF, dark = #0A0A0A
# We already messed up the sed for #0A0A0A, let's restore contact.html's CSS for those components
