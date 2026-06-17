# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

# Function to calculate factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Main program
numbers = [3, 6, 9, 12]

for num in numbers:
    print(check_even_odd(num))
    print(f"Factorial of {num} = {factorial(num)}")
    print("-" * 30)

