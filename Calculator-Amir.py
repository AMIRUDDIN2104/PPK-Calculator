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

def calculate_exponent(base, exponent):
    return base **

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

#exponent
base_exp = float(input("\nEnter base exponent: "))
exponent = float(input("Enter exponent number: "))
print(base_exp ** exponent)