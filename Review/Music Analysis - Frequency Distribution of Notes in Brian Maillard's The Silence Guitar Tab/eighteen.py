from seventeen import get_df_boxes
import numpy as np, pandas as pd

def group_digits_to_numbers(df_string, threshold=20):
    # df_string: DataFrame for digits in one string, sorted by x
    numbers = []
    current_digits = []
    prev_x = None
    for _, row in df_string.sort_values('center_x').iterrows():
        if prev_x is None or row['x1'] - prev_x > threshold:
            # start new number
            if current_digits:
                number = ''.join(current_digits)
                numbers.append(number)
                current_digits = []
        current_digits.append(row['char'])
        prev_x = row['x2']  # using right boundary as prev
    # append last number
    if current_digits:
        number = ''.join(current_digits)
        numbers.append(number)
    return numbers

# Example for string 1
def get_numbers_s1():
    df_boxes = get_df_boxes()
    return group_digits_to_numbers(df_boxes[df_boxes['string_num']==1])

if __name__ == "__main__":
    print(get_numbers_s1()[:20])
