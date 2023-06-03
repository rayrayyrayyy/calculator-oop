# import
from intro_outro import IntroOutro
from class_and_functions import CalculatorOop
import pyfiglet
from colorama import Fore, Back, Style

# call class
class CalculatorRay(IntroOutro, CalculatorOop):
    def intro(self):
        # intro message
        hi_welcome = pyfiglet.figlet_format("Welcome User!", font = "doom", width = 150, justify = "center")
        print(Fore.YELLOW + hi_welcome)
        print(Style.RESET_ALL)
        print(Fore.MAGENTA + "="*150)
        print(Style.RESET_ALL)
        instruction = "INSTRUCTION: Please choose an operation you would like to use ( +, -, *, / )."
        instruction_center = instruction.center(150)
        print(instruction_center)
        print('\n' + Fore.MAGENTA + "="*150)
        print(Style.RESET_ALL)

    def outro(self):
        # outro message
        print('\n' + Fore.MAGENTA + Style.BRIGHT + "="*150 + Style.RESET_ALL)
        done = pyfiglet.figlet_format("Thank you!", font = 'doom', width = 150, justify = 'center')
        print(Fore.YELLOW + done)
        print(Fore.MAGENTA + '='*69 + Style.RESET_ALL + "Have a great day!" + Fore.MAGENTA + '='*69 + '\n') 
