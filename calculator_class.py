#Redo calculator program applying the OOP concept.
#import the UserInterface Class and some modules
from pyboxen import boxen
from colorama import Fore, Style
from user_interface import UserInterface

#construct an object
input = UserInterface()

#create a class named Calculator
class Calculator:

    #constructor
    def __init__(self):
        pass

    #create method for addition operation
    def addition(self):
        #ask inputs from user that are needed to perform the operation
        inputs = input.get_numbers()
        #perform the addition operation on two numbers and print the sum of the two numbers
        #the 1st number is inputs[0] and the 2nd number is inputs[1]
        print(Fore.CYAN + Style.BRIGHT + "\nThe sum is", Fore.WHITE + Style.NORMAL + str(inputs[0] + inputs[1]))

    #create method for subtraction operation
    def subtraction(self):   
        #ask inputs from user that are needed to perform the operation
        inputs = input.get_numbers()
        #perform the subtraction operation on two numbers.
        print(Fore.CYAN + Style.BRIGHT + "\nThe difference is", Fore.WHITE + Style.NORMAL + str(inputs[0] - inputs[1]))

    #create method for multiplication operation
    def multiplication(self):
        #ask inputs from user that are needed to perform the operation
        inputs = input.get_numbers()
        #perform the multiplication operation on two numbers.
        print(Fore.CYAN + Style.BRIGHT + "\nThe product is", Fore.WHITE + Style.NORMAL + str(inputs[0] * inputs[1]))

    #create method for division operation
    def division(self):
        while True:
            try:
                #ask inputs from user that are needed to perform the operation
                inputs = input.get_numbers()
                #perform the division operation on two numbers.
                quotient = inputs[0] / inputs[1]
                #print the quotient of the two numbers
                if quotient < 1:
                    print(Fore.CYAN + Style.BRIGHT + "\nThe quotient is", Fore.WHITE + Style.NORMAL + format(quotient, ".3f"))
                else:
                    print(Fore.CYAN + Style.BRIGHT + "\nThe quotient is", Fore.WHITE + Style.NORMAL + format(quotient, ".2f"))
            #if there's an error detected, except block will be executed
            except ZeroDivisionError:
                print("\n" +
                        boxen(
                            "Invalid Input. Second number cannot be 0. Please enter again.",
                            color="cyan",
                        )
                    )               
            else:
                break
