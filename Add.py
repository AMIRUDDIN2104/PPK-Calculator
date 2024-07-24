#code by Asyraf
#Add
#Subtract
#Divide
def add(a, b):
        return a + b

def subtract (a, b):
        return a - b

def divide (a, b):
        return a / b

print("Select an operation to perform:")
print("1. Add")

while True:

    choice = input ("Choose the option (1/2/3): ")

    if choice in ('1', '2', '3'):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

#addition
    if choice == '1':
        print(num1, "+", num2, "=",add(num1, num2))

#subtraction
    elif choice == '2':
         print(num1, "-", num2, "=",subtract(num1, num2))

#division
    elif choice == '3':
        print(num1, "/", num2, "=",divide(num1, num2))

    else:
        print("Invalid Input")

    break
#code end here by Asyraf