import math
import sys

class AdvancedCalculator:
    def __init__(self):
        self.memory = 0
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def power(self, a, b):
        result = math.pow(a, b)
        self.history.append(f"{a} ^ {b} = {result}")
        return result
    
    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        result = math.sqrt(a)
        self.history.append(f"√{a} = {result}")
        return result
    
    def sin(self, a, degrees=False):
        if degrees:
            a = math.radians(a)
        result = math.sin(a)
        self.history.append(f"sin({a}) = {result}")
        return result
    
    def cos(self, a, degrees=False):
        if degrees:
            a = math.radians(a)
        result = math.cos(a)
        self.history.append(f"cos({a}) = {result}")
        return result
    
    def tan(self, a, degrees=False):
        if degrees:
            a = math.radians(a)
        result = math.tan(a)
        self.history.append(f"tan({a}) = {result}")
        return result
    
    def log(self, a, base=math.e):
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        result = math.log(a, base)
        self.history.append(f"log_{base}({a}) = {result}")
        return result
    
    def factorial(self, a):
        if a < 0:
            raise ValueError("Factorial undefined for negative numbers")
        result = math.factorial(int(a))
        self.history.append(f"{a}! = {result}")
        return result
    
    def memory_add(self, value):
        self.memory += value
        return self.memory
    
    def memory_subtract(self, value):
        self.memory -= value
        return self.memory
    
    def memory_clear(self):
        self.memory = 0
    
    def memory_recall(self):
        return self.memory
    
    def show_history(self):
        for entry in self.history:
            print(entry)
    
    def clear_history(self):
        self.history = []

def display_menu():
    print("\nAdvanced Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Factorial")
    print("12. Memory Operations")
    print("13. Show History")
    print("14. Clear History")
    print("0. Exit")

def memory_menu():
    print("\nMemory Operations:")
    print("1. Add to Memory")
    print("2. Subtract from Memory")
    print("3. Clear Memory")
    print("4. Recall Memory")
    print("0. Back to Main Menu")

def main():
    calc = AdvancedCalculator()
    
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if choice == 0:
            print("Exiting calculator. Goodbye!")
            sys.exit()
        
        elif choice == 1:  # Addition
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.add(a, b)}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == 2:  # Subtraction
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.subtract(a, b)}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == 3:  # Multiplication
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.multiply(a, b)}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == 4:  # Division
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print(f"Result: {calc.divide(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero")
        
        elif choice == 5:  # Power
            try:
                a = float(input("Enter base: "))
                b = float(input("Enter exponent: "))
                print(f"Result: {calc.power(a, b)}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == 6:  # Square Root
            try:
                a = float(input("Enter number: "))
                print(f"Result: {calc.sqrt(a)}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == 7:  # Sine
            try:
                a = float(input("Enter angle: "))
                deg = input("Is this in degrees? (y/n): ").lower() == 'y'
                print(f"Result: {calc.sin(a, deg)}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == 8:  # Cosine
            try:
                a = float(input("Enter angle: "))
                deg = input("Is this in degrees? (y/n): ").lower() == 'y'
                print(f"Result: {calc.cos(a, deg)}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == 9:  # Tangent
            try:
                a = float(input("Enter angle: "))
                deg = input("Is this in degrees? (y/n): ").lower() == 'y'
                print(f"Result: {calc.tan(a, deg)}")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        elif choice == 10:  # Logarithm
            try:
                a = float(input("Enter number: "))
                base = input("Enter base (leave blank for natural log): ")
                if base:
                    base = float(base)
                    print(f"Result: {calc.log(a, base)}")
                else:
                    print(f"Result: {calc.log(a)}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == 11:  # Factorial
            try:
                a = float(input("Enter number: "))
                print(f"Result: {calc.factorial(a)}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == 12:  # Memory Operations
            while True:
                memory_menu()
                try:
                    mem_choice = int(input("Enter memory operation choice: "))
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                
                if mem_choice == 0:
                    break
                elif mem_choice == 1:  # Add to memory
                    try:
                        value = float(input("Enter value to add to memory: "))
                        print(f"Memory value: {calc.memory_add(value)}")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                elif mem_choice == 2:  # Subtract from memory
                    try:
                        value = float(input("Enter value to subtract from memory: "))
                        print(f"Memory value: {calc.memory_subtract(value)}")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                elif mem_choice == 3:  # Clear memory
                    calc.memory_clear()
                    print("Memory cleared.")
                elif mem_choice == 4:  # Recall memory
                    print(f"Memory value: {calc.memory_recall()}")
                else:
                    print("Invalid choice. Please try again.")
        
        elif choice == 13:  # Show History
            calc.show_history()
        
        elif choice == 14:  # Clear History
            calc.clear_history()
            print("History cleared.")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
