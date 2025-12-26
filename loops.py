# This file contains examples of using loops in Python.

# Example of a for loop
print("For Loop Example:")
for i in range(5):
    print(f"Iteration {i + 1}: Hello, World!")

# Example of a while loop
print("\nWhile Loop Example:")
count = 0
while count < 5:
    print(f"Iteration {count + 1}: Hello, World!")
    count += 1

# Example of iterating over a list
print("\nIterating Over a List:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}.")