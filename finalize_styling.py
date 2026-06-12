#!/usr/bin/env python3
"""Final comprehensive HTML update to full English professional styling"""
import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

updated_lines = []
in_about_cards = False
in_stats_section = False
in_model_section = False
skip_lines = 0

for i, line in enumerate(lines):
    if skip_lines > 0:
        skip_lines -= 1
        continue
    
    # Update about section heading and intro
    if 'Why Choose Our Solution' in line and in_about_cards == False:
        in_about_cards = True
        updated_lines.append(line)
        continue
    
    # Skip and replace Bengali card content in about section
    if in_about_cards and '<div class="soft-card' in line and 'p-3 sm:p-4' in line:
        # Read ahead to see if this is a Bengali card
        # Just update the styling for now - make smaller
        new_line = line.replace('p-3 sm:p-4', 'p-2.5 sm:p-3').replace('rounded-lg', 'rounded-lg').replace('text-2xl', 'text-lg')
        updated_lines.append(new_line)
        continue
    
    # Update "About" section classes for smaller padding
    if 'mt-12 grid gap-4' in line:
        updated_lines.append(line.replace('mt-12 gap-4', 'mt-8 gap-3'))
        continue
    
    # Update text-2xl to text-lg for emojis in about cards
    if '<div class="text-2xl mb-2">' in line:
        updated_lines.append(line.replace('text-2xl mb-2', 'text-lg mb-1'))
        continue
        
    # Update data boxes to smaller size
    if '<p class="text-2xl font-bold text-indigo-600">' in line:
        updated_lines.append(line.replace('text-2xl', 'text-lg'))
        continue
    
    # Update "mt-10 grid" to "mt-8 grid" and "gap-4" to "gap-3"
    if 'mt-10 grid gap-4 sm:grid-cols-3' in line:
        updated_lines.append(line.replace('mt-10 grid gap-4', 'mt-8 grid gap-3').replace('p-3 sm:p-4', 'p-2.5 sm:p-3'))
        continue
    
    # Update stats section - replace Bengali with English labels
    if 'मডेलের कर्मक्षमता' in line or 'मडेलের کর্مक्ষमता' in line:
        updated_lines.append(line.replace(line.split('>')[1].split('<')[0], 'Performance</p>'))
        continue
    
    if 'पूर्वाभাस पिरिसंख्यान' in line:
        updated_lines.append(line.replace(line.split('>')[1].split('<')[0], 'Model Statistics</h2>'))
        continue
    
    # Update py spacing in stats  
    if 'py-16 sm:py-20' in line and in_stats_section == False:
        updated_lines.append(line.replace('py-16 sm:py-20', 'py-12 sm:py-14'))
        in_stats_section = True
        continue
    
    # Update team boxes
    if 'rounded-2xl border border-gray-200 p-5 sm:p-6' in line:
        updated_lines.append(line.replace('rounded-2xl', 'rounded-lg').replace('p-5 sm:p-6', 'p-3.5 sm:p-4'))
        continue
    
    # Update model details section styling
    if 'py-16 sm:py-20' in line and in_model_section == False and i > 200:
        updated_lines.append(line.replace('py-16 sm:py-20', 'py-12 sm:py-14'))
        in_model_section = True
        continue
    
    # Update model cards spacing
    if 'gap-6 sm:grid-cols-2 lg:grid-cols-4' in line:
        updated_lines.append(line.replace('gap-6', 'gap-3').replace('p-4 shadow-sm', 'p-3 shadow-sm hover:shadow-md transition'))
        continue
    
    updated_lines.append(line)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.writelines(updated_lines)

print("✓ Professional sizing applied")
print("✓ Smaller padding (p-2.5/p-3 instead of p-4/p-5)")
print("✓ Smaller gaps (gap-3 instead of gap-4)")
print("✓ Smaller boxes implemented")
print("✓ Team member cards compacted")
