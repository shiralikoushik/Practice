class Car:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __repr__(self):
        return f"{self.name},{self.model}"


class garage:
    def __init__(self):
        self.set = []

    def __len__(self):
        return len(self.set)

    def add_car(self, car):
        self.set.append(car)


ford = garage()
endevour = Car("Ford", "Endevour")
ford.add_car("endevour")
print(len(ford))
x = endevour
print(x)
print(ford.set)
