import re

with open('home-2.html', 'r') as f:
    content = f.read()

# Fix buttons to have white text in light mode (since the button is orange)
replacements = {
    '[data-theme="light"] .logo-mark i { color: var(--accent); }': '[data-theme="light"] .logo-mark i { color: #FFFFFF; }',
    '[data-theme="light"] .cta-btn { color: var(--accent); }': '[data-theme="light"] .cta-btn { color: #FFFFFF; }',
    '[data-theme="light"] .mobile-action-btn.primary { color: var(--accent); }': '[data-theme="light"] .mobile-action-btn.primary { color: #FFFFFF; }',
    '[data-theme="light"] .mobile-action-btn.primary:hover { color: var(--accent); }': '[data-theme="light"] .mobile-action-btn.primary:hover { color: #FFFFFF; }',
    '[data-theme="light"] .btn-primary { color: var(--accent); }': '[data-theme="light"] .btn-primary { color: #FFFFFF; }',
    '[data-theme="light"] .btn-primary:hover { color: var(--accent); }': '[data-theme="light"] .btn-primary:hover { color: #FFFFFF; }',
    '[data-theme="light"] .footer-btn { color: var(--accent); }': '[data-theme="light"] .footer-btn { color: #FFFFFF; }',
    '[data-theme="light"] .footer-btn:hover { color: var(--accent); }': '[data-theme="light"] .footer-btn:hover { color: #FFFFFF; }',
    '[data-theme="light"] #scroll-top { color: var(--accent); }': '[data-theme="light"] #scroll-top { color: #FFFFFF; }',
    '[data-theme="light"] #scroll-top:hover { color: var(--accent); }': '[data-theme="light"] #scroll-top:hover { color: #FFFFFF; }',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('home-2.html', 'w') as f:
    f.write(content)
