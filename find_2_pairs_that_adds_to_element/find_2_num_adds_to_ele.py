li = [1,2,5,4,3,8,10,7,15]
l = len(li)
lis = []
for i in range(len(li)):
    diff = 7 - li[i]
    if diff in li and (diff,li[i]) not in lis and diff != li[i]:
        lis.append((li[i],diff))

print(lis)

