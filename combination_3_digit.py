def comb(li):
    if (len(li)!=3):
        print("Not a valid input")
    else:
        for i in li:
            for j in li:
                for k in li:
                    if ((i!=j)&(j!=k)&(k!=i)):
                        print(i,j,k)
comb([1, 2, 3])