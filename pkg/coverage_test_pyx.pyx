# cython: linetrace=True
# distutils: define_macros=CYTHON_TRACE=1

def func1(int a, int b):
    cdef int x = 1      #  5
    c = func2(a) + b    #  6
    return x + c        #  7


def func2(int a):
    return a * 2        # 11
