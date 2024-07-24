# python code by amir
# calculator
# multiply/modulus/logs/exponential

import math

def multiply(num1, num2):
    return num1 * num2

def calculate_modulus(dividend, divisor):
    return dividend % divisor

def calculate_logarithm(base, number):
    return math.log(number, base)

#multiplication
num1 = float(input("Enter Number1 for multiplication: "))
num2 = float(input("Enter Number2 for multiplication: "))
print(num1 * num2)

#modulus
dividend = float(input("\nEnter dividend number: "))
divisor = float(input("Enter divisor: "))
print(dividend % divisor)

#logs
base = float(input("\nEnter base: "))
number = float(input("Enter number (log X): "))
print(math.log(number, base))