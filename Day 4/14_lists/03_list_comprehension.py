#Create a lst conataining the table of 5
'''
a = 5
table = []

for i in range(1,11):
    table.append(5*i)

    This is a regualr method to do this.
'''
table = [5*i for i in range(1,11)]

print(table)

#We can also write like this.