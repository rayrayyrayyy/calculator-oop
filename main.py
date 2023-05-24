# import modules for design
from colorama import Fore, Back, Style
import time

# import class
from class_and_functions import CalculatorOop
from intro_outro import IntroOutro

# create objects
compute = CalculatorOop()
welcome_bye = IntroOutro() 

welcome_bye.intro() # call intro

operation_choices = input("Operation: " + Fore.BLUE)
if operation_choices == "+":
    compute.addition() # call function addition
    compute.compute_again() # call compute again function

elif operation_choices == "-":
    compute.subtraction() # call function subtraction
elif operation_choices == "*":
    compute.multiplication() # call function multiplication
elif operation_choices == "/":
    compute.division() # call function division
else:
    print(Fore.RED + Style.BRIGHT + "\nERROR: Please input valid operations only ( +, -, *, / ).\n" + Style.RESET_ALL)

time.sleep(1)
welcome_bye.outro() # call outro
    
# end program