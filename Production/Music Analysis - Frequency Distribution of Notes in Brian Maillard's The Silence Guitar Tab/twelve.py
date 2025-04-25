import pandas as pd, numpy as np, re
from eleven import get_boxes_str

def parse_boxes(boxes_str):
    boxes = []
    for line in boxes_str.strip().split('\n'):
        parts = line.split()
        if len(parts) == 6:
            char, x1, y1, x2, y2, _ = parts
            if char.isdigit():  # Keep digits only
                x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
                boxes.append({
                    'char': char, 
                    'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
                    'center_x': (x1+x2)/2, 'center_y': (y1+y2)/2
                })
    return pd.DataFrame(boxes)

if __name__ == "__main__":
    df_boxes = parse_boxes(get_boxes_str())
    print(df_boxes.head(), len(df_boxes))
