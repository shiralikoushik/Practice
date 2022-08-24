def strong(li):
    strongest = []
    for i in range(len(li) - 1):
        strongest.append(max(li[i],li[i+1]))
    print(strongest)

strong([1,2,2,3,4,5])
strong([5,5])