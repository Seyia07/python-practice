def sum_list(numbers):
    """Returns the sum of all elements in the list."""
    total = 0
    for num in numbers:
        total += num
    return total

# Test the function
if __name__ == "__main__":
    sample_list = [5, 267, 87, 945, 85]
    print("Sum:", sum_list(sample_list))
