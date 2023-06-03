#importing the classes and modules into the main_program file
from colorama import Fore, Style
from calculator_class import Calculator
from user_interface import UserInterface
from calculator_class_inheritance import CalculatorAppend

#construct objects
simple_calculator = Calculator()
the_interface = UserInterface()
simple_calculator_pt2 = CalculatorAppend()

while True:

    the_interface.title()
    the_interface.header()

    #by calling the 'menu method', diplay the menu and ask the user what operation he/she wants to use
    #operation = the_interface.menu()
    operation = simple_calculator_pt2.menu()

    #if the user enters number 1, call the 'addition method'
    if operation == 1:
        simple_calculator_pt2.addition()
    #if the user enters number 2, call the 'subtraction method'
    elif operation == 2:
        simple_calculator_pt2.subtraction()
    #if the user enters number 3, call the 'multiplication method'
    elif operation == 3:
        simple_calculator_pt2.multiplication()
    #if the user enters number 4, call the 'division method'
    elif operation == 4:
        simple_calculator_pt2.division()
    #else, if the user enters number 5, call the 'exponent method'
    else:
        simple_calculator_pt2.exponent()

    print("\n" + "=" * 95)
    #ask if user wants to use the program again
    again = input("Do you want to use the program again? Type Y to restart or press another key to quit: ")  # Asking the user if he/she wants to try/start again.
    #if user typed "y", go back to the top.
    if again.upper() == "Y":  
        continue
    print( "=" * 95)
    #else, if the user press other key, quit the program.
    print(Fore.CYAN + Style.BRIGHT + "\nThank you for using this program! Have a Nice Day!\n")
    break


