import matplotlib.pyplot as plt

def create_chart(stats, chart_no):
    labels = []
    timings = []
    for lines in stats.timings.items():
        for line in lines[1]: # the lines
            ' Adds the line of code or line number '
            labels.append(line[0]) 
            ' Adds the timings '
            timings.append(line[2]) # timing

    # convert timings to percentages

    total_time = sum(timings)

    for i in range(len(timings)):
        timings[i] = timings[i] / total_time * 100

    """
    Create a pie chart
    """

    fig1, ax1 = plt.subplots()
    ax1.pie(timings, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    fig1.savefig("figure"+str(chart_no)+".png")


from line_profiler import LineProfiler
import random

# the module and function to profile
from graph_traversal import depth_traversal, breadth_traversal

lp = LineProfiler()

# data
graph_1 = {
    "A":["C", "B",],
    "B":["K"],
    "C":["F", "D"],
    "D":["G", "H", "E"],
    "E":[],
    "F":["J","G"],
    "G":[],
    "H":[],
    "J":["H"],
    "K":[]
}

# profile the depth_traversal

lp_wrapper = lp(depth_traversal)
lp_wrapper(graph_1, "A")
stats1 = lp.get_stats()

# profile the breadth_traversal

lp_wrapper = lp(breadth_traversal)
lp_wrapper(graph_1, "A")
stats2 = lp.get_stats()


create_chart(stats1, 1)
create_chart(stats2, 2)

plt.show()

