def get_articles():
    return [
        ("2018-12-31", "International Cannabis Business Conference article about Thailand legalizing medical cannabis"),
        ("2019-09-03", "Understanding Cannabis Liberalization in Thailand - Tilleke"),
        ("2020-12-21", "Decriminalization of Narcotics Clarified by Thailand’s Ministry of Public Health - Tilleke"),
        ("2022-06-14", "Reuters article on Thailand legalising growing and consumption of marijuana"),
        ("2022", "Medical cannabis use in Thailand after its legalization: a respondent-driven sample survey (collection date 2022)"),
        ("2023-10-12", "Transnational Institute article 'Cannabis policy in Thailand – a way forward'")
    ]

from collections import defaultdict

def get_counts():
    articles = get_articles()
    counts = defaultdict(int)
    for date_str, _ in articles:
        year = date_str.split("-")[0]
        counts[year] += 1
    return counts

if __name__ == "__main__":
    print(get_counts())
