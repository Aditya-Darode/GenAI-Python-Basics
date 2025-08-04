numbers = [1, 2, 3, 4, 5, 6, 7 , 8]

def square(x):
    return x*x

new = list(map(square,numbers))
print(new)
