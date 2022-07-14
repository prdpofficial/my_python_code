def add(a,b):
    return a+b

def calc(a,b):
    return lambda a ,b : a+b

print(add(5,6))
print(calc(5,6))

def myfunc(n):
      yield lambda a : a * n

mydoubler = myfunc(3)

p=mydoubler(11)

print(p.__next__())

