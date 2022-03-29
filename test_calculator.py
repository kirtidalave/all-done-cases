import calculator
import pytest

@pytest.mark.parametrize("a,b,c",[(93,2,5),(10,12,15),(2,5,8),(7,8,15)])
def test_add(a,b,c):

    result = calculator.add(a,b)
    assert c==result

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