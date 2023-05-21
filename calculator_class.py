#Redo calculator program applying the OOP concept.

#import the UserInterface Class
from user_interface import UserInterface
input = UserInterface()
#for the class file, create a class named Calculator
class Calculator:

    #constructor
    def __init__(self):
        pass

    #create method for addition operation
    def addition(self):
        #under the addition method, call the get_numbers method to get the inputs from user that are needed to perform the operation
        inputs = input.get_numbers()
        #perform the addition operation on two numbers.
        #the 1st number is inputs[0] and the 2nd number is inputs[1]
        sum = inputs[0] + inputs[1]
        #print the sum of the two numbers
        print("\n\tThe sum is " + str(sum))

    #create method for subtraction operation
    def subtraction(self):   
        #under the subtraction method, call the get_numbers method to get the inputs from user that are needed to perform the operation
        inputs = input.get_numbers()
        #perform the subtraction operation on two numbers.
        difference = inputs[0] - inputs[1]
        #print the difference of the two numbers
        print("\n\tThe difference is " + str(difference))

    #create method for multiplication operation
    def multiplication(self):
        #under the multiplication method, call the get_numbers method to get the inputs from user that are needed to perform the operation
        inputs = input.get_numbers()
        #perform the multiplication operation on two numbers.
        product = inputs[0] * inputs[1]
        #print the product of the two numbers
        print("\n\tThe product is " + str(product))

    #create method for division operation
    def division(self):
        while True:
            try:
                #under the division method, call the get_numbers method to get the inputs from user that are needed to perform the operation
                inputs = input.get_numbers()
                #perform the division operation on two numbers.
                quotient = inputs[0] / inputs[1]
                #print the quotient of the two numbers
                if quotient < 1:
                    print("\n\tThe quotient is", format(quotient, ".3f"))
                else:
                    print("\n\tThe quotient is", format(quotient, ".2f"))
            #if there's an error detected, except block will be executed
            except ZeroDivisionError:
                print("\n\tZero Division Error: Second number cannot be 0. Please enter again.")
            else:
                break
