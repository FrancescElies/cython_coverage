from pkg import coverage_test_pyx
from coverage import coverage
from io import StringIO, BytesIO
from nose import with_setup

module = coverage_test_pyx
cov = coverage()
def setup():
    cov.start()
 
def teardown():
    cov.stop()
    out = BytesIO()
    cov.report(file=out)
    lines = out.getvalue().splitlines()
    print lines
    
@with_setup(setup, teardown)
def test01():
    assert module.func1(1, 2) == (1 * 2) + 2 + 1


