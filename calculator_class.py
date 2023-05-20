#Redo calculator program applying the OOP concept.

#pseudocode for the class file
#create a file for the calculator class that contains necessary methods

#for the class file, create a class named Calculator
class Calculator:

    #under the Calculator class, create a method for the menu
    def menu(self):
        while True:
            try:
                #under the menu method, ask the user what operation he/she wants to use
                print("OPTIONS: \n\t[1] Addition, \n\t[2] Subtraction, \n\t[3] Multiplication, \n\t[4] Division")
                operation = int(input("\nKindly enter the number that corresponds to the operation you want to perform: "))
                #if the input is among number 1-4,
                if operation in range (1,5):
                    #then return operation
                    return operation
                #else, if the input is not belong to numbers from 1-4,
                else:
                    #then
                    print("\n\tInvalid Input. Please enter a number from 1-4 only.")
            #if there's an error detected, except block will be executed
            except (ValueError, TypeError):
                print("\n\tInvalid Input. Please enter a numeric character.")

    #create a method for the user input
    def get_numbers(self):
        while True:
            try:
                #under the user input method, ask user for the first number
                first_number = float(input("\n\tEnter first number: "))
                #under the user input method, ask user for the second number
                second_number = float(input("\tEnter second number: "))
                #return the first and second inputs
                return (first_number, second_number)
            #if there's an error detected, except block will be executed
            except (ValueError, TypeError):
                print("\n\tInvalid Input. Please enter a numeric character.")

    #create method for addition operation
    def addition(self):
        #under the addition method, call the get_numbers method to get the inputs from user that are needed to perform the operation
        inputs = self.get_numbers()
        #perform the addition operation on two numbers.
        #the 1st number is inputs[0] and the 2nd number is inputs[1]
        sum = inputs[0] + inputs[1]
        #print the sum of the two numbers
        print("\n\tThe sum is " + str(sum))

    #create method for subtraction operation
    def subtraction(self):   
        #under the subtraction method, call the get_numbers method to get the inputs from user that are needed to perform the operation
        inputs = self.get_numbers()
        #perform the subtraction operation on two numbers.
        #the 1st number is inputs[0] and the 2nd number is inputs[1]
        difference = inputs[0] - inputs[1]
        #print the difference of the two numbers
        print("\n\tThe difference is " + str(difference))

    #create method for multiplication operation
    def multiplication(self):
        #under the multiplication method, call the get_numbers method to get the inputs from user that are needed to perform the operation
        inputs = self.get_numbers()
        #perform the multiplication operation on two numbers.
        #the 1st number is inputs[0] and the 2nd number is inputs[1]
        product = inputs[0] * inputs[1]
        #print the product of the two numbers
        print("\n\tThe product is " + str(product))

    #create method for division operation
    def division(self):
        while True:
            try:
                #under the division method, call the get_numbers method to get the inputs from user that are needed to perform the operation
                inputs = self.get_numbers()
                #perform the division operation on two numbers.
                #the 1st number is inputs[0] and the 2nd number is inputs[1]
                quotient = inputs[0] / inputs[1]
                #print the quotient of the two numbers
                if quotient < 1:
                    print("\n\tThe quotient is", format(quotient, ".3f"))
                else:
                    print("\n\tThe quotient is", round(quotient))
            #if there's an error detected, except block will be executed
            except ZeroDivisionError:
                print("\n\tZero Division Error: Second number cannot be 0.")
