from first import get_names_specialties

def get_categories():
    return ['Joint Replacement', 'Spine Surgery', 'Sports Medicine']

def get_count():
    counts = {}
    names_specialties = get_names_specialties()
    for name, spec in names_specialties.items():
        if 'Spine' in spec:
            cat='Spine Surgery'
        elif 'Sports' in spec:
            cat='Sports Medicine'
        else:
            cat='Joint Replacement'
        counts[cat]=counts.get(cat, 0)+1
    return counts

if __name__ == "__main__":
    print(get_count())
