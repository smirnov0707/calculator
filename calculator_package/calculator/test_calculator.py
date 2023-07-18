from calculator.calculator import Calculator

def test_calculator():
    calc = Calculator()

    assert calc.add(2) == 2
    assert calc.subtract(1) == 1
    assert calc.multiply(3) == 3
    assert calc.divide(2) == 1.5
    assert calc.root(2) == 1.224744871391589
    assert calc.reset() == 0
