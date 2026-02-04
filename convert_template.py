#!/usr/bin/env python3
"""Convert HTTrack HTML to Django template with Zuriwave branding"""

import re

# Read the original HTML
with open('Zuriwave/tsg.xyz/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Django template tags at the beginning
django_header = "{% load static %}\n"

# Replace CSS file paths
html = html.replace('href="_nuxt/', 'href="{% static \'css/')
html = html.replace('.css"', '.css\' %}"')

# Replace JS file paths
html = html.replace('src="_nuxt/', 'src="{% static \'css/')
html = html.replace('.js"', '.js\' %}"')

# Replace font paths in CSS
html = html.replace('url(PPMori-', 'url({% static \'fonts/PPMori-')
html = html.replace('.woff)', '.woff\' %})')

# Replace image paths
html = html.replace('src="images/', 'src="{% static \'images/')
html = html.replace('src="/images/', 'src="{% static \'images/')
html = re.sub(r'(src="{% static \'images/[^"]+)"', r"\1' %}", html)

# Replace video paths
html = html.replace('src="videos/', 'src="{% static \'videos/')
html = re.sub(r'(src="{% static \'videos/[^"]+)"', r"\1' %}", html)

# Replace TSG branding with Zuriwave
replacements = [
    ('The Stack Group', 'Zuriwave'),
    ('THE STACK GROUP', 'ZURIWAVE'),
    ('TSG is the parent company of Paystack', 'Zuriwave is building the future of African fintech'),
    ('TSG', 'Zuriwave'),
    ('tsg.xyz', 'zuriwave.com'),
    ('hello@tsg.xyz', 'hello@zuriwave.com'),
]

for old, new in replacements:
    html = html.replace(old, new)

# Write the Django template
output = django_header + html

with open('core/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("Template converted successfully!")
print("TSG branding replaced with Zuriwave")
print("Static file paths updated for Django")
print("Saved to core/templates/index.html")
