import pytest
from racunske_operacije import Calculator

@pytest.fixture
def calculator():
    """Kreiranje instance klase Calculator za testiranje"""
    return Calculator(10, 5)

def test_add(calculator):
    """Testiranje sabiranja"""
    assert calculator.add() == 15

def test_subtract(calculator):
    """Testiranje oduzimanja"""
    assert calculator.subtract() == 5

def test_multiply(calculator):
    """Testiranje množenja"""
    assert calculator.multiply() == 50

def test_divide(calculator):
    """Testiranje deljenja"""
    assert calculator.divide() == 2

def test_divide_by_zero():
    """Testiranje deljenja nulom"""
    calc = Calculator(10, 0)
    assert calc.divide() == "Deljenje nulom nije dozvoljeno!"
