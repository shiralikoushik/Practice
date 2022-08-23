"""Python Program for Sum of squares of first n natural numbers"""
user_input = int(input("Enter the number to find the squares: "))
cou = 0
for i in range(1, user_input + 1):
    cou += i * i

print(cou)
