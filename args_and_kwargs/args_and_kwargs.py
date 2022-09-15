def myFun(*args,**kwargs):
    print(args)
    print(kwargs)


kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun("a","b",x=3,y=4)


# li1 = [("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)]
#
# print(list(zip(*li1)))
