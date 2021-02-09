from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import csv
import matplotlib.pyplot as plt
import pickle
import joblib

def makeLearningDataSet():
    x_data = []
    y_data = []

    f = open('clusteredFoodList3.CSV', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    for line in rdr:
        x_data.append(int(line[1]))
        y_data.append(float(line[2]))

    data_set = [x_data, y_data]
    return data_set

def regressionModel():

    data_set = makeLearningDataSet()
    x_data = [np.array(data_set[0])]
    x_data = np.transpose(x_data)
    y_data = [np.array(data_set[1])]
    y_data = np.transpose(y_data)

    plt.plot(x_data, y_data, "b.")
    plt.ylabel("Y", fontsize=15, rotation=0)
    plt.xlabel("X", fontsize=15)
    plt.show()

    poly_features = PolynomialFeatures(degree=3, include_bias=False)
    X_poly = poly_features.fit_transform(x_data)

    lin_reg = LinearRegression()
    lin_reg.fit(X_poly, y_data)

    X_new = np.linspace(1, 12, 100).reshape(100, 1)
    X_new_poly = poly_features.transform(X_new)
    y_new = lin_reg.predict(X_new_poly)
    plt.plot(x_data, y_data, "b.")
    plt.plot(X_new, y_new, "r-", linewidth=2, label="Predictions")
    plt.xlabel("$x_1$", fontsize=18)
    plt.ylabel("$y$", rotation=0, fontsize=18)
    plt.legend(loc="upper left", fontsize=14)
    plt.axis([1, 12, 6, 11])
    plt.show()

    if input("Do you want to make model?(Y/N) : ") == 'Y':
        joblib.dump(lin_reg, 'linearRegressionModeThree.pkl')

if __name__ == '__main__':
    regressionModel()