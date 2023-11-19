import csv

i = 1

def next()->str:
    """возвращает кортежи [дата, значение]"""
    for i in range(1, 7187):
        with open('lab1/dataset.csv', "r") as file:
            reader = csv.reader(file, delimiter=",")
            j = 0
            for row in reader:
                if i == j:
                    x = row
                    break
                j+=1
        file.close()
        yield row
        
def main():
    for i in next():
        print(i)

if __name__ == '__main__':
    main()