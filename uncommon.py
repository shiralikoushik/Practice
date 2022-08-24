li = [(1,2),(3,4),(5,6)]
li2 = [(3,4),(5,7),(1,2)]

res = set(map(tuple,li)) ^ set(map(tuple,li2))
print(res)
