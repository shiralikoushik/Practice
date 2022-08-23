class Human:
    def __init__(self, age, name):
        self.name = name
        self.age = age

class Sport:
    def __init__(self,game):
        self.game = game

class student(Human,Sport):
    def __init__(self, age,name,game):
        Human.__init__(self,age,name)
        Sport.__init__(self,game)


stu = student(26,"Koushik","Cricket")

print(stu.name)
print(stu.game)
print(stu.age)