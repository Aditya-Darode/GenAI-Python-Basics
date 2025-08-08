# Simple Calculator Program using Python

try:
    # Taking first number as input from the user
    a = int(input("Enter the number: "))

    # Taking second number as input from the user
    b = int(input("Enter the number: "))

    # Asking the user for the type of operation they want to perform
    print("What kind of operation do you want to perform?")
    print("Press + for addition")
    print("Press - for subtraction")
    print("Press / for division")
    print("Press * for multiplication")

    # Reading the operation choice
    o = input("Enter Operation: ")

    # Using match-case for selecting the operation (Python 3.10+ feature)
    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "/":
            print(f"The result is: {a / b}")
        case "*":
            print(f"The result is: {a * b}")
        case default:  # Default case for invalid operation
            print("Invalid operation selected.")

# Handling exceptions if user enters non-integer values or division by zero
except Exception as e:
    print("Enter a valid value of a and b")
