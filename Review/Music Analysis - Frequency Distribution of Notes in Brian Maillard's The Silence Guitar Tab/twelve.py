from ten import parse_boxes, get_boxes_str

df_boxes = parse_boxes(get_boxes_str())
print(df_boxes['center_y'].min(), df_boxes['center_y'].max())
