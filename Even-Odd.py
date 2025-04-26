def check_even_odd():
    while True:
        try:
            number = int(input("Enter a number: "))
            print(f"You entered: {number}")
            if number % 2 == 0:
                print(f"{number} is Even")
            else:
                print(f"{number} is Odd")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

check_even_odd()
