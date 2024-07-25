import tkinter as tk
from tkinter import messagebox
import math

# Function to handle multiplication
def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for multiplication.")

# Function to handle modulus
def calculate_modulus():
    try:
        dividend = float(entry_dividend.get())
        divisor = float(entry_divisor.get())
        result = dividend % divisor
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for modulus calculation.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is undefined.")

# Function to handle logarithm
def calculate_logarithm():
    try:
        base = float(entry_base.get())
        number = float(entry_number.get())
        result = math.log(number, base)
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for logarithm calculation.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input for logarithm calculation. Base must be > 0 and != 1; number must be > 0.")

# Function to handle exponentiation
def calculate_exponent():
    try:
        base_exp = float(entry_base_exp.get())
        exponent = float(entry_exponent.get())
        result = base_exp ** exponent
        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers for exponentiation.")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create input fields and labels
label_num1 = tk.Label(root, text="Number1:")
entry_num1 = tk.Entry(root)

label_num2 = tk.Label(root, text="Number2:")
entry_num2 = tk.Entry(root)

label_dividend = tk.Label(root, text="Dividend:")
entry_dividend = tk.Entry(root)

label_divisor = tk.Label(root, text="Divisor:")
entry_divisor = tk.Entry(root)

label_base = tk.Label(root, text="Base:")
entry_base = tk.Entry(root)

label_number = tk.Label(root, text="Number (log X):")
entry_number = tk.Entry(root)

label_base_exp = tk.Label(root, text="Base Exponent:")
entry_base_exp = tk.Entry(root)

label_exponent = tk.Label(root, text="Exponent:")
entry_exponent = tk.Entry(root)

# Create buttons
button_multiply = tk.Button(root, text="Multiply", command=multiply)
button_modulus = tk.Button(root, text="Modulus", command=calculate_modulus)
button_logarithm = tk.Button(root, text="Logarithm", command=calculate_logarithm)
button_exponent = tk.Button(root, text="Exponential", command=calculate_exponent)

# Create result label
label_result = tk.Label(root, text="Result:")

# Arrange widgets using grid layout
label_num1.grid(row=0, column=0, sticky="e")
entry_num1.grid(row=0, column=1)

label_num2.grid(row=1, column=0, sticky="e")
entry_num2.grid(row=1, column=1)

label_dividend.grid(row=2, column=0, sticky="e")
entry_dividend.grid(row=2, column=1)

label_divisor.grid(row=3, column=0, sticky="e")
entry_divisor.grid(row=3, column=1)

label_base.grid(row=4, column=0, sticky="e")
entry_base.grid(row=4, column=1)

label_number.grid(row=5, column=0, sticky="e")
entry_number.grid(row=5, column=1)

label_base_exp.grid(row=6, column=0, sticky="e")
entry_base_exp.grid(row=6, column=1)

label_exponent.grid(row=7, column=0, sticky="e")
entry_exponent.grid(row=7, column=1)

button_multiply.grid(row=8, column=0, columnspan=2)
button_modulus.grid(row=8, column=2, columnspan=2)
button_logarithm.grid(row=9, column=0, columnspan=2)
button_exponent.grid(row=9, column=2, columnspan=2)

label_result.grid(row=10, column=0, columnspan=4)

# Start the GUI event loop
root.mainloop()
