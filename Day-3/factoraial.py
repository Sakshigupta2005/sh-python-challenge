#python program to find its factoral number

num =int(input("enter a number to find its factorial:"))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")