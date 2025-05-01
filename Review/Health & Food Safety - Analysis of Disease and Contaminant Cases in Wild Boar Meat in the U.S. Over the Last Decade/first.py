def get_events():
    return [
        {"year": 2014, "disease_or_contaminant": "undeclared allergen (soy lecithin)", "type": "contaminant", "data_source": "USDA FSIS recall 2014", "details": "144,000 pounds recalled."},
        {"year": 2016, "disease_or_contaminant": "excess nitrite", "type": "contaminant", "data_source": "USDA FSIS recall 2016", "details": "4,692 pounds Wild Boar Brotwurst recalled."},
        {"year": 2017, "disease_or_contaminant": "Trichinella spiralis (trichinellosis)", "type": "disease", "data_source": "CDC MMWR 2018 article about 2017 outbreak", "details": "12 human cases."},
        {"year": 2025, "disease_or_contaminant": "Brucella suis (brucellosis)", "type": "disease", "data_source": "CDC EID article 2025 (case in Florida)", "details": "1 human case from feral swine meat exposure (published 2025)."}
    ]

if __name__ == "__main__":
    print(get_events())
