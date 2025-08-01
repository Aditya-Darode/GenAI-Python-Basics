''' 
0 1 1 2 5 8 13 _ _ _ _

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1)
fib(3) = fib(1) + fib(2)
fib(n) = fib(n-2) + fib(n-1)

'''
def fib(n):
    #Base case of recursion
    if(n==0 or n==1):
       return n

    return fib(n-2) + fib(n-1)
print(fib(6))
