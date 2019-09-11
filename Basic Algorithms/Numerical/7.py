def pagesNumbering(n):
    if n < 10:
        return n
    else:
        pages = 9
        base = 10**(len(str(n))-1)
        while n > 0:
            print("base",base)
            print("n",n)
            pages += (n - base) * len(str(n))
            base //= 10
            n //= 10
        return pages

print(pagesNumbering(11))