def pagesNumbering(n):
    if n < 10:
        return n
    else:
        pages = 9
        base = 10**(len(str(n))-1)
        while n > 10:
            # print("base",base)
            # print("n",n)
            pages += (n - base + 1) * len(str(n))
            # print((n - base + 1) * len(str(n)))
            n = base - 1
            base //= 10
        return pages

print(pagesNumbering(1000))