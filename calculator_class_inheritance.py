#import modules
from art import *
from colorama import Fore, Back, Style
from pyboxen import boxen


#imports class Calculator and class UserInterface
from calculator_class import Calculator
from user_interface import UserInterface

#create class that inherits the methods of class Calculator and class UserInterface
class CalculatorAppend(UserInterface, Calculator):
        
        #Override the Menu method of class UserInterface adding the Exponent Operation in the menu.
        def menu(self):
            while True:
                print(Fore.CYAN + Style.NORMAL + "OPTIONS:", Fore.WHITE + Style.NORMAL + "=" * 86, "\n[1] Addition \n[2] Subtraction \n[3] Multiplication \n[4] Division \n[5]Exponent\n" + "=" * 95)
                try:
                    #under the menu method, ask the user what operation he/she wants to use
                    print(Fore.LIGHTCYAN_EX + Style.NORMAL + "\nKindly enter the number that corresponds to the operation you want to perform: ", end = "")
                    operation = float(input(Fore.WHITE + ""))     
                    #if the input is among number 1-4, then return operation
                    if operation in range (1,6):
                        return operation
                    #else, if the input is not belong to numbers from 1-4, then notify the user
                    else:
                        print('\n' +
                                boxen(
                                    "  Invalid Input. Please enter a number from 1-5 only. ",
                                    color="cyan",
                                    padding = (0,7,0,7)
                                )
                            )                 
                #if there's another error detected, except block will be executed
                except (ValueError, TypeError):
                    print('\n' +
                            boxen(
                                "  Invalid Input. Please enter a numeric character. ",
                                color="cyan",
                                padding = (0,7,0,7)
                            )
                        )   