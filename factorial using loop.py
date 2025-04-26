
def loop_factorial(num):
    i = num
    while i > 1:
        num = num * (i-1)
        i = i - 1
    return num


r = loop_factorial(4)
print(r)
