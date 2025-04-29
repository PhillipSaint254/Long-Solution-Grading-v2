import pandas as pd
from first import GetPercentage

def get_data():
    return [
        ('Snapchat My AI Chatbot', 150_000_000),
        ('Microsoft Bing Chat', 100_000_000),
        ('Duolingo (with ChatGPT features)', 74_100_000),
        ('OpenAI API Developers', 2_000_000),
        ('Khan Academy Khanmigo', 500_000),
    ]

def get_rows():
    total_users = GetPercentage().get_total_chatgpt_users()
    data = get_data()
    rows = []
    for name, count in data:
        percent = round(count / total_users * 100, 1)
        rows.append((name, count, percent))
    return rows

if __name__ == "__main__":
    print(get_rows())
