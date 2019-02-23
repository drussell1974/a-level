"""
1. Download the appropriate version of line_profiler https://www.lfd.uci.edu/~gohlke/pythonlibs/#line_profiler
2. Run... 'pip install line_profiler-*.whl'
3. Add the @profile decorator to the function
3. From the command line run 'kernprof -l -v adder.py'
"""

@profile
def add(x, y):
    return x + y

