from collections import Counter
import re, statistics

# Define Document 3 sections and list items.
def get_doc3_sections():
    return {
        'Regulatory milestones': [
            'NIST selects algorithms for standardization',
            'Federal agencies plan for PQC adoption',
            'NIST publishes PQC standards',
            'CNSA 2.0: preference to PQC-compliant vendors',
            'Vendors complete transition to PQC',
            'Payments (EPAA, NACHA)'
        ],
        'Consortia': [
            'PQC Alliance (Linux Foundation)',
            'Open Quantum Safe (OQS)',
            'Post-Quantum Telco Network',
            'NCCoE',
            'PQC Coalition (MITRE)',
            'Critical Infrastructure Protection Coalition'
        ],
        'IBM services': [
            'Quantum-safe preparation & advisory',
            'Application modernization',
            'Security Platform modernization',
            'Quantum-safe talent transformation'
        ],
        'Algorithms / Protocols / Standards / Libraries': [
            'Key encryption: CRYSTALS-Kyber',
            'Digital signature: CRYSTALS-Dilithium',
            'Digital signature: FALCON',
            'Cryptography Bill of Materials (CBOM)',
            'MAYO',
            'UOV',
            'SQISign'
        ],
        'IBM infrastructure': [
            'IBM z16, IBM Hyper Protect Crypto Services, IBM Tape Storage, Hardware Security Modules (HSM)',
            'IBM Cloud, IBM Software, Red Hat, IBM Storage, IBM Power : Strategy & Planning'
        ],
        'IBM Quantum Safe technology': [
            'Adaptive Proxy',
            'Performance benchmarking',
            'TLS, VPN, SSH',
            'Encryption/key/certificate management',
            'Crypto-agility framework',
            'Automated remediation',
            'LLM-based recommendation',
            'IBM Quantum Safe Remediator',
            'Risk-based prioritization',
            'Enriched metadata',
            'AI-driven risk analysis',
            'IBM Guardium Quantum Safe',
            'Static scan',
            'CBOM generation',
            'CI/CD integration',
            'Custom library support',
            'Remediation recommendation',
            'LLM-assisted scanning',
            'IBM Quantum Safe Explorer',
            'IBM Cloud, IBM Software, Red Hat, IBM Storage, IBM Power : Phase-1',
            'IBM Cloud, IBM Software, Red Hat, IBM Storage, IBM Power : Phase-2',
            'OpenSSL',
            'Dynamic Inventory',
            'Cryptography Posture Management',
            'Cryptography Policy Management',
            'Healthcare Coalition',
            'Quantum-safe transformation services'
        ]
    }

if __name__ == "__main__":
    doc3_sections = get_doc3_sections()
    # Now count per section and average.
    counts3 = {sec: len(items) for sec, items in doc3_sections.items()}
    avg3 = statistics.mean(counts3.values())
    print(counts3, avg3)
