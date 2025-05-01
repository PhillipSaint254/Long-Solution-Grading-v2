from fourteen import get_specific_freq

def get_summary_by_disease():
    specific_freq = get_specific_freq()
    return specific_freq.reset_index()

if __name__ == "__main__":
    summary_by_disease = get_summary_by_disease()
    print(summary_by_disease)
