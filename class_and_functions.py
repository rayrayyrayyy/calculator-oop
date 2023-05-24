# Ray Allessandra Pacis | BSCPE 1-5

# import modules for design
from colorama import Fore, Back, Style
import time
import pyfiglet

# create class for calculator
class CalculatorOop:
    # define addition function
    def addition(self):
        add_note = pyfiglet.figlet_format("ADDITION", font = "big", width = 150, justify = "center")
        print(Fore.LIGHTMAGENTA_EX + add_note)

        first_num = float(input('\033[1;35m' + "\nEnter first number: \033[0m"))
        second_num = float(input('\033[1;35m' + "Enter second number: \033[0m"))
        sum = first_num + second_num
        time.sleep(1)
        print("\nRESULT: " + Fore.BLUE + str(sum) + Style.RESET_ALL)

    # define subtraction function
    def subtraction(self):
        sub_note = pyfiglet.figlet_format("SUBTRACTION", font = "big", width = 150, justify = "center")
        print(Fore.LIGHTMAGENTA_EX + sub_note)

        first_num = float(input('\033[1;35m' + "\nEnter first number: \033[0m"))
        second_num = float(input('\033[1;35m' + "Enter second number: \033[0m"))
        difference = first_num - second_num
        time.sleep(1)
        print("\nRESULT: " + Fore.BLUE + str(difference) + Style.RESET_ALL)
        
    # define multiplication function
    def multiplication(self):
        mul_note = pyfiglet.figlet_format("MULTIPLICATION", font = "big", width = 150, justify = "center")
        print(Fore.LIGHTMAGENTA_EX + mul_note)

        first_num = float(input('\033[1;35m' + "\nEnter first number: \033[0m"))
        second_num = float(input('\033[1;35m' + "Enter second number: \033[0m"))
        product = first_num * second_num
        time.sleep(1)
        print("\nRESULT: " + Fore.BLUE + str(product) + Style.RESET_ALL)

    # define division function
    def division(self):
        div_note = pyfiglet.figlet_format("DIVISION", font = "big", width = 150, justify = "center")
        print(Fore.LIGHTMAGENTA_EX + div_note)
        try:
            first_num = float(input('\033[1;35m' + "\nEnter first number: \033[0m"))
            second_num = float(input('\033[1;35m' + "Enter second number: \033[0m"))
            quotient = first_num / second_num
            time.sleep(1)
            print("\nRESULT: " + Fore.BLUE + str(quotient) + Style.RESET_ALL)
        except ZeroDivisionError:
            print(Fore.RED + Style.BRIGHT + "\nERROR: Division by zero is not allowed.\n" + Style.RESET_ALL)
        except: 
            print(Fore.RED + Style.BRIGHT + "\nINVALID INPUT." + Style.RESET_ALL)