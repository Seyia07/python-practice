def sum_of_digits(number):
    total = 0
    number = abs(number)
    while number > 0:
        total += number % 10
        number //= 10
    return total
while True:
    try:
        num = int(input("Enter a number: "))
        print(f"Sum of digits in {num}: {sum_of_digits(num)}")
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")