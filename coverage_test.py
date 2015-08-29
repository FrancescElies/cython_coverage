import re
import os.path
try:
    # io.StringIO in Py2.x cannot handle str ...
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from coverage import coverage

from pkg import coverage_test_py
from pkg import coverage_test_pyx
import coverage_test_include_pyx


for module in [coverage_test_py, coverage_test_pyx, coverage_test_include_pyx]:
    assert not any(module.__file__.endswith(ext) for ext in '.py .pyc .pyo .pyw .pyx .pxi'.split()), \
        module.__file__


def source_file_for(module):
    module_name = module.__name__
    path, ext = os.path.splitext(module.__file__)
    platform_suffix = re.search(r'[.]cpython-[0-9]+[a-z]*$', path, re.I)
    if platform_suffix:
        path = path[:platform_suffix.start()]
    return path + '.' + module_name.rsplit('_', 1)[-1]


def run_coverage(module):
    module_name = module.__name__
    module_path = module_name.replace('.', os.path.sep) + '.' + module_name.rsplit('_', 1)[-1]

    cov = coverage()
    cov.start()
    assert module.func1(1, 2) == (1 * 2) + 2 + 1
    assert module.func2(2) == 2 * 2
    if '_include_' in module_name:
        assert module.main_func(2) == (2 * 3) + ((2 * 2) + 4 + 1) + (2 * 2)
    cov.stop()

    out = StringIO()
    cov.report(file=out)
    #cov.report([module], file=out)
    lines = out.getvalue().splitlines()
    assert any(module_path in line for line in lines), "'%s' not found in coverage report:\n\n%s" % (
        module_path, out.getvalue())

    mod_file, exec_lines, excl_lines, missing_lines, _ = cov.analysis2(source_file_for(module))
    assert module_path in mod_file

    if '_include_' in module_name:
        executed = set(exec_lines) - set(missing_lines)
        assert all(line in executed for line in [7, 12]), '%s / %s' % (exec_lines, missing_lines)

        # rest of test if for include file
        mod_file, exec_lines, excl_lines, missing_lines, _ = cov.analysis2(
            os.path.join(os.path.dirname(module.__file__), "pkg", "coverage_test_pyx.pxi"))

    executed = set(exec_lines) - set(missing_lines)
    assert all(line in executed for line in [5, 6, 7, 11]), '%s / %s' % (exec_lines, missing_lines)


if __name__ == '__main__':
    run_coverage(coverage_test_py)
    run_coverage(coverage_test_pyx)
    run_coverage(coverage_test_include_pyx)
