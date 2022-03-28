import calculator

def test_add():
    x = 10
    y = 25
    result = calculator.add(x,y)
    assert x+y==result

def test_sub():
    x = 20
    y = 12
    result = calculator.substract(x,y)
    assert x-y==result

def test_mult():
    x = 15
    y = 20
    result = calculator.multiply(x,y)
    assert x*y==result

def test_div():
    x = 12
    y = 15
    result = calculator.divide(x,y)
    assert x/y==result