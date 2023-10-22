import os
import csv
from datetime import date

with open("lab1/dataset.csv", "r", newline='') as dataset:
    reader = csv.reader(dataset, delimiter = ",")
    next(reader)
    year = -1
    week = -1
    first = 0
    last = 0
    count = 0
    count_of_files = -1
    for row in reader:
        if year != date(int(row[0][0:4]), int(row[0][5:7]), int(row[0][8:10])).isocalendar()[0] or week != date(int(row[0][0:4]), int(row[0][5:7]), int(row[0][8:10])).isocalendar()[1]:
            year = date(int(row[0][0:4]), int(row[0][5:7]), int(row[0][8:10])).isocalendar()[0]
            week = date(int(row[0][0:4]), int(row[0][5:7]), int(row[0][8:10])).isocalendar()[1]
            count_of_files+=1
            with open(f'lab2/lab2-3/{count_of_files}.csv', 'w', newline='') as file:
                filewriter = csv.writer(file, delimiter = ",", lineterminator="\r")
                filewriter.writerow(['Date', 'Value'])
                filewriter.writerow(row)
                file.close()
                if count_of_files != 0:
                    os.rename(f'lab2/lab2-3/{count_of_files-1}.csv', f'lab2/lab2-3/{first}_{last}.csv')
                last = str(row[0][0:4]) + str(row[0][5:7]) + str(row[0][8:10])
        else:
            with open(f'lab2/lab2-3/{count_of_files}.csv', 'a', newline='') as file:
                    filewriter = csv.writer(file, delimiter = ",", lineterminator="\r")
                    filewriter.writerow(row)
                    file.close()
                    first = str(row[0][0:4]) + str(row[0][5:7]) + str(row[0][8:10])
    os.rename(f'lab2/lab2-3/{count_of_files}.csv', f'lab2/lab2-3/{first}_{last}.csv')
    dataset.close()