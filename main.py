# import modules for design
from colorama import Fore, Back, Style

# import class
from class_and_functions import CalculatorOop
from intro_outro import IntroOutro

compute = CalculatorOop()

operation_choices = input("Operation: ")
if operation_choices == "+":
    compute.addition() # call function addition
elif operation_choices == "-":
    compute.subtraction() # call function subtraction
elif operation_choices == "*":
    compute.multiplication() # call function multiplication
elif operation_choices == "/":
    compute.division() # call function division
else:
    print(Fore.RED + Style.BRIGHT + "\nERROR: Please input valid operations only ( +, -, *, / ).\n" + Style.RESET_ALL)
    
# end program