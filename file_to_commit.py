def add_numbers(*args):
    """Add any amount of number to 'sum'."""
    sum = 0
    for num in args:
        sum += num
    
    return sum

def dif_numbers(*args):
    """First number entered got substracted."""
    diff = args[0]
    
    for num in args:
        diff -= num
    
    return diff

print(add_numbers(1, 2, 3, 4, 5))
print(dif_numbers(1, 2, 3, 4, 5))



