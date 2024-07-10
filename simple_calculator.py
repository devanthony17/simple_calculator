def add(num1, num2):
    """Return the sum of num1 and num2."""
    return num1 + num2

def subtract(num1, num2):
    """Return the difference between num1 and num2."""
    return num1 - num2

def multiply(num1, num2):
    """Return the product of num1 and num2."""
    return num1 * num2

def divide(num1, num2):
    """Return the quotient of num1 divided by num2.
    Raise ValueError if num2 is zero.
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def modulus(num1, num2):
    """Return the remainder of num1 divided by num2."""
    return num1 % num2

def get_number(prompt):
    """Get a number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    """Get a valid operation from the user."""
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide, '%': modulus}
    while True:
        op = input("Choose an operation (+, -, *, /, %): ")
        if op in operations:
            return op, operations[op]
        print("Invalid operation. Please choose from +, -, *, /, %.")

def main():
    print("Welcome to the Simple Calculator")
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        op_symbol, operation = get_operation()

        try:
            result = operation(num1, num2)
            print(f"The result of {num1} {op_symbol} {num2} is: {result}")
        except ValueError as e:
            print(f"Error: {e}")

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
