def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  #
    return result
while True:
    try:
        num = int(input("Enter a number: "))
        print(f"Factorial of {num}: {factorial_iterative(num)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")