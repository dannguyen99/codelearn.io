import math
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

def greatestCommonPrimeDivisor(a, b):
    p1 = primeFactor(a)
    p2 = primeFactor(b)
    if max(p1) in p2 or max(p2) in p1:
        return int(max(p1))
    else:
        return -1