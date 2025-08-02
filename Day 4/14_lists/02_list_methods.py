marks = [5, 20, 7, 19, 9, 22, 12]
extra_marks = [13, 14, 15, 16, 17]

print(marks)
marks.append(13) #This will change the original list
print(marks)

marks.pop()      #This will remove the last object
print(marks)

marks.extend(extra_marks) #This will append the second list to the first list
print(marks)

marks.sort() 
print(marks)

marks.reverse()
print(marks)