
#a = 4
#b = 2
#c = 1

#average  = (a + b + c)/3
#print(average)

#a1 = 6
#b1 = 7
#c1 = 12

#average1 = (a1 + b1 + c1)/3
#print(average1)

#This above methods are the regular method to to do this but we can use function to reduce our code by calling function for the operation.

def average(a,b,c):
    d = (a+b+c)/3
  # print(d) 
  #average(3,5,1)     #this print average but if we want to assign this value to obejct the we have to return that value like this 
    return d
o1 = average(3,5,1)
print(o1)

