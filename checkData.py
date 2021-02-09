import csv
import os

f = open('price.CSV', 'r')
rdr = csv.reader(f)
"""
food = input("작물 번호를 입력: ")

for line in rdr:
    if line[0] == food:
        print(line[1], "월: ", line[2])
"""
foodList = []

for line in rdr:
    isNotIn = True
    if float(line[2]) <= 6:
        for i in foodList:
            if i == line[0]:
                isNotIn = False
        if isNotIn:
            foodList.append(line[0])

for i in foodList:
    print(i)