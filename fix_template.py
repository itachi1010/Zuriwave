#!/usr/bin/env python3
"""Fix the Django template - better conversion"""

import re

# Read the original HTML from HTTrack
with open('Zuriwave/tsg.xyz/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Django template tags at the beginning
django_header = "{% load static %}\n"

# Replace TSG branding with Zuriwave FIRST (before modifying paths)
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

# Fix CSS file references - be more specific
html = re.sub(r'href="_nuxt/([^"]+\.css)"', r'href="{% static \'css/\1\' %}"', html)

# Fix JS file references - be more specific
html = re.sub(r'src="_nuxt/([^"]+\.js)"', r'src="{% static \'css/\1\' %}"', html)

# Fix image paths
html = re.sub(r'src="images/([^"]+)"', r'src="{% static \'images/\1\' %}"', html)

# Fix video paths
html = re.sub(r'src="videos/([^"]+)"', r'src="{% static \'videos/\1\' %}"', html)

# Write the Django template
output = django_header + html

with open('core/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print("Template fixed successfully!")
print("All static paths properly formatted")
