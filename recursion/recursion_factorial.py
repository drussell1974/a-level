def iterative_factorial(num):
    factorial = 1
    for x in range(1, num+1):
        factorial = factorial * x
    return factorial

def recursive_factorial(num):
    if num < 2:
        """ stop the recursion when num = 1 or less """
        return 1
    else:
        """ recursive call """
        return num * recursive_factorial(num-1) # num - 1 will stop the recursion

#print(iterative_factorial(5))
print(recursive_factorial(1))