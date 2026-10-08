import re

with open('contact.html', 'r') as f:
    content = f.read()

old_css = "        .form-group.full { grid-column: 1 / -1; }"

new_css = """        .form-group.full { grid-column: 1 / -1; }
        input[type="date"]::-webkit-calendar-picker-indicator { filter: invert(1); cursor: pointer; opacity: 0.7; }
        input[type="date"]::-webkit-calendar-picker-indicator:hover { opacity: 1; }
        [data-theme="light"] input[type="date"]::-webkit-calendar-picker-indicator { filter: none; }"""

content = content.replace(old_css, new_css)

with open('contact.html', 'w') as f:
    f.write(content)
