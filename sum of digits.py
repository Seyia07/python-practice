def digits_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10 
    return total

numbers = 1234
sum_numbers = digits_sum(numbers)
print(sum_numbers) # Output is 10
