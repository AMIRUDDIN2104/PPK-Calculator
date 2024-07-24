# python code by amir
# calculator
# multiply/modulus/logs/exponential

import math

def multiply(num1, num2):
    return num1 * num2

def calculate_modulus(dividend, divisor):
    return dividend % divisor

#multiplication
num1 = float(input("Enter Number1 for multiplication: "))
num2 = float(input("Enter Number2 for multiplication: "))
print(num1 * num2)

#modulus
dividend = float(input("\nEnter dividend number: "))
divisor = float(input("Enter divisor: "))
print(dividend % divisor)