import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean

data_1 = pd.read_csv("data/Dataset1.csv").values.tolist()
data_2 = pd.read_csv("data/Dataset2.csv").values.tolist()

# plt.scatter(data_1["X"], data_1["Y"])
# plt.savefig("Dataset2.png")
# plt.clf()
# plt.scatter(data_2["X"], data_2["Y"])
# plt.savefig("Dataset2.png")

k = 3
max_loops = 15
k_means = []
cluster_pointers = {}
clusters = []
data_count = len(data_1)
for i in range(k):
    r = np.random.randint(0, data_count)
    mean = data_1[r]
    k_means.append(mean)
    cluster_pointers.update({r : i})
    clusters.append([mean])

for kk in range(max_loops):
    for j in range(data_count):
        point = data_1[j]
        min_dist = float("inf")
        nearest_mean_index = -1
        for i in range(k):
            dist = euclidean(k_means[i], point)
            if min_dist > dist:
                min_dist = dist
                nearest_mean_index = i
        try:
            clusters[cluster_pointers[j]].remove(point)
        except:
            pass
        cluster_pointers[j] = nearest_mean_index
        clusters[nearest_mean_index].append(point)
        new_mean = np.mean(clusters[nearest_mean_index])
        k_means[nearest_mean_index] = new_mean
    print(kk)

xs = [[clusters[j][i][0] for i in range(len(clusters[0]))] for j in range(len(clusters))]
ys = [[clusters[j][i][1] for i in range(len(clusters[0]))] for j in range(len(clusters))]