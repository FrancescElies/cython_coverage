# cython: linetrace=True
# distutils: define_macros=CYTHON_TRACE=1

def func1(a, b):
    x = 1               #  5
    c = func2(a) + b    #  6
    return x + c        #  7


def func2(a):
    return a * 2        # 11

