# def myFun(**x):
#     for i in x:
#         print(i)

# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(**kwargs)

# first,*last, l1 = [1]

# print(first)
# print(last)
# print(l1)

li1 = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]

print(list(zip(*li1)))
