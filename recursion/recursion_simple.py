# https://pythontips.com/2013/08/31/fixing-error-maximum-recursion-depth-reached/

import sys
print(sys.getrecursionlimit())
#sys.setrecursionlimit(6000)

def recursion_made_simple(stop_at, current):
    if current > stop_at:
        return 1
    return recursion_made_simple(stop_at, current+1)
    
    
print(recursion_made_simple(2999, 1))