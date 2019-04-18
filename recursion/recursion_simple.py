def recursion_made_simple(stop_at, current):
    if current > stop_at:
        return 1
    return recursion_made_simple(stop_at, current+1)
    
print(recursion_made_simple(2987, 1))