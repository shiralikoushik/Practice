def add_method(num1, num2):
    return num1 + num2


def subtract_method(num1, num2):
    sub_ans = add_method(num1, -num2)
    return sub_ans


def multiplication_method(num1, num2):
    num3 = 0
    for i in range(num2):
        num3 = add_method(num1, num3)
    return num3


def division_method(num1, num2):
    num3 = num1
    counter = 0
    reminder = 0
    while num3 >= num2:
        num3 = add_method(num3, -num2)
        counter += 1
        if (num3 < num2) and (num3 != 0):
            reminder = num3
    return counter, reminder


print(division_method(10, 3))
