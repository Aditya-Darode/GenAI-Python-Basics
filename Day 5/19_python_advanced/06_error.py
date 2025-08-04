#while True:
    # try:
    #     a = int(input("Enter number 1: "))
    #     b = int(input("Enter number 2: "))
    #     print(f"The sum is{a + b}")
        
    #     #this is used to run the code even if any type of error occured like in this we are accepting integer input if someone entered string then our code will crash and it can't be ececuted further so to handle this error we use this. 
    # except:
    #     print("Some error occurred!")


#raising error

a = int(input("Enter number 1:"))
b = int(input("Enter number 2: "))

if b == 0:
    raise ValueError("Please don't divide by 0")

print(f"The division is {a/b}")