def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

while True:
    try:
        num = int(input("Enter a number: "))
        print(f"Factorial of {num}: {factorial_recursive(num)}")
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")