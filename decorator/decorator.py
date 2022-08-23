
################## Function Decorator ###################

def decortaor_method(original_func):
    def wrapper_method():
        print("I am a wrapper method")
        return 
        original_func()
    return wrapper_method
@decortaor_method
def display():
    print("Hi I am a display method")

# display = decortaor_method(display)

display()

################## Class Decorator ######################

# class decorator_class:
#     def __init__(self,original_fun):
#         self.original_fun = original_fun

#     def __call__(self):
#         print("Hi How are you")
#         return self.original_fun()


# @decorator_class
# def display():
#     print("Hi I am a display method")

# display()