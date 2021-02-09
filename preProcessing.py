import csv
import os

f = open('price.CSV', 'r')
rdr = csv.reader(f)

dataList = []
foodList = []
clusteringList = []

for line in rdr:
    if line[3]=='KA' and line[7] == '소매' and line[9] == '상품':
        dataOneRankList = []
        month = (int(line[0])%10000)//100
        dataOneRankList.append(line[1])
        dataOneRankList.append(month)
        dataOneRankList.append(line[5])
        dataList.append(dataOneRankList)

        isNotInList = True
        for index in foodList:
            if index == line[1]:
                isNotInList = False
                break

        if isNotInList:
            foodList.append(line[1])

for food in foodList:
    highestPrice = 0.0
    lowestPrice = 999999999.0
    highestMonth = 0
    lowestMonth = 0

    for data in dataList:
        if food == data[0]:
            print(data[2], lowestPrice)
            if float(data[2])>highestPrice:
                highestPrice = float(data[2])
                highestMonth = data[1]
            elif float(data[2]) < lowestPrice:
                lowestPrice = float(data[2])
                lowestMonth = data[1]

    clusteringList.append([food, highestMonth, lowestMonth])

    for data in dataList:
        if food == data[0]:
            data[2] = (float(data[2])/highestPrice)*10
f.close()
print(dataList)

f = open("treatedPrice.CSV", "w", newline='')
wr = csv.writer(f)

for line in dataList:
    wr.writerow(line)
f.close()

f = open("clustering.CSV", "w", newline='')
wr = csv.writer(f)

for line in clusteringList:
    wr.writerow(line)
f.close()
