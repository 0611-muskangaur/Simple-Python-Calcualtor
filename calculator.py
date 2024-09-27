def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b 

def multiply(a, b):
    return a * b 

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b 

def floorDivide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a // b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a % b

def calculator():
    print("Select Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor Division")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6): ")
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter First Number: "))
                num2 = float(input("Enter Second Number: "))
            except ValueError:
                print("Invalid Input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '6':
                print(f"{num1} // {num2} = {floorDivide(num1, num2)}")
        else:
            print("Invalid Input! Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
