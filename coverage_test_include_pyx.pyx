# cython: linetrace=True
# distutils: define_macros=CYTHON_TRACE=1

cdef int x = 5                                   #  4

cdef int cfunc1(int x):                          #  6
    return x * 3                                 #  7

include "pkg/coverage_test_pyx.pxi"              #  9

def main_func(int x):                            # 11
    return cfunc1(x) + func1(x, 4) + func2(x)    # 12
