def ger():
    for i in range(10):
        yield (i, i + 1)


x = ger()

for i in x:
    print(i[0], i[1])
