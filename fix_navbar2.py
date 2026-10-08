import re

with open('rituals.html', 'r') as f:
    content = f.read()

# Replace all occurrences of color: #FFFFFF; with color: #0A0A0A; ONLY WHERE IT WAS MESSED UP
# Actually, since I did a global replace of color: #0A0A0A; to color: #FFFFFF;, I might have ruined a lot.
# Let's see what contact.html has.
with open('contact.html', 'r') as f:
    contact_content = f.read()
    
# Let's extract the <style> block from rituals.html
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
rituals_style = style_match.group(1)

# Now, we know rituals.html is supposed to be exactly like contact.html for the navbar and buttons
# EXCEPT that the default theme is light, and the [data-theme="dark"] is dark.
# So any color: #0A0A0A; in contact (default dark) should be color: #FFFFFF; in rituals (default light).
# Oh wait! In contact.html (default dark), `color: #0A0A0A;` means text on orange is BLACK.
# In contact.html `[data-theme="light"]`, text on orange is WHITE!
# So in rituals.html (default light), text on orange SHOULD BE WHITE!
# And in rituals.html `[data-theme="dark"]`, text on orange SHOULD BE BLACK!
# So my global replacement `color: #FFFFFF;` was actually CORRECT for the default rules!
# But for `[data-theme="dark"]`, they should all be `#0A0A0A;`.
# Let's fix the `[data-theme="dark"]` rules in rituals.html.
