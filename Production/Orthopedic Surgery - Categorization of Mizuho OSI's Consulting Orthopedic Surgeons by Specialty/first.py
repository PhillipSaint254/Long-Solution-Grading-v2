def get_names_specialties():
    return {
        'Dr. Andrew Wickline': 'Joint Replacement (Hip/Knee)',
        'Dr. Joel Matta': 'Joint Replacement/Hip Disorders',
        'John C. Wilson Jr.': 'Sports Medicine / Hip (Motion and Sports Analysis)',
        'Brett Babat, MD': 'Spine Surgery',
        'Christopher Martin, MD': 'Spine Surgery',
        'Kristen Jones, MD': 'Spine Surgery',
        'Dr. Jonathan Yerasimides': 'Joint Replacement/Hip Reconstruction',
        'Dr. E. Trent Andrews': 'Spine Surgery',
        'Dr. Charles DeCook': 'Joint Replacement (Hip/Knee)'
    }

if __name__ == "__main__":
    names_specialties = get_names_specialties()
    from collections import Counter
    print(Counter([cat.split()[0] for cat in names_specialties.values()]))
