# Ray Allessandra Pacis | BSCPE 1-5

#import modules for design 
import pyfiglet
from colorama import Fore, Back, Style

# create class for calculator
class CalculatorOop:
    # define addition function
    def addition(self):
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        sum = first_num + second_num
        print(sum)

    # define subtraction function
    def subtraction(self):
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        difference = first_num - second_num
        print(difference)
        
    # define multiplication function
    def multiplication(self):
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        product = first_num * second_num
        print(product)

    # define division function
    def division(self):
        first_num = float(input("Enter first number: "))
        second_num = float(input("Enter second number: "))
        quotient = first_num / second_num
        print(quotient)