
class a:
    def __init__(self,f_name,l_name):
        self.f_name = f_name
        self.l_name = l_name

    def full_name(self):
        return f'{self.f_name} {self.l_name}'


class b(a):
    def __init__(self, f_name, l_name,age):
        super().__init__(f_name, l_name)
        self.age = age
    
    def full_name(self):
        return f'{self.l_name} {self.f_name}'
    @property
    def name_age(self):
        full_name =  super().full_name()
        return f'{full_name} {self.age}'
    @name_age.setter
    def name_age(self,age):
        self.age = age
    
ex1 = a("Koushik","Shirali")
ex2 = b("Koushik","Shirali",26)
ex2.name_age = 27
print(ex2.name_age)