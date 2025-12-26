def greet(name):
    """Function to greet a person with their name."""
    return f"Hello, {name}!"

def add(a, b):
    """Function to add two numbers."""
    return a + b

def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b

def factorial(n):
    """Function to calculate the factorial of a number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def main():
    """Main function to demonstrate the use of the above functions."""
    print(greet("Student"))
    print(f"5 + 3 = {add(5, 3)}")
    print(f"4 * 7 = {multiply(4, 7)}")
    print(f"Factorial of 5 = {factorial(5)}")

if __name__ == "__main__":
    main()