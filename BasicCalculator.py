# Here, in day1 we are  going to create a basic calculator using python. This calculator will perform basic arithmetic operations like addition, subtraction, multiplication, and division.

def add(x,y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if  y == 0:
        return "Error! Division by zero"
    else:
        return x / y

def calculator():
    print("Welcome to Calculator program")

    while True:
        print("Select Operation")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = input("Enter your choice: ")

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid Input")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != "yes":
            print("Program terminated. Thank you for using the calculator.")
            break


calculator()
