# import class
from calculator import CalculatorOop

# call methods
def main():
    compute = CalculatorOop()
    compute.addition(number_1 + number_2)


# import tkinter library
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# open a window using tkinter
root_window = Tk()
root_window.title("OOP CALCULATOR")
root_window.geometry("400x400+800+350")
root_window.config(bg = "yellow")

# create entry box and labels
note_1 = Label(root_window, text = "Enter first number:", bg = "yellow", font = ("Times", 15), justify = CENTER) # label for first num
note_1.place(x=10, y=10)
number_1 = Entry(root_window, font=("Segoe Script",10), justify = CENTER) # entry box for first num
number_1.place(x=170, y=10)

note_2 = Label(root_window, text = "Enter second number:", bg = "yellow", font = ("Times", 15), justify = CENTER) # label for second num
note_2.place(x=10, y=40)
number_2 = Entry(root_window, font=("Segoe Script",10), justify = CENTER) # entry box for second num
number_2.place(x=190, y=40)

#create buttons
# addition button
add_button = Button(root_window, text = "ADD", width = 20, command = main)
add_button.place(x=30, y=90)

# display output

mainloop()
# end program
