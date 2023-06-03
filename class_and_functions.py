# Ray Allessandra Pacis | BSCPE 1-5

# import modules for design
from colorama import Fore, Back, Style
import time
import pyfiglet

from user_input import UserInput

class_input = UserInput()
first_num = class_input.ask_user()
second_num = class_input.ask_user()

# create class for calculator
class CalculatorOop:
    # define addition function
    def addition(self):
        add_note = pyfiglet.figlet_format("ADDITION", font = "big", width = 150, justify = "center")
        print(Fore.LIGHTMAGENTA_EX + add_note)

        sum = first_num + second_num
        time.sleep(1)
        print("\nRESULT: " + Fore.BLUE + str(sum) + Style.RESET_ALL)

    # define subtraction function
    def subtraction(self):
        sub_note = pyfiglet.figlet_format("SUBTRACTION", font = "big", width = 150, justify = "center")
        print(Fore.LIGHTMAGENTA_EX + sub_note)

        difference = first_num - second_num
        time.sleep(1)
        print("\nRESULT: " + Fore.BLUE + str(difference) + Style.RESET_ALL)
        
    # define multiplication function
    def multiplication(self):
        mul_note = pyfiglet.figlet_format("MULTIPLICATION", font = "big", width = 150, justify = "center")
        print(Fore.LIGHTMAGENTA_EX + mul_note)

        product = first_num * second_num
        time.sleep(1)
        print("\nRESULT: " + Fore.BLUE + str(product) + Style.RESET_ALL)

    # define division function
    def division(self):
        div_note = pyfiglet.figlet_format("DIVISION", font = "big", width = 150, justify = "center")
        print(Fore.LIGHTMAGENTA_EX + div_note)
        try:
            quotient = first_num / second_num
            time.sleep(1)
            print("\nRESULT: " + Fore.BLUE + str(quotient) + Style.RESET_ALL)
        except ZeroDivisionError:
            print(Fore.RED + Style.BRIGHT + "\nERROR: Division by zero is not allowed.\n" + Style.RESET_ALL)
        except: 
            print(Fore.RED + Style.BRIGHT + "\nINVALID INPUT." + Style.RESET_ALL)