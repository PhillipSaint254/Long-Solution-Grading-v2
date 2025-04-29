from first import GetPercentage

def get_integration_counts():
    data = GetPercentage()
    snap_users = data.get_snap_users()
    bing_users = data.get_bing_users()
    duolingo_users = data.get_duolingo_users()  # 74.1 million
    api_developers = data.get_api_developers()
    khanmigo_users = data.get_khanmigo_users()  # half a million
    return [
        ('Snapchat My AI Chatbot', snap_users),
        ('Microsoft Bing Chat', bing_users),
        ('Duolingo (Duolingo Max features with ChatGPT)', duolingo_users),
        ('OpenAI API developers building on ChatGPT', api_developers),
        ('Khan Academy Khanmigo AI tutor', khanmigo_users),
    ]

def get_sorted_counts():
    integration_counts = get_integration_counts()
    return sorted(integration_counts, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    print(get_sorted_counts())
