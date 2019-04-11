def recursion_fibonacci(num):
    if num <= 1:
        return num
    else:
        return recursion_fibonacci(num-1) + recursion_fibonacci(num-2)
    
print(recursion_fibonacci(10))