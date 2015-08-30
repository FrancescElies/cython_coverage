```
    python -c 'import shutil; shutil.copy("pkg/coverage_test_pyx.pyx", "pkg/coverage_test_pyx.pxi")'
    python setup.py build_ext -i
    python coverage_test.py
```
