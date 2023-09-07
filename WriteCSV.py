# 写入csv文件，保留4位小数

import csv
import numpy as np


def writeXY(name, X, y, type):
    with open(name, type, newline='') as file:
        writer = csv.writer(file)
        if type == 'w':
            writer.writerow(['X', 'y'])
        # print(type(X[0]))
        # print(X[0])
        for i in range(len(X)):
            # if X[i]!='nan':
            writer.writerow([X[i], y[i]])


def writeMultiRow(name, X, y, type):
    temp = []
    with open(name, type, newline='') as file:
        writer = csv.writer(file)
        if type == 'w':
            writer.writerow(['X', 'y'])
        for i in range(len(X)):
            # if X[i]!='nan':
            writer.writerow([X[i], y[i]])
