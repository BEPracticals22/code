import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


# Read dataset
dataset = pd.read_csv("/home/sumeet/Projects/BE-VIII/LP-3/ML-P1/data.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values
regressor = LinearRegression()
regressor.fit(x, y)
print(regressor.coef_)
print(regressor.intercept_)
print("Accureccy: ", regressor.score(x, y)*100)
plt.plot(x, y, 'o')
plt.plot(x, regressor.predict(x))
plt.show()