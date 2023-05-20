from calculator_class import Calculator

calculate = Calculator()

try:
    calculate.get_numbers()
except ValueError as ERROR:
    print("\nInvalid Input. Please enter a numeric character.\n")
    calculate.get_numbers()

calculate.addition()