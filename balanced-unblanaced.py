def check(my_string):
    brackets = ['()','{}','[]']
    lg = True
    while (lg):
        for br in brackets:
            print(br)
            my_string = my_string.replace(br,'')
            print("string is {}".format(my_string))
            print("Exit inside for loop")
        lg = False
        for x in brackets:
            if x in my_string:
                lg = True
    return not my_string

if (check("{([{{[()]}}])}")):
    print("Balanced")
else:
    print("Unbalanced")
