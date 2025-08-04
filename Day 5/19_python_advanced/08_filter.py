def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False
    
a = [1, 2, 345, 34, 6, 7, 9, 13, 22]

new = list(filter(is_greater_than_9, a))
print(new)