import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier


dataset = pd.read_csv("/home/sumeet/Projects/BE-VIII/LP-3/ML-P3/data.csv")
x = dataset.iloc[:,:-1].values # independent variable.
y = dataset.iloc[:, 2].values # dependent variable.

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x, y)

x_test = np.array([6, 6])
y_pred = classifier.predict([x_test])
print("General KNN: ", y_pred)

classifier = KNeighborsClassifier(n_neighbors=3, weights="distance")
classifier.fit(x, y)
x_test = np.array([6, 6])
y_pred = classifier.predict([x_test])
print("Distance weighted KNN: ", y_pred)

