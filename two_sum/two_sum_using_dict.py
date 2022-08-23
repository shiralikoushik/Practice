def two_pair(arr,num):
    dif = 0
    dic1 = {}
    for i in range(len(arr)):
        diff = num - arr[i]
        if diff in dic1:
            return (dic1[diff],i)
        else:
            dic1[arr[i]] = i

print(two_pair([1, 4, 45, 6, 10, 8],16))
        