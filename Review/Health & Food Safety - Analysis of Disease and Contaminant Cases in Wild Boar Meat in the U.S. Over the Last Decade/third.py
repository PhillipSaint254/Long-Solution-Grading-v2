def get_event_data():
    return [
        {"year": 2014, "disease_or_contaminant": "Undeclared soy allergen","type":"contaminant", "human_case_num":0},
        {"year": 2016, "disease_or_contaminant": "Excess nitrite", "type":"contaminant","human_case_num":0},
        {"year": 2017, "disease_or_contaminant": "Trichinella", "type":"disease","human_case_num":12},
        {"year": 2025, "disease_or_contaminant": "Brucella", "type":"disease","human_case_num":1}
    ]

if __name__ == "__main__":
    print(get_event_data())
