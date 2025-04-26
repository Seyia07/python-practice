def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
user_input = input("Enter a word or phrase: ")
print(f"Original: {user_input}")
print(f"Reversed: {reverse_string(user_input)}")

