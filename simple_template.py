#!/usr/bin/env python3
"""Simplest approach - minimal changes to HTML"""

# Read the original HTML
with open('Zuriwave/tsg.xyz/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Only replace branding text, don't touch any paths
replacements = [
    ('The Stack Group', 'Zuriwave'),
    ('THE STACK GROUP', 'ZURIWAVE'),
    ('TSG is the parent company of Paystack', 'Zuriwave is building the future of African fintech'),
    (' TSG ', ' Zuriwave '),
    ('tsg.xyz', 'zuriwave.com'),
    ('hello@tsg.xyz', 'hello@zuriwave.com'),
]

for old, new in replacements:
    html = html.replace(old, new)

# Write without Django template tags - just serve as static
with open('core/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Template created - keeping all original paths")
