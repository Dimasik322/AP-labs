import csv

class SimpleIterator:
    def __init__(self):
        self.limit = 7187
        self.counter = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            with open('lab1/dataset.csv', "r") as file:
                reader = csv.reader(file, delimiter=",")
                j = 0
                for row in reader:
                    if self.counter == j:
                        x = row
                        break
                    j+=1
                file.close()
            self.counter+=1
            return row
        else:
            raise StopIteration
