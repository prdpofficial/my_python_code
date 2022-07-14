import collections
q =collections.deque()

squ2= list(map(lambda x : x**2 ,range(11)))
squ3= q(squ2)
squ2.append(121)
squ2.popleft()
print(squ2)
