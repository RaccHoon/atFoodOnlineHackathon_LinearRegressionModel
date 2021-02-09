import joblib
import csv
import os

f = open('result.CSV', 'w', newline='')
wr = csv.writer(f)
load_model = joblib.load("./linearRegressionModel.pkl")

for i in range(12):
    line = []
    prediction = load_model.predict([[i+1, (i+1)**2, (i+1)**3]])
    line.append(i+1)
    line.append(prediction)
    wr.writerow(line)

