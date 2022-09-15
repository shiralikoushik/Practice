################## Function Decorator ###################


def decortaor_method(original_func):
    def wrapper_method(*args,**kwargs):
        print("Koushik")
        return original_func(*args,**kwargs)

    return wrapper_method


@decortaor_method
def display(name):
    print(name)


# display = decortaor_method(display)

display("Shirali")

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
