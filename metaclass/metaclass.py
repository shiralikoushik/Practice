"""Meta class is the class which sits above the class which is created
the class which we have created acts as object of meta class which is "type" class"""


class MetaClass(type):
    def __new__(cls,class_name,base,attr):
        print(attr)
        dic = {}
        for key,val in attr.items():
            if key.startswith("__"):
                dic[key] = val
            else:
                dic[key.upper()] = val
        print(dic)
        return type(class_name,base,dic)

class abc(metaclass=MetaClass):
    x = 10
    y = 11

    def show(self):
        print("hi")

ob = abc()

print(ob.X)
