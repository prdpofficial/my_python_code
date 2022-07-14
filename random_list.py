import random

class Ran_number :
    n = int(input())
    random.seed(10)
    x=[random.randrange(10,500,10) for i in range(n)]
    print(x)
    random.shuffle(x)
    print(x)
    random.seed(14)
    x=[random.randrange(10,500,10) for i in range(n)]
    print(x)
    
