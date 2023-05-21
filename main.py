# import class
from calculator import CalculatorOop

# import tkinter library
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# open a window using tkinter
root_window = Tk()
root_window.title("OOP CALCULATOR")
root_window.geometry("400x400")
root_window.config(bg = "yellow")

# create buttons and labels
note_1 = Label(root_window, text = "Enter first number:", bg = "yellow", font = ("Times", 15), justify = CENTER) # label for first num
note_1.place(x=10, y=10)
number_1 = Entry(root_window, font=("Segoe Script",10), justify = CENTER) # entry box for first num
number_1.place(x=170, y=10)

# call methods
# display output

mainloop()
# end program
