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

"""
get the line number and times for each line in the function
"""
    
line_nos = []
timings = []
for lines in stats.timings.items():
    for line in lines[1]: # the lines
        line_nos.append(line[0]) # line number
        timings.append(line[2]) # time

# convert timings to perctange

total_time = sum(timings)

for i in range(len(timings)):
    timings[i] = timings[i] / total_time * 100
    
"""
Create a line graph
"""
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(1,1,1)
plt.plot(line_nos, timings, "o-")
plt.title('Execution')
plt.ylabel('time %')
plt.xlabel('line #')
plt.show()

