from eighteen import group_digits_to_numbers, get_df_boxes

# Compute numbers for each string
def get_string_numbers():
    string_numbers = {}
    df_boxes = get_df_boxes()
    for s in range(1,7):  # 1..6
        digits = group_digits_to_numbers(df_boxes[df_boxes['string_num']==s], threshold=25)
        string_numbers[s] = digits
    return string_numbers

if __name__ == "__main__":
    print(get_string_numbers())
