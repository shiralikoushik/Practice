"""Find the max valued integer from a list which contains integer and string in one line code"""

list1 = ["a", 1, "b", 2, "c", 3, "d", 4]

x = max([i for i in list1 if type(i) == int])

y = max(filter(lambda x: type(x) == int, list1))

print(x)
print(y)
