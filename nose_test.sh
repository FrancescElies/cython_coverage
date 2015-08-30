python -c "import coverage; print 'coverage = ', coverage.__version__"
python -c "import cython; print 'cython =', cython.__version__"
nosetests -vs --with-coverage  tests/test_nose.py
