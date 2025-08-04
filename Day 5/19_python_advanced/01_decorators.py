# Decorator is function that takes a function, it creates a new function inside its body (warapper). Then it returns the new function.
def decorator(func):
    def warapper():
        print("I am about to execute a function...")
        func()
        print("I have executed the function...")
    return warapper

def say_hello():
    print("Hello")

#say_hello()
f = decorator(say_hello)
f()
'''
f will look something like this 
def f():
    print("I am about to execute a function...")
    print("Hello")
    print("I have executed the function...")

'''
