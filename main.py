# import modules for design
from colorama import Fore, Back, Style
import time

# import class
from class_and_functions import CalculatorOop
from intro_outro import IntroOutro
from child_class import CalculatorRay

# create objects
compute = CalculatorOop()
welcome_bye = IntroOutro() 
calculator_ray = CalculatorRay()

calculator_ray.intro() # call intro

operation_choices = input("Operation: " + Fore.BLUE)
if operation_choices == "+":
    calculator_ray.addition() # call function addition
elif operation_choices == "-":
    calculator_ray.subtraction() # call function subtraction
elif operation_choices == "*":
    calculator_ray.multiplication() # call function multiplication
elif operation_choices == "/":
    calculator_ray.division() # call function division
else:
    print(Fore.RED + Style.BRIGHT + "\nERROR: Please input valid operations only ( +, -, *, / ).\n" + Style.RESET_ALL) 

time.sleep(1)
calculator_ray.outro() # call outro
    
# end program