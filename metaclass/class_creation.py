class test:
    y = 5

Test = type("Test",(test,),{"x":5})

"""Here both the Test and test are class and object of the class type. 
ie when i create a test class(above) in background the new method of the type class is called.
which retuns its object like type("test",(),{"x":5}) and this type class is called meta class
here inside type() the first argument is class_name, second argument is class name from which
it is inherting, and third argument is attributes"""

# ob = test()
# print(ob.x)

ob1 = Test()
print(ob1.y)