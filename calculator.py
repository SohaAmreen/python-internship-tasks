
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    print("=== Simple Calculator ===")
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        print("\nChoose operation:")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        else:
            print("Invalid choice.")
            continue

        print("Result:", result)

        again = input("\nCalculate again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break

main()
