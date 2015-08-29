from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize([
    'coverage_test_*.py*',
    'pkg/coverage_test_*.py*'
]))
