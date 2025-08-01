def sum(a,b):
    print("Hey I am summing")
    global z #please modify global z
    z = 0    #This will refer to global z and not create a local variable 
    c = a + b
    return c

z = 3 #This is a global variable 
print(sum(22,13))
print(z)


#Question - can we modify the global variable in the function ?
#Answer - Yes we can 