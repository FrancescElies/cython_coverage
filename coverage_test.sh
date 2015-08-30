python setup.py build_ext -i

python -c "import coverage; print 'coverage = ', coverage.__version__"
python -c "import cython; print 'cython =', cython.__version__"
python -c 'import shutil; shutil.copy("pkg/coverage_test_pyx.pyx", "pkg/coverage_test_pyx.pxi")'
python coverage_test.py
