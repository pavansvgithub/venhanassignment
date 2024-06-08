def sum_of_squares(numbers):
    sum = 0
    for i in numbers:
        sum += i * i 
    return sum

numbers = list(map(int,input().split()))
result = sum_of_squares(numbers)
print(result)