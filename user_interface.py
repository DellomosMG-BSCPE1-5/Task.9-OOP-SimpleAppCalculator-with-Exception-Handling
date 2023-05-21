from art import *
from colorama import Fore, Back, Style
from pyboxen import boxen

class UserInterface:

    def title(self):
        #title
        program_title = text2art("  CALCULATE  IT!  ", font='tarty1', chr_ignore=True)
        print(Fore.CYAN + program_title)

    def header(self):
        #header
        print('\n' +
                boxen(
                    "  Welcome to Calculate it! A calculator for every need, accuracy at your fingertips.  ",
                    color="cyan",
                    padding = (0,4,0,4)
                )
            )

    def menu(self):
        while True:
            print("\nOPTIONS: \n\t[1] Addition, \n\t[2] Subtraction, \n\t[3] Multiplication, \n\t[4] Division")
            try:
                #under the menu method, ask the user what operation he/she wants to use
                operation = int(input("\tKindly enter the number that corresponds to the operation you want to perform: "))
                #if the input is among number 1-4, then return operation
                if operation in range (1,5):
                    return operation
                #else, if the input is not belong to numbers from 1-4, then notify the user
                else:
                    print("\n\tInvalid Input. Please enter a number from 1-4 only.")
            #if there's another error detected, except block will be executed
            except (ValueError, TypeError):
                print("\n\tInvalid Input. Please enter a numeric character.")
    
        #create a method for the user input
    def get_numbers(self):
        while True:
            try:
                #under the user input method, ask user for the first number
                first_number = float(input("\n\tEnter first number: "))
                #ask user for the second number
                second_number = float(input("\tEnter second number: "))
                #return the first and second inputs
                return (first_number, second_number)
            #if there's an error detected, except block will be executed
            except (ValueError, TypeError):
                print("\n\tInvalid Input. Please enter a numeric character.")