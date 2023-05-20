#importing the Calculator class into the main_program file
from calculator_class import Calculator

#construct an object named simple_calculator
simple_calculator = Calculator()
#by calling the 'menu method', diplay the menu and ask the user what operation he/she wants to use
operation = simple_calculator.menu()

#if the user enters number 1, call the 'addition method'
if operation == 1:
    simple_calculator.addition()
#if the user enters number 2, call the 'subtraction method'
#if the user enters number 3, call the 'multiplication method'
#if the user enters number 4, call the 'division method'
#after using the program, ask the user if he/she wants to use the program again

