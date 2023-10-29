import csv

i = 1

def next():
    global i
    if i <= 7186:
        with open('lab1/dataset.csv', "r") as file:
            reader = csv.reader(file, delimiter=",")
            j = 0
            for row in reader:
                if i == j:
                    x = row
                    break
                j+=1
            file.close()
        i+=1
        return row
        
print(next())
print(next())
print(next())
print(next())