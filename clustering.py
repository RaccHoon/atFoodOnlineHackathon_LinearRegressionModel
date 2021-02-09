import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow.compat.v1 as tf
import csv
import os
vectors_set = []
foodList = []

f = open('clustering.CSV', 'r')
rdr = csv.reader(f)


for line in rdr:
    foodList.append(line[0])
    vectors_set.append([float(line[1]), float(line[2])])
f.close()
df = pd.DataFrame({"highest": [v[0] for v in vectors_set], "lowest": [v[1] for v in vectors_set]})
sns.lmplot("highest", "lowest", data=df, fit_reg=False, height=6)
plt.show()

with tf.Session() as sess:
    vectors = tf.constant(vectors_set)

    k = 6
    centroides = tf.Variable(tf.slice(tf.random_shuffle(vectors), [0, 0], [k, -1]))

    expanded_vectors = tf.expand_dims(vectors, 0)
    expanded_centroides = tf.expand_dims(centroides, 1)

    assignments = tf.argmin(tf.reduce_sum(tf.square(tf.subtract(expanded_vectors, expanded_centroides)), 2), 0)
    means = tf.concat([tf.reduce_mean(tf.gather(vectors, tf.reshape(tf.where(tf.equal(assignments, c)), [1, -1])), reduction_indices=[1]) for c in range(k)], axis=0)

    update_centroides = tf.assign(centroides, means)

    init_op = tf.initialize_all_variables()

    sess = tf.Session()
    sess.run(init_op)

    for step in range(100):
        _, centroid_values, assignments_values = sess.run([update_centroides, centroides, assignments])

    data = {"highest": [], "lowest": [], "cluster": []}
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []

    for i in range(len(assignments_values)):
        data["highest"].append(vectors_set[i][0])
        data["lowest"].append(vectors_set[i][1])
        data["cluster"].append(assignments_values[i])
        if assignments_values[i] == 0:
            one.append(foodList[i])
        elif assignments_values[i] == 1:
            two.append(foodList[i])
        elif assignments_values[i] == 2:
            three.append(foodList[i])
        elif assignments_values[i] == 3:
            four.append(foodList[i])
        elif assignments_values[i] == 4:
            five.append(foodList[i])
        else:
            six.append(foodList[i])
    print(four)
    clusterArr = [one, two, three, four, five, six]

    f = open("clusteredFoodListTotal.CSV", "w", newline='')
    wr = csv.writer(f)

    for line in clusterArr:
        wr.writerow(line)
    f.close()

    f = open("clusteredFoodList1.CSV", "w", newline='')
    wr = csv.writer(f)
    totalArr = []
    for number in one:
        f2 = open("treatedPrice.CSV", 'r')
        rdr = csv.reader(f2)
        for line in rdr:
            if line[0] == number:
                arr = []
                arr.append(number)
                arr.append(line[1])
                arr.append(line[2])
                totalArr.append(arr)
        f2.close()
    for line in totalArr:
        wr.writerow(line)
    f.close()

    f = open("clusteredFoodList2.CSV", "w", newline='')
    wr = csv.writer(f)
    totalArr = []
    for number in two:
        f2 = open("treatedPrice.CSV", 'r')
        rdr = csv.reader(f2)
        for line in rdr:
            if line[0] == number:
                arr = []
                arr.append(number)
                arr.append(line[1])
                arr.append(line[2])
                totalArr.append(arr)
        f2.close()
    for line in totalArr:
        wr.writerow(line)
    f.close()

    f = open("clusteredFoodList3.CSV", "w", newline='')
    wr = csv.writer(f)
    totalArr = []
    for number in three:
        f2 = open("treatedPrice.CSV", 'r')
        rdr = csv.reader(f2)
        for line in rdr:
            if line[0] == number:
                arr = []
                arr.append(number)
                arr.append(line[1])
                arr.append(line[2])
                totalArr.append(arr)
        f2.close()
    for line in totalArr:
        wr.writerow(line)
    f.close()

    f = open("clusteredFoodList4.CSV", "w", newline='')
    wr = csv.writer(f)
    totalArr = []
    for number in four:
        f2 = open("treatedPrice.CSV", 'r')
        rdr = csv.reader(f2)
        for line in rdr:
            if line[0] == number:
                arr = []
                arr.append(number)
                arr.append(line[1])
                arr.append(line[2])
                totalArr.append(arr)
        f2.close()
    for line in totalArr:
        wr.writerow(line)
    f.close()

    f = open("clusteredFoodList5.CSV", "w", newline='')
    wr = csv.writer(f)
    totalArr = []
    for number in five:
        f2 = open("treatedPrice.CSV", 'r')
        rdr = csv.reader(f2)
        for line in rdr:
            if line[0] == number:
                arr = []
                arr.append(number)
                arr.append(line[1])
                arr.append(line[2])
                totalArr.append(arr)
        f2.close()
    for line in totalArr:
        wr.writerow(line)
    f.close()

    f = open("clusteredFoodList6.CSV", "w", newline='')
    wr = csv.writer(f)
    totalArr = []
    for number in six:
        f2 = open("treatedPrice.CSV", 'r')
        rdr = csv.reader(f2)
        for line in rdr:
            if line[0] == number:
                arr = []
                arr.append(number)
                arr.append(line[1])
                arr.append(line[2])
                totalArr.append(arr)
        f2.close()
    for line in totalArr:
        wr.writerow(line)
    f.close()

    df = pd.DataFrame(data)
    sns.lmplot("highest", "lowest", data=df, fit_reg=False, size=6, hue="cluster", legend=False)
    plt.show()
