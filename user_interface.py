#import the some modules
from art import *
from colorama import Fore, Back, Style
from pyboxen import boxen

#create a class named UserInterface
class UserInterface:
    
    #title method
    def title(self):
        program_title = text2art("  CALCULATE  IT!  ", font='tarty1', chr_ignore=True)
        print(Fore.CYAN + program_title)
        
    #header method
    def header(self):
        print('\n' +
                boxen(
                    "  Welcome to Calculate it! A calculator for every need, accuracy at your fingertips.  ",
                    color="cyan",
                    padding = (0,4,0,4)
                )
            )

    #menu method
    def menu(self):
        while True:
            print(Fore.CYAN + Style.NORMAL + "OPTIONS:", Fore.WHITE + Style.NORMAL + "=" * 86, "\n[1] Addition \n[2] Subtraction \n[3] Multiplication \n[4] Division\n" + "=" * 95)
            try:
                #under the menu method, ask the user what operation he/she wants to use
                print(Fore.LIGHTCYAN_EX + Style.NORMAL + "\nKindly enter the number that corresponds to the operation you want to perform: ", end = "")
                operation = float(input(Fore.WHITE + ""))     
                #if the input is among number 1-4, then return operation
                if operation in range (1,5):
                    return operation
                #else, if the input is not belong to numbers from 1-4, then notify the user
                else:
                    print('\n' +
                            boxen(
                                "  Invalid Input. Please enter a number from 1-4 only. ",
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
                  
    #method for the user input
    def get_numbers(self):
        while True:
            try:
                #under the user input method, ask user for the first number
                first_number = float(input("\nEnter first number: "))
                #ask user for the second number
                second_number = float(input("Enter second number: "))
                #return the first and second inputs
                return (first_number, second_number)
            #if there's an error detected, except block will be executed
            except (ValueError, TypeError):
                print('\n' +
                        boxen(
                            "  Invalid Input. Please enter a numeric character. ",
                            color="cyan",
                            padding = (0,7,0,7)
                        )
                    )       