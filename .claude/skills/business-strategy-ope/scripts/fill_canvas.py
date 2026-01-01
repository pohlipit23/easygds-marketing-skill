#!/usr/bin/env python3
"""
Fill OPE Canvas Template

Usage:
    python fill_canvas.py input.json output.html

Input JSON format:
{
    "company_name": "...",
    "designed_by": "...",
    "date": "...",
    "obvious_choice": "...",
    "ideal_customer": "...",
    "core_problem": "...",
    "core_product": "...",
    "primary_channels": "...",
    "geography": "...",
    "moat_1": "...",
    "moat_2": "...",
    "moat_3": "...",
    "endgame": "...",
    "year_picture": "...",
    "quarterly_picture": "...",
    "monthly_picture": "...",
    "core_values": "...",
    "core_capabilities": "...",
    "strategic_choices": "..."
}
"""

import json
import sys
from pathlib import Path

def fill_template(template_path: str, data: dict) -> str:
    """Fill template with data."""
    with open(template_path, 'r') as f:
        html = f.read()
    
    replacements = {
        '{{COMPANY_NAME}}': data.get('company_name', ''),
        '{{DESIGNED_BY}}': data.get('designed_by', ''),
        '{{DATE}}': data.get('date', ''),
        '{{OBVIOUS_CHOICE}}': data.get('obvious_choice', ''),
        '{{IDEAL_CUSTOMER}}': data.get('ideal_customer', ''),
        '{{CORE_PROBLEM}}': data.get('core_problem', ''),
        '{{CORE_PRODUCT}}': data.get('core_product', ''),
        '{{PRIMARY_CHANNELS}}': data.get('primary_channels', ''),
        '{{GEOGRAPHY}}': data.get('geography', ''),
        '{{MOAT_1}}': data.get('moat_1', ''),
        '{{MOAT_2}}': data.get('moat_2', ''),
        '{{MOAT_3}}': data.get('moat_3', ''),
        '{{ENDGAME}}': data.get('endgame', ''),
        '{{YEAR_PICTURE}}': data.get('year_picture', ''),
        '{{QUARTERLY_PICTURE}}': data.get('quarterly_picture', ''),
        '{{MONTHLY_PICTURE}}': data.get('monthly_picture', ''),
        '{{CORE_VALUES}}': data.get('core_values', ''),
        '{{CORE_CAPABILITIES}}': data.get('core_capabilities', ''),
        '{{STRATEGIC_CHOICES}}': data.get('strategic_choices', ''),
    }
    
    for placeholder, value in replacements.items():
        # Convert lists to HTML if needed
        if isinstance(value, list):
            value = '<ul>' + ''.join(f'<li>{item}</li>' for item in value) + '</ul>'
        html = html.replace(placeholder, str(value))
    
    return html

def main():
    if len(sys.argv) < 3:
        print("Usage: python fill_canvas.py input.json output.html")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    
    # Find template
    script_dir = Path(__file__).parent.parent
    template_path = script_dir / 'assets' / 'ope-canvas-template.html'
    
    if not template_path.exists():
        # Try relative to current dir
        template_path = Path('assets/ope-canvas-template.html')
    
    if not template_path.exists():
        print(f"Template not found at {template_path}")
        sys.exit(1)
    
    with open(input_path, 'r') as f:
        data = json.load(f)
    
    html = fill_template(str(template_path), data)
    
    with open(output_path, 'w') as f:
        f.write(html)
    
    print(f"Canvas saved to {output_path}")

if __name__ == '__main__':
    main()
