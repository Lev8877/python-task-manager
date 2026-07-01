class Countdown:
    def __init__(self,num):
        self.num = num + 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.num -= 1
        if self.num < 0:
            raise StopIteration
        return self.num
    
countdown = Countdown(3)

for number in countdown:
    print(number)