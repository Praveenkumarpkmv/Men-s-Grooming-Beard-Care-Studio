import re

with open('home-2.html', 'r') as f:
    content = f.read()

replacements = {
    '[data-theme="light"] .reserve-card.accent { color: var(--accent); }': '[data-theme="light"] .reserve-card.accent { color: #FFFFFF; }',
    '[data-theme="light"] .reserve-card.accent p { color: var(--accent); }': '[data-theme="light"] .reserve-card.accent p { color: #FFFFFF; }',
    '[data-theme="light"] .reserve-card.accent h3,': '[data-theme="light"] .reserve-card.accent h3,',
    '[data-theme="light"] .reserve-card.accent .reserve-card-icon { color: var(--accent); border-color: rgba(255,255,255,0.3); }': '[data-theme="light"] .reserve-card.accent .reserve-card-icon { color: #FFFFFF; border-color: rgba(255,255,255,0.3); }',
    '[data-theme="light"] .reserve-card.accent .reserve-card-foot { color: var(--accent); }': '[data-theme="light"] .reserve-card.accent .reserve-card-foot { color: #FFFFFF; }'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('home-2.html', 'w') as f:
    f.write(content)
