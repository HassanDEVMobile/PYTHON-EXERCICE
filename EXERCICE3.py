from copyreg import constructor


def fun(a,b):
    a = a*2*3.14
    b = (b**0.5)*4
    if a>b:
        return True
    else:
        return False

print(fun(16, 625))

print(fun(5, 100))

print(fun(8, 144))

