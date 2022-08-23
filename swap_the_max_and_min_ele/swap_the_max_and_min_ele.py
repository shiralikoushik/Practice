list1 = [1,2,3,4,"Koushik",5,6,7,8,9,"Shirali"]

y = {i:list1[i] for i in range(len(list1)) if type(list1[i]) == str}
for value in y.values():
    list1.remove(value)

max1 = list1.index(max(list1))
min1 = list1.index(min(list1))


list1[min1],list1[max1] = max(list1), min(list1)

for ky,value in y.items():
    list1.insert(ky,value)


print(list1)
