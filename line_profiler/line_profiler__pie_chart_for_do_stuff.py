from line_profiler import LineProfiler
import random

numbers = [random.randint(1,100) for i in range(1000)]
lp = LineProfiler()

from do_stuff import do_stuff # the module and function to profile

lp_wrapper = lp(do_stuff)
lp_wrapper(numbers)
#lp.print_stats()
stats = lp.get_stats()



"""
get the line number and times for each line in the function
"""

' read the file to get the lines of code '
f = open('do_stuff.py')
file = f.readlines()


labels = []
timings = []
for lines in stats.timings.items():
    for line in lines[1]: # the lines
        ' Adds the line of code '
        line_of_code = "#%s: %s" % (line[0], file[int(line[0])-1].strip())
        labels.append(line_of_code) # line of code
        
        ' Adds the timings '
        timings.append(line[2]) # timing

# convert timings to percentages

total_time = sum(timings)

for i in range(len(timings)):
    timings[i] = timings[i] / total_time * 100
    
"""
Create a pie chart
"""
import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()
ax1.pie(timings, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

