#import modules for design 
import pyfiglet
from colorama import Fore, Back, Style

class IntroOutro:
    def intro(self):
        # intro message
        hi_welcome = pyfiglet.figlet_format("Welcome User!", font = "doom", width = 150, justify = "center")
        print(Fore.MAGENTA + hi_welcome)
        print(Style.RESET_ALL)
        print(Fore.BLUE + "="*150)
        print(Style.RESET_ALL)
        instruction = "INSTRUCTION: Please choose an operation you would like to use ( +, -, *, / )."
        instruction_center = instruction.center(150)
        print(instruction_center)
        print('\n' + Fore.BLUE + "="*150)
        print(Style.RESET_ALL)

    def outro(self):
        # outro message
        print('\n' + Fore.BLUE + Style.BRIGHT + "="*150 + Style.RESET_ALL)
        done = pyfiglet.figlet_format("Thank you!", font = 'doom', width = 150, justify = 'center')
        print(Fore.MAGENTA + done)
        print(Fore.BLUE + '='*69 + Style.RESET_ALL + "Have a great day!" + Fore.BLUE + '='*69 + '\n') 