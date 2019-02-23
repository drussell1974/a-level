from line_profiler import LineProfiler
import random

def do_stuff(numbers):
    s = sum(numbers)
    l = [numbers[i]/43 for i in range(len(numbers))]
    m = ['hello'+str(numbers[i]) for i in range(len(numbers))]

numbers = [random.randint(1,100) for i in range(1000)]
lp = LineProfiler()
lp_wrapper = lp(do_stuff)
lp_wrapper(numbers)
lp.print_stats()
"""
LineProfiler class in line_profiler.py inherits from CLineProfiler

(See _line_profiler.pyx at https://github.com/rkern/line_profiler/blob/master/_line_profiler.pyx)

CLineProfiler includes get_stats that returns a LineStats containing timings and unit.

"""
stats = lp.get_stats()


""" Gets the timings line by line e.g. {('adder_inline.py', 4, 'do_stuff'): [(5, 1, 28), (6, 1, 646), (7, 1, 1382)]} """
print(stats.timings)

""" Gets the timer unit e.g. 4.1025624194615713e-07 """
print(stats.unit)

""" get the line number and hits for the function
"""
for func in stats.timings.items():
    print(func[0]) # function

for lines in stats.timings.items():
    for line in lines[1]: # the lines
        print("line number: %s " % line[0]) # line number
        print("hits: %s " % line[1]) # hits
        print("time: %s " % line[2]) # time
