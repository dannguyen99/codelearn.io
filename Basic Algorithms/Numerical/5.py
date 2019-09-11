import math
def lastDigitDiffZero(n):
    n = math.factorial(n)
    while n > 0:
        if n % 10 != 0:
            return n %10
        n //= 10