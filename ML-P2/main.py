import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from dtreeplt import dtreeplt

df = pd.read_csv("/home/sumeet/Projects/BE-VIII/LP-3/ML-P2/data.csv")
print(df.head())
x = df.iloc[:,:-1] # independent variable.
y = df.iloc[:,-1].values # dependent variable.
print("Our dependent cariable y consists of :", y)
# labelencoder_x = LabelEncoder()
x = x.apply(LabelEncoder().fit_transform)

regressor = DecisionTreeClassifier()
regressor.fit(x.iloc[:, 1:5], y)

x_inp = np.array([1, 1, 0, 0])
y_pred = regressor.predict([x_inp])

print(y_pred)


