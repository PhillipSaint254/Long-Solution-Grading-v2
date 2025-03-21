# We'll build a list of dictionaries with entries for each company
companies = [
    {
        'name': 'Drip Hydration',
        'treatments': [
            ('Hangover IV (nausea, headache relief)', '$299'),
            ('Dehydration IV (rehydration)', '$249')
        ]
    },
    {
        'name': 'Mobile IV Nurses',
        'treatments': [
            ('Purely Saline (hydration)', '$110'),
            ("Myers' Cocktail (vitamins, for hangovers etc.)", '$225 (often $205)')
        ]
    },
    {
        'name': 'Hydreight (mobile IV therapy via WEL Palm Beach)',
        'treatments': [
            ('Various IV drips (e.g. hangover, dehydration, migraine)', '$179–$299')
        ]
    },
    {
        'name': 'IV Revival (mobile IV therapy)',
        'treatments': [
            ('Basic Rehydration (fluids)', '$125'),
            ('Hangover Helper (hangover relief)', '$200'),
            ('Myers Cocktail (vitamin infusion)', '$195')
        ]
    },
    {
        'name': 'Revive Mobile IV',
        'treatments': [
            ('Saline (hydration)', '$115'),
            ('The After Party (hangover relief)', '$225'),
            ('The Myers (vitamin infusion)', '$200')
        ]
    }
]

# Now generate a Markdown table: columns: Company, Treatments (with cost).
# For those with multiple treatments, we can display them in separate lines within a cell.

from textwrap import indent

# Construct table
lines = []
lines.append("| Company | Cost of service / treatments | Types of treatments offered |")
lines.append("|---------|------------------------------|------------------------------|")

for c in companies:
    # join treatments costs
    # We will put cost per treatment and description
    tre_lines = []
    descr_lines = []
    for tre, cost in c['treatments']:
        tre_lines.append(f"{tre}: {cost}")
        # Types is somewhat redundant because we include the descriptions
    # For the third company we can mention "Various IV drips" and list the examples already included
    # Actually we need a third column "Types" maybe we just restate the treatments?
    # But we already have types in the second column? We wrote the description and cost together.
    # Let's write in third column a list of categories: e.g., "Hangover relief, hydration, vitamin infusion" for each
    # We can glean them from the treatments. Perhaps we can derive from tre_lines, but we can manually list them.
    
    # We'll set a mapping for the third column
    if c['name'].startswith('Drip Hydration'):
        types = "Hangover relief, hydration"
    elif c['name'].startswith('Mobile IV'):
        types = "Hydration, vitamin infusion (including hangover support)"
    elif c['name'].startswith('Hydreight'):
        types = "Wide range (hangover, dehydration, migraine, etc.)"
    elif c['name'].startswith('IV Revival'):
        types = "Hydration, hangover relief, vitamin infusions"
    elif c['name'].startswith('Revive'):
        types = "Hydration, hangover relief, vitamin infusions"
    else:
        types = ""
    
    lines.append(f"| {c['name']} | " +
                 "<br>".join(tre_lines) + " | " +
                 types + " |")
    
# Output
print("\n".join(lines))

