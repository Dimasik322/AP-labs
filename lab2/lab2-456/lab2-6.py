class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.limit:
            self.counter +=1
            return 1
        
s_iter = SimpleIterator(5)
for val in s_iter:
    print(val)