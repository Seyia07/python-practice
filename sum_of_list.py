def list_sum(numbers):
    sum = 0 #Included a variable to which all numbers would be added to there
    for number in numbers:
        sum += number
    return sum 

marks = [10,20,30,40]
sum = list_sum(marks) #Returns 100
print(sum)