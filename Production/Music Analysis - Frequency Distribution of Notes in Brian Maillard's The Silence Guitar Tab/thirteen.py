from sklearn.cluster import KMeans
import numpy as np, pandas as pd
from twelve import parse_boxes, get_boxes_str

df_boxes = parse_boxes(get_boxes_str())
y = df_boxes['center_y'].values.reshape(-1,1)
kmeans = KMeans(n_clusters=6, random_state=0).fit(y)
df_boxes['string_cluster'] = kmeans.labels_
df_boxes[['char','center_y','string_cluster']].head()
