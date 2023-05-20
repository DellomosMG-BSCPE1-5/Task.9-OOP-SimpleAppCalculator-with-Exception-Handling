#Redo calculator program applying the OOP concept.

#pseudocode for the class file
#create a file for the calculator class that contains necessary methods

#for the class file, create a class named Calculator
class Calculator:

    #under the Calculator class, create a method for the menu
    def menu(self):
        #under the menu method, ask the user what operation he/she wants to use
        print("OPTIONS: \n\t[1] Addition, \n\t[2] Subtraction, \n\t[3] Multiplication, \n\t[4] Division")
        operation = int(input("\nKindly enter the number that corresponds to the operation you want to perform: "))
        #return operation
        return operation
    
    #create a method for the user input
    def get_numbers(self):
        #under the user input method, ask user for the first number
        first_number = float(input("\n\tEnter first number: "))
        #under the user input method, ask user for the second number
        second_number = float(input("\tEnter second number: "))
        #return the first and second inputs
        return (first_number, second_number)

    #create method for addition operation
    def addition(self):
        #under the addition method, perform the addition operation on two numbers
        sum = first_number + second_number
        #return the sum of the two numbers
        return sum
        
#create method for subtraction operation
#under the subtraction method, perform the subtraction operation on two numbers
#return the difference of the two numbers
#create method for multiplication operation
#under the multiplication method, perform the multiplication operation on two numbers
#return the product of the two numbers
#create method for division operation
#under the division method, perform the division operation on two numbers
#insert exception handling (ZeroDivisionError) incase the zero number is equal to zero
#call the user input method to ask for user's input again. This time, the second number should not be equal to zero again.
#return the product of the two numbers if the first and second numbers are valid and successfully obtained their quotient
