# Function to perform the chosen arithmetic operation
def calculate(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        return num1 / num2
    else:
        return "Invalid operation"

# Main program
def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter choice (1/2/3/4): ")

    # Prompt the user to input two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the calculation and display the result
    result = calculate(num1, num2, operation)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
