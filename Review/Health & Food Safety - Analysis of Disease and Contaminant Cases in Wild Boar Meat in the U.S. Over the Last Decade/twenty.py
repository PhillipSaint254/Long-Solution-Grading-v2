from nineteen import get_final_table

def get_freq_table():
    final_table = get_final_table()
    return final_table.groupby("Disease or contaminant").agg(**{"Occurrences":("Year","count"), "Human cases":("Human cases","sum")})

if __name__ == "__main__":
    print(get_freq_table())
