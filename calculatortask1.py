# Python GUI Calculator
# BY Ssemuhungu Emmanuel

import tkinter as tk
from tkinter import messagebox

# Function to handle button clicks  in their order
def click(button_text):
    """Append clicked button to the entry"""
    entry_var.set(entry_var.get() + button_text)

# Function to clear the entry
def clear():
    """Clear the calculator display"""
    entry_var.set("")

# Function to calculate the result
def calculate():
    """Evaluate the expression in the entry"""
    try:
        # Evaluate the mathematical expression
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except ZeroDivisionError:
        entry_var.set("Error: Division by zero")
    except:
        entry_var.set("Error: Invalid input")

# Function to show about information
def show_about():
    """Show a friendly about message"""
    messagebox.showinfo("About", "Simple Python GUI Calculator\nAuthor: Your Name\nEnjoy calculating!")

# Creating main window
root = tk.Tk()
root.title("Simple GUI Calculator")
root.geometry("320x450")  # Slightly bigger window

# Variable to store entry text
entry_var = tk.StringVar()

# Entry widget where numbers and expressions are shown
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

# Define the button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "About"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)  # Frame for each row
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        if btn_text == "=":
            btn = tk.Button(frame, text=btn_text, font=("Arial", 18), command=calculate)
        elif btn_text == "C":
            btn = tk.Button(frame, text=btn_text, font=("Arial", 18), command=clear)
        elif btn_text == "About":
            btn = tk.Button(frame, text=btn_text, font=("Arial", 18), command=show_about)
        else:
            btn = tk.Button(frame, text=btn_text, font=("Arial", 18), command=lambda x=btn_text: click(x))
        btn.pack(side="left", expand=True, fill="both")

# Friendly welcome message
messagebox.showinfo("Welcome", "Welcome to Simple GUI Calculator!\nYou can perform +, -, *, / operations.")

# Run the main application loop
root.mainloop()