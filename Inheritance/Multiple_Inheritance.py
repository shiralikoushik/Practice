class Human:
    def __init__(self, age, name):
        self.name = name
        self.age = age
    def show(self):
        print(self.name)


class Sport:
    def __init__(self, game):
        self.game = game
    def show(self):
        print(self.game)


class student(Sport,Human):
    def __init__(self, age, name, game):
        Human.__init__(self, age, name)
        Sport.__init__(self, game)
    def show(self):
        super().show()

stu = student(26, "Koushik", "Cricket")

print(stu.name)
print(stu.game)
print(stu.age)

print(stu.show())