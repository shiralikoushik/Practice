list1 = ["a", 1, "b", 2, "c", 3, "d", 4]

x = max([i for i in list1 if type(i) == int])

y = max(filter(lambda x: type(x) == int, list1))

print(x)
print(y)
