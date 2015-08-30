python setup.py build_ext -i
nosetests -vs --with-coverage  tests/test_nose.py
python -c "import coverage; print 'coverage = ', coverage.__version__"
python -c "import cython; print 'cython =', cython.__version__"
