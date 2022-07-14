import functools as f

show= lambda a, b, c : a+b+c

k=f.partial(show,5)

l=f.partial(k,6)

m=l(3)

print(m)
