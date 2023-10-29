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

#для разбивки по неделям
def value_by_date(_date):
    year = date.fromisoformat(_date).year
    month = date.fromisoformat(_date).month
    day = date.fromisoformat(_date).day
    day_of_week = date.fromisoformat(_date).isocalendar()[2]
    min_date = date.fromisoformat(_date) - timedelta(days=day_of_week)
    max_date = date.fromisoformat(_date) + timedelta(days=(7-day_of_week))
    for i in range(0, 8):
        for j in range(0, 8):
            first = min_date + timedelta(days=i)
            last = max_date - timedelta(days=j)
            path = os.getcwd() + f"/lab2/lab2-3/{str(first)[0:4]}{str(first)[5:7]}{str(first)[8:10]}_{str(last)[0:4]}{str(last)[5:7]}{str(last)[8:10]}.csv"
            if os.path.exists(path) == True:
                with open(path, "r") as file:
                    reader = csv.reader(file, delimiter=",")
                    for row in reader:
                        if row[0] == _date:
                            return row[1]
    return None
                        
#для разбивки по годам
def value_by_date(_date):
    year = date.fromisoformat(_date).year
    month = date.fromisoformat(_date).month
    day = date.fromisoformat(_date).day
    day_of_week = date.fromisoformat(_date).isocalendar()[2]
    min_date = date.fromisoformat(f'{year}-01-01')
    max_date = date.fromisoformat(f'{year}-12-31')
    #print(min_date, max_date)
    for i in range(0, 365):
        for j in range(0, 365):
            first = min_date + timedelta(days=i)
            last = max_date - timedelta(days=j)
            path = os.getcwd() + f"/lab2/lab2-3/{str(first)[0:4]}{str(first)[5:7]}{str(first)[8:10]}_{str(last)[0:4]}{str(last)[5:7]}{str(last)[8:10]}.csv"
            if os.path.exists(path) == True:
                with open(path, "r") as file:
                    reader = csv.reader(file, delimiter=",")
                    for row in reader:
                        if row[0] == _date:
                            return row[1]  
    return None 


print(value_by_date('2004-06-26'))