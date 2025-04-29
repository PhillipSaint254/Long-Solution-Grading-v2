from second import get_sorted_counts
from first import GetPercentage

def get_sorted_percentages():
    total_chatgpt_users = GetPercentage().get_total_chatgpt_users()
    sorted_counts = get_sorted_counts()
    return [(name, count, count/total_chatgpt_users*100) for name,count in sorted_counts]

if __name__ == "__main__":
    print(get_sorted_percentages())
