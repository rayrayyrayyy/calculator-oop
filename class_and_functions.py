# Ray Allessandra Pacis | BSCPE 1-5

# import modules for design
from colorama import Fore, Back, Style
import time

# create class for calculator
class CalculatorOop:
    # define addition function
    def addition(self):
        first_num = float(input('\033[1;35m' + "\nEnter first number: \033[0m"))
        second_num = float(input('\033[1;35m' + "Enter second number: \033[0m"))
        sum = first_num + second_num
        time.sleep(2)
        print("\nRESULT: " + Fore.BLUE + str(sum) + Style.RESET_ALL)

    # define subtraction function
    def subtraction(self):
        first_num = float(input('\033[1;35m' + "\nEnter first number: \033[0m"))
        second_num = float(input('\033[1;35m' + "Enter second number: \033[0m"))
        difference = first_num - second_num
        time.sleep(2)
        print("\nRESULT: " + Fore.BLUE + str(difference) + Style.RESET_ALL)
        
    # define multiplication function
    def multiplication(self):
        first_num = float(input('\033[1;35m' + "\nEnter first number: \033[0m"))
        second_num = float(input('\033[1;35m' + "Enter second number: \033[0m"))
        product = first_num * second_num
        time.sleep(2)
        print("\nRESULT: " + Fore.BLUE + str(product) + Style.RESET_ALL)

    # define division function
    def division(self):
        first_num = float(input('\033[1;35m' + "\nEnter first number: \033[0m"))
        second_num = float(input('\033[1;35m' + "Enter second number: \033[0m"))
        quotient = first_num / second_num
        time.sleep(2)
        print("\nRESULT: " + Fore.BLUE + str(quotient) + Style.RESET_ALL)