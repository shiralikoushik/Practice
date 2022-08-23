def if_prime (n):
    """ Prints if a given number is prime or not"""
    for i in range(2,n):
        print(i)
        if n%i == 0:
            return False
    return True
def interval_prime(n):
    primes = []
    """ prints total prime numbers between 0 to given number"""
    for i in range(1,n):
        if i == 1 or i == 2:
            primes.append(i)
        else:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                primes.append(i)
    return(primes)       
                


def only_till_prime(n):
    """ prints only given number of prime"""
    count = []
    i = 2
    while len(count) < n:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            count.append(i)
        i += 1
    return count

#print(if_prime(1))

#print(interval_prime(10))

print(only_till_prime(10))