class A:
    def __new__(cls, a):
        print("Hi I am a new method")
        cls.a = 10
        print(cls.a)
        return object.__new__(cls)

    def __init__(self, a):
        print("Hi I am a init method")
        self.b = a


x = A(20)
