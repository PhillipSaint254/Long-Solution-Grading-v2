from thirteen import get_df_boxes as gdfb
from sixteen import get_string_map

def get_df_boxes():
    df_boxes = gdfb()
    string_map = get_string_map()
    df_boxes['string_num'] = df_boxes['string_cluster'].map(string_map)
    return df_boxes

if __name__ == "__main__":
    print(get_df_boxes().head())

