
def get_shows():
    return {
        "Arcane": 9.0,
        "Invincible": 8.6,
        "Stranger Things": 8.6,
        "Tron: Uprising": 8.2,
        "Voltron: Legendary Defender": 8.0,
        "Teen Titans": 7.9,
        "Ben 10: Ultimate Alien": 7.8,
        "Generator Rex": 7.6,
        "Smallville": 7.5,
        "The 100": 7.5
    }

if __name__ == "__main__":
    shows = get_shows()
    print(sorted(shows.items(), key=lambda x: x[1], reverse=True))
