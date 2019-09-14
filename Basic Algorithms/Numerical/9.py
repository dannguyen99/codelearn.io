from math import factorial


def numberZeroDigits(n):
    result = 0
    n = factorial(n)
    while n > 0:
        if n % 10 != 0:
            return result
        else:
            result +=1
        n //= 10
    return result
