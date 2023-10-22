import os
import csv

with open("lab1/dataset.csv", "r", newline='') as dataset:
    reader = csv.reader(dataset, delimiter = ",")
    next(reader)
    year = 0
    min_year = 0
    max_year = 0
    for row in reader:
        if int(year) > int(max_year):
            max_year = int(year)
        if row[0][0:4:] == year:
            with open(f'lab2/lab2-2/{year}.csv', 'w', newline='') as file:
                filewriter = csv.writer(file, delimiter = ",", lineterminator="\r")
                filewriter.writerow(['Date', 'Value'])
                file.close()
        else:
            year = row[0][0:4:]
            min_year = int(year)
    dataset.close()
                    
with open("lab1/dataset.csv", "r", newline='') as dataset:
    reader = csv.reader(dataset, delimiter = ",")
    next(reader)
    year = 0
    for row in reader:
        year = int(row[0][0:4:])
        with open(f'lab2/lab2-2/{year}.csv', 'a', newline='') as file:
            filewriter = csv.writer(file, delimiter = ",", lineterminator="\r")
            filewriter.writerow(row)
            #last = str(row[0])[0:4] + str(row[0])[5:7] + str(row[0])[8:10]
            file.close()
    dataset.close()

for year in range(min_year, max_year+1):
    with open(f'lab2/lab2-2/{year}.csv', 'r', newline='') as file:
        count = 0
        reader = csv.reader(file, delimiter = ",")
        next(reader)
        for row in reader:
            if count == 0:
                last = row[0][0:4] + row[0][5:7] + row[0][8:10]
                count = 1
            first = row[0][0:4] + row[0][5:7] + row[0][8:10]
        count = 0
        file.close()
    os.rename(f'lab2/lab2-2/{year}.csv', f'lab2/lab2-2/{first}_{last}.csv')