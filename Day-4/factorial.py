#python program factorial 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial of 5
print("Factorial of 5:", factorial(5))