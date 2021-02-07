import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.spatial.distance import euclidean
import time


img = mpimg.imread('data/sample_img1.png')
img.shape


print("Start!")
data_1 = img
k = 4
max_loops = 3
k_means = []
cluster_pointers = {}
clusters = []
data_count = data_1.shape

for i in range(k):
    r1 = np.random.randint(0, data_count[0])
    r2 = np.random.randint(0, data_count[1])
    mean = data_1[r1][r2]
    k_means.append(mean)
    cluster_pointers.update({(r1, r2) : i})
    clusters.append([mean])

for _ in range(max_loops):
    for j in range(data_count[0]):
        # start = time.time()
        for k_ in range(data_count[1]):
            point = data_1[j][k_]
            min_dist = float("inf")
            nearest_mean_index = -1
            for i in range(k):
                dist = euclidean(k_means[i], point)
                if min_dist > dist:
                    min_dist = dist
                    nearest_mean_index = i
            try:
                clusters[cluster_pointers[(j,k_)]].remove(point)
            except:
                pass
            cluster_pointers[(j,k_)] = nearest_mean_index
            clusters[nearest_mean_index].append(point)
        # end = time.time()
        # print(j)
        # print(end - start)
    for i in range(k):
        new_mean = sum(clusters[i]) / len(clusters[i])
        k_means[i] = new_mean

for r1, r2 in cluster_pointers.keys():
    cluster = cluster_pointers[(r1, r2)]
    mean = k_means[cluster]
    data_1[r1][r2] = mean

plt.imshow(data_1)
plt.savefig("k-2_128px.png")