def fib(n):
    fib_num = [0,1]
    for i in range(1,n-1):
        fib_num.append(fib_num[i]+fib_num[i-1])
    return fib_num

print(fib(3))