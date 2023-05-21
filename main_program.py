#importing the classes and modules into the main_program file
from calculator_class import Calculator
from user_interface import UserInterface

#construct an object named simple_calculator
simple_calculator = Calculator()
title_header = UserInterface()

while True:

    title_header.title()
    title_header.header()

    #by calling the 'menu method', diplay the menu and ask the user what operation he/she wants to use
    operation = simple_calculator.menu()

    #if the user enters number 1, call the 'addition method'
    if operation == 1:
        simple_calculator.addition()
    #if the user enters number 2, call the 'subtraction method'
    elif operation == 2:
        simple_calculator.subtraction()
    #if the user enters number 3, call the 'multiplication method'
    elif operation == 3:
        simple_calculator.multiplication()
    #if the user enters number 4, call the 'division method'
    else:
        simple_calculator.division()

    
    #ask if user wants to use the program again
    again = input("\nDo you want to use the program again? Type Y to restart or press another key to quit: ")  # Asking the user if he/she wants to try/start again.
    #if user typed "y", go back to the top.
    if again.upper() == "Y":  
        continue
    #else, if the user press other key, quit the program.
    print("\nThank you for using this program! Have a Nice Day!\n")
    break


