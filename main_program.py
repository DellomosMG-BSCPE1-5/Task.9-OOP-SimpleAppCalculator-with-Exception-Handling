from calculator_class import Calculator

calculate = Calculator()
try:
    calculate.menu()
except ValueError as ERROR:
    print("\nInvalid Input. Please enter a numeric character from 1-4 only.\n")
    calculate.menu()