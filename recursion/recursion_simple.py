def sum(number):
    if number == 0:
        return number
    else:
        return sum(number-1)

import sys
sys.setrecursionlimit(1000)
print(sum(998))