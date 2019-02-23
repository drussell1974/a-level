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

stats = lp.get_stats()

""" get the line number and hits for the function
"""


for lines in stats.timings.items():
    for line in lines[1]: # the lines
        print("line number: %s " % line[0]) # line number
        print("hits: %s " % line[1]) # hits
        print("time: %s " % line[2]) # time
