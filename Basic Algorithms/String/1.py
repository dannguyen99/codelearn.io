import string
def checkStrongPassword(password):
    if len(password) < 6:
        return False
    digits = '1234567890'
    specials = '!@#$%^&*()-+'
    di = False
    low = False
    up = False
    spec = False
    for i in password:
        if di and low and up and spec:
            return True
        elif i in string.ascii_lowercase:
            low = True
        elif i in string.ascii_uppercase:
            up = True
        elif i in digits:
            di = True
        elif i in specials:
            spec = True
    return di and low and up and spec
