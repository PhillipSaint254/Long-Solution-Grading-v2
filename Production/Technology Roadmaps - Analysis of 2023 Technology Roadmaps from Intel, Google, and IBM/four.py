# We'll define the three sections for Document 1 (Intel) and list the items.

def get_doc1_sections():
    return {
        'Upstream Scope 3': [
            'Collective action on industry-wide emissions reductions via Semiconductor Climate Consortium and supplier engagement',
            'Request suppliers set 100% renewable electricity and net-zero targets with supporting roadmaps',
            'Implement spent chemical reuse',
            'Activate Catalyze Program to support supplier renewable electricity use'
        ],
        'Scope 1 and 2 (Operations)': [
            'Energy conservation projects',
            'Build facilities to U.S. Green Building Council LEED® standards',
            'Collaborate on development of new abatement technologies',
            'Install new abatement technologies at new factories',
            'Reduce process chemistry use through tool optimization',
            'Identify and implement process chemistry alternatives',
            'Install electric facilities equipment',
            'Reconfigure facility systems',
            'Electrify on-site and leased vehicle fleets',
            'Implement process chemistry alternatives',
            'Retrofit natural gas burning equipment',
            'Investigate implementation of renewable natural gas'
        ],
        'Downstream Scope 3': [
            'Reduce carbon footprint of platform reference designs for client form factors',
            'Meet annual milestones for server and client microprocessor energy efficiency',
            'Offer smart grid technologies to enable grid renewable electricity',
            'Enable more grid renewable electricity'
        ]
    }

if __name__ == "__main__":
    # Now compute number of items per section and average.
    import statistics

    doc1_sections = get_doc1_sections()

    counts1 = {sec: len(items) for sec, items in doc1_sections.items()}
    avg1 = statistics.mean(counts1.values())

    print(counts1, avg1)
