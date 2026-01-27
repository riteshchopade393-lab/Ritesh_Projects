history = []

def addition(a, b):
    result = a + b
    history.append(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    result = a - b
    history.append(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    result = a * b
    history.append(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    result = a / b
    history.append(f"{a} / {b} = {result}")
    return result

# History Functions

def show_history():
    if not history:
        print("No calculation done yet")
    else:
        print("\n Calculation history")
        for item in history:
            print(item)

def export_history():
    if not history:
        print("No history to export.")
        return
    
    with open("calculator_history.txt", "w") as f:
        for item in history:
            f.write(item + "\n")
        
    print("History exported to calculator_history.txt")

# Main program

while True:
    print("\n---Calculation Menu---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Export History")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice in ["1", "2", "3", "4"]:
        a = float(input("Enter a number: "))
        b = float(input("Enter the second number: "))

        if choice == "1":
            print("Result: ", addition(a, b))

        elif choice == "2":
            print("Result: ", subtract(a, b))

        elif choice == "3":
            print("Result: ", multiply(a, b))

        elif choice == "4":
            print("Result: ", divide(a, b))

    elif choice == "5":
        show_history()

    elif choice == "6":
        export_history()

    elif choice == "7":
        print("Exisiting Calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


        

