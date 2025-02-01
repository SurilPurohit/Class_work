class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        if y != 0:
            self.result = x / y
        else:
            return "Error! Division by zero."
        return self.result

    def clear(self):
        self.result = 0
        print("Result cleared.")

    def get_result(self):
        return self.result

def display_menu():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Clear result")
    print("6. Exit")

def main():
    calc = Calculator()
    while True:
        display_menu()
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Exiting calculator.")
            break

        if choice == '5':
            calc.clear()
            continue

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {calc.add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {calc.subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {calc.multiply(num1, num2)}")
            elif choice == '4':
                result = calc.divide(num1, num2)
                if isinstance(result, str):
                    print(result)  # Error message for division by zero
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid input! Please choose a valid operation.")

if __name__ == "__main__":
    main()
