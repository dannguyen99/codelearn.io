from math import sqrt

def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
    else:
        return False
    return True

def primeSum(n):
    result = 0
    for i in range(n+1):
        if isPrime(i):
            result += i
            # print(i)
    return result % 22082018

print(primeSum(5))