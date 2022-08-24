li = [(1,2,4,5,6,4),(2,3,4),(3,4,3,3,4),(4,4,3,2),(4,4,5)]
k = 4
test = []
for i in li:
    #print(i)
    for j in range((len(i)-1)):
       # print("j =",j)
       # print("i[j] =",i[j])
        #print("i[j+1] =",i[j+1])
        if ((i[j] == i[j+1]) and (i[j] == k)):
           # print("yes")
            test.append(i)
test = set(test)
for i in test:
    if i in li:
        li.remove(i)

print(li)