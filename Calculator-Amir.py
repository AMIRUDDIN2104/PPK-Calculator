# Python code by Amir
# Scientific Calculator
# Multiply/Modulus/Logs/Exponential

import math

def multiply(num1, num2):
    return num1 * num2

def calculate_modulus(dividend, divisor):
    try:
        return dividend % divisor
    except ZeroDivisionError:
        return "Error: Division by zero is undefined."

def calculate_logarithm(base, number):
    if base > 0 and base != 1 and number > 0:
        return math.log(number, base)
    else:
        return "Error: Invalid input for logarithm calculation. Base must be > 0 and != 1; number must be > 0."

def calculate_exponent(base, exponent):
    return base ** exponent

while True:
    print("\nSelect an operation (or type 'stop' to exit):")
    print("1. Multiply")
    print("2. Modulus")
    print("3. Logarithm")
    print("4. Exponential")

    operation = input("Enter the operation number (1/2/3/4) or 'stostop': ").strip().lower()

    if operation == "stop":
        print("Exiting calculator.")
        break

    if operation == "1":
        try:
            num1 = float(input("Enter Number1 for multiplication: "))
            num2 = float(input("Enter Number2 for multiplication: "))
            result = multiply(num1, num2)
            print(f"Result: {result}")
        except ValueError:
            print("Error > enter valid numbers for multiplication.")

    elif operation == "2":
        try:
            dividend = float(input("Enter dividend number: "))
            divisor = float(input("Enter divisor: "))
            result = calculate_modulus(dividend, divisor)
            print(f"Result: {result}")
        except ValueError:
            print("Error > enter valid numbers for modulus calculation.")

    elif operation == "3":
        try:
            base = float(input("Enter base: "))
            number = float(input("Enter number (log X): "))
            result = calculate_logarithm(base, number)
            print(f"Result: {result}")
        except ValueError:
            print("Error > enter valid numbers for logarithm calculation.")

    elif operation == "4":
        try:
            base_exp = float(input("Enter base exponent: "))
            exponent = float(input("Enter exponent number: "))
            result = calculate_exponent(base_exp, exponent)
            print(f"Result: {result}")
        except ValueError:
            print("Error > enter valid numbers for exponentiation.")

    else:
        print("Invalid input. Please select a valid operation (1/2/3/4) or stop to exit calculator.")

# end code - Amir
