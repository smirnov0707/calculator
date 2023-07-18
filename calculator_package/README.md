# Calculator Package

This is a Python package that provides a Calculator class for performing basic arithmetic operations.

## Installation

You can install the package using pip:

pip install calculator_package


### Usage
To use the Calculator class, first import it in your Python script:


from calculator_package.calculator.calculator import Calculator

#### Then, create an instance of the Calculator class and perform calculations:

calculator = Calculator()
calculator.add(2)
print(calculator.memory)  # Output: 2

calculator.multiply(3)
print(calculator.memory)  # Output: 6

calculator.reset_memory()
print(calculator.memory)  # Output: 0

##### The Calculator class provides the following methods:

add(num): Adds a number to the calculator's memory.
subtract(num): Subtracts a number from the calculator's memory.
multiply(num): Multiplies the calculator's memory by a number.
divide(num): Divides the calculator's memory by a number.
take_root(n): Takes the nth root of the calculator's memory.
reset_memory(): Resets the calculator's memory to 0.

##### For detailed documentation of the available methods, refer to the docstrings in the calculator.py file.
