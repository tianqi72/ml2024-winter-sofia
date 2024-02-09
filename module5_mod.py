class find_index:

    def __init__(self):
        self.numbers = []
    
    def read_number(self, num):
        self.numbers.append(num)

    def search(self, X):
        if X in self.numbers:
            return self.numbers.index(X) + 1
        else:
            return -1
