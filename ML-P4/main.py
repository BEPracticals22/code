import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

x = [
    [0.1, 0.6],
    [0.15, 0.71],
    [0.08, 0.9],
    [0.16, 0.85],
    [0.2, 0.3],
    [0.25, 0.5],
    [0.24, 0.1],
    [0.3, 0.2]
]

centers = np.array([[0.1, 0.6], [0.3, 0.2]])
print('Initial centeroids: ', centers)

model = KMeans(n_clusters=2, init=centers, n_init=1)
model.fit(x)
print(model.labels_)

# P6 location.
print('P6 belongs to: ', model.labels_[5])

# Cout where value is set to 1.
print("Number of population around cluster 2: ", np.count_nonzero(model.labels_ == 1))

print("New centroids: ", model.cluster_centers_)
print(centers)