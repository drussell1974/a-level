def div(x, y):
    return x / y

def sqrt(x):
    return x * x

def _tests():
    # div tests
    assert div(1,1) == 1, "fail"
    assert div(3,2) == 1.5, "fail"
    # sqrt
    assert sqrt(5) == 25, "fail"
    assert sqrt(-5) == 25, "fail"
    
    
if __name__ == '__main__':
    _tests()