def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                return False
    else:
        return False
    return True

def digitsProduct(product):
    result = []
    if product == 0:
        return 10
    elif product < 10:
        return product
    elif product >= 10 and isPrime(product):
        return -1
    while product != 1:
        for i in range(9, 1, -1):
            if product % i == 0:
                result.append(i)
                product /= i
                break
    number = ""
    for i in range(len(result) - 1, -1, -1):
        number += str(result[i])
    return int(number)

print(digitsProduct(12))
