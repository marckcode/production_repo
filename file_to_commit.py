def add_numbers(*args):
    sum = 0
    for num in args:
        sum += num
    
    return sum

print(add_numbers(1, 2, 3, 4, 5))