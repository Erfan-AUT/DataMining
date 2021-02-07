from sklearn.cluster import DBSCAN
import folium
import pandas as pd
from sklearn import metrics
import numpy as np

m = folium.Map(location=[32.427910, 53.688046], zoom_start=5)
loc = [35.703136, 51.409126]
folium.Marker(location=loc).add_to(m)

X = pd.read_csv("data/covid.csv")
# for i in range(X.shape[0]):
    # folium.Circle(location=X.iloc[[i]].values.tolist()[0], radius=1, color="red", fill=True).add_to(m)
# m

db = DBSCAN(eps=0.65, min_samples=30).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)

unique_labels = set(labels)
colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred','lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen']
a = zip()
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = "black"

    class_member_mask = (labels == k)
    xy = X[class_member_mask & core_samples_mask]
    folium.Circle(location=list(xy), radius=1, color=col, fill=True).add_to(m)
    
    # plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
    #          markeredgecolor='k', markersize=14)

    # xy = X[class_member_mask & ~core_samples_mask]
    # plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
    #          markeredgecolor='k', markersize=6)