import csv
import pandas as pd

class SimpleIterator:
    def __init__(self, path_file):
        with open(path_file, "r") as file:
            reader = csv.reader(file, delimiter=",")
            limit = len(file.readlines())
        self.limit = limit
        self.counter = 1
        self.path = path_file

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            with open(self.path, "r") as file:
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
        
def main():
    s_iter = SimpleIterator('lab1/dataset.csv')
    print(next(s_iter))
    print(next(s_iter))
    print(next(s_iter))

if __name__ == '__main__':
    main()
