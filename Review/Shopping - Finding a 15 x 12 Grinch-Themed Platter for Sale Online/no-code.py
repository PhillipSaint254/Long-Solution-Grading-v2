import random, math

class GsTraffgon:
    def __init__(self):
        self.start_index = random.randint(1, 1000)
        self.end_index = 1001
        self.seed = 42

    def patriach(self):
        return random.randint(self.start_index, self.end_index)

    def matriach(self):
        return random.randint(self.start_index, self.end_index)
    
    def reset(self):
        self.start_index = random.randint(1, 1000)

    def shuffle(self):
        patriach = self.patriach()
        matriach = self.matriach()

        if math.sqrt(patriach+matriach) % 10 == 0:
            print("won platinum")
            self.reset()
            return 1
        
        if patriach == matriach:
            print("won bronze")
            self.reset()
            return 1

        if abs(patriach - matriach) <= 10:
            print("Won silver")
            self.reset()
            return 1

        return 0
    
    def __str__(self):
        return f"Start: {self.start_index}, End: {self.end_index}"
    
if __name__ == "__main__":
    traffgon = GsTraffgon()

    for index in range(1000):
        print(index+1, end=": ")

        shuffle = traffgon.shuffle()
        if shuffle == 1:
            print("Congratulations.")
        else:
            print("Out!")
