print(" Simple Python Calculator")

try:

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    
    operation = input("Enter operation (+, -, *, /): ")

    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            result = "Error: Cannot divide by zero!"
        else:
            result = num1 / num2
    else:
        result = "Invalid operation!"

    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")
