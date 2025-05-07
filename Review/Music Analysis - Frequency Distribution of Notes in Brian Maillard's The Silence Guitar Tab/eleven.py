from ten import parse_boxes
from nine import get_boxes_str
from sklearn.cluster import KMeans

df_boxes = parse_boxes(get_boxes_str())
y = df_boxes['center_y'].values.reshape(-1,1)
kmeans = KMeans(n_clusters=6, random_state=0).fit(y)
df_boxes['string_cluster'] = kmeans.labels_
print(df_boxes[['char','center_y','string_cluster']].head())
