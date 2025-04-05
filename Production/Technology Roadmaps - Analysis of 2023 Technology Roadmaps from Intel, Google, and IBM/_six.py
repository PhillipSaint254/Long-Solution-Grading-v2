import statistics

# Define Document 2 Google sections and list items.
def get_doc2_sections():
    return {
        'Net-zero carbon': [
            # Reducing carbon emissions:
            'Energy-efficient and low-carbon facilities',
            'Electrification',
            'Sustainable travel and commuting',
            'Supplier engagement',
            # Advancing carbon-free energy:
            'Purchasing carbon-free energy',
            'Accelerating new and improved technologies',
            'Transforming the energy system through partnerships and advocacy'
        ],
        'Water stewardship': [
            'Advance responsible water use',
            'Benefit watersheds and communities (collaborate to replenish and improve watershed health)',
            'Support water security with technology'
        ],
        'Circular economy': [
            'Design out waste and pollution',
            'Keep materials in use as long as safely possible',
            'Promote safe and healthy materials'
        ],
        'Nature and biodiversity': [
            'Build for biodiversity (designing for ecology and bringing nature back to cities)',
            'Protect nature and make it more accessible',
            'Source responsibly across supply chain',
            'Develop technology to address biodiversity loss'
        ]
    }

if __name__ == "__main__":
    doc2_sections = get_doc2_sections()
    counts2 = {sec: len(items) for sec, items in doc2_sections.items()}
    avg2 = statistics.mean(counts2.values())
    print(counts2, avg2)
