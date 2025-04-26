def sum_of_digits(number):
    """Calculates the sum of digits in a given number."""
    total = 0  # Start at zero
    number = abs(number)  # Convert to positive (in case user enters a negative number)
    
    while number > 0:  # Loop until no digits are left
        total += number % 10  # Get last digit and add to total
        number //= 10  # Remove last digit
    
    return total  # Return final sum of digits

# Get user input with error handling
while True:
    try:
        num = int(input("Enter a number: "))  # Ask user for input
        print(f"Sum of digits in {num}: {sum_of_digits(num)}")  # Display result
        break  # Exit loop after successful input
    except ValueError:  # Handle non-integer input
        print("Invalid input! Please enter a valid integer.")

