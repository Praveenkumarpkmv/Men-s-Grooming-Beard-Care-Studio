import re

with open('home-2.html', 'r') as f:
    content = f.read()

# Add media query to fix mg-masthead-inner on mobile
old_css = """        @media (max-width: 900px) {
            .mg-hero-grid { grid-template-columns: 1fr; gap: 2rem; }
        }"""

new_css = """        @media (max-width: 900px) {
            .mg-hero-grid { grid-template-columns: 1fr; gap: 2rem; }
            .mg-masthead-inner {
                flex-direction: column;
                align-items: flex-start;
                gap: 0.6rem;
            }
            .mg-hero {
                padding-top: 14rem;
            }
        }"""

content = content.replace(old_css, new_css)

with open('home-2.html', 'w') as f:
    f.write(content)
