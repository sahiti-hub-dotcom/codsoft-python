def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Simple Calculator")
    print("=================")
    
    # Prompt the user to input two numbers
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    
    # Prompt the user to choose an operation
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        choice = input("\nEnter your choice (1/2/3/4): ")
        
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice! Please select a valid operation.")
    
    # Perform the calculation based on the user's choice
    if choice == '1':
        result = add(num1, num2)
        operation = "Addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "Subtraction"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "Multiplication"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "Division"
    
    # Display the result
    print(f"\n{operation} of {num1} and {num2} = {result}")

if __name__ == "__main__":
    main()
