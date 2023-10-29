import os
import csv
from datetime import date
from datetime import timedelta
import os.path

#для dataset
def value_by_date(_date):
    with open("lab1/dataset.csv", "r", newline='') as dataset:
        reader = csv.reader(dataset, delimiter = ",")
        next(reader)
        for row in reader:
            if row[0] == _date:
                return row[1]
        return None
    
#для X и Y 
def value_by_date(_date):
    with open("lab2/lab2-1/X.csv", "r", newline='') as X:
        readerX = csv.reader(X, delimiter="\n")
        number = 0
        flag = False
        for row in readerX:
            print(row)
            if row[0] == _date:
                flag = True
                break;
            number+=1
        if flag == False:
            return None
        else:
            with open("lab2/lab2-1/Y.csv", "r", newline='') as Y:
                readerY = csv.reader(Y, delimiter="\n")
                i = 0
                for row in readerY:
                    if i == number:
                        return row[0]
                    else:
                        i+=1

#для разбивки по годам
def value_by_date(_date):
    year = date.fromisoformat(_date).year
    month = date.fromisoformat(_date).month
    day = date.fromisoformat(_date).day
    day_of_week = date.fromisoformat(_date).isocalendar()[2]
    min_date = date.fromisoformat(_date) - day_of_week * timedelta(days=1)
    max_date = date.fromisoformat(_date) + ((7 - day_of_week) * timedelta(days=1))
    for i in range(0, 7):
        for j in range(0, 7):
            i = min_date + timedelta(days=i)
            j = max_date - timedelta(days=j)
            print(i, j)
    if os.path.exists(f"/lab2/lab2-2/{str(min_date)[0:4]}{str(min_date)[5:7]}{str(min_date)[8:10]}_{str(max_date)[0:4]}{str(max_date)[5:7]}{str(max_date)[8:10]}") == True:
        with open(f'/lab2/lab2-2/{str(min_date)[0:4]}{str(min_date)[5:7]}{str(min_date)[8:10]}_{str(max_date)[0:4]}{str(max_date)[5:7]}{str(max_date)[8:10]}', "r") as file:
             reader = csv.reader(file, delimiter=",")
             print("fk yes")
    #print(year, month, day_of_week)


print(value_by_date('1992-07-03'))