#code by Asyraf
#Add
#Subtract
#Divide
def add(a, b):
    return a + b

def subtract (a, b):
    return a - b

def divide (a, b):
    if b != 0:
        return a / b    
    else:
        return "Error: Cannot divide by zero"
              
while True:
    
    print("Select an operation to perform:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Exit Calculator")

    choice = input ("Choose the option (1 - 4): ")

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
    else:
        break    
        
#code end here by Asyraf