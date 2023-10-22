import os
import csv

with open('lab2/lab2-1/X.csv', 'w', newline='') as X:
    with open('lab2/lab2-1/Y.csv', 'w', newline='') as Y:
        X_filewriter = csv.writer(X, delimiter = " ", lineterminator="\r")
        Y_filewriter = csv.writer(Y, delimiter = " ", lineterminator="\r")
        with open("lab1/dataset.csv") as dataset:
            reader = csv.reader(dataset, delimiter = ",")
            for row in reader:
                if row[0]!="Date":
                    X_filewriter.writerow([row[0]])
                    Y_filewriter.writerow([row[1]])