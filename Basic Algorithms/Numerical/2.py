import math
def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
    else:
        return False
    return True

def primeFactor(n):
    result = []
    while n%2 == 0:
        result.append(2)
        n /= 2
    for i in range(3,int(math.sqrt(n) +1), 2):
        while n % i == 0:
            result.append(i)
            n /= i
    if n > 2:
        result.append(n)
    return result

def factorSum(n):
    while not isPrime(int(n)):
        primes = primeFactor(n)
        n = 0
        for i in primes:
            n += i
    return int(n)

print(factorSum(24))