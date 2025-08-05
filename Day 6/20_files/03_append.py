#Append to an existinf file called Jhon Doe.txt
#It should data about Jhon Doe"s Hometown


f =open("Jhon Doe.txt", "a")

string = '''
Jhon Doe initially lived in Phoenix, Arizona. He is a very nice guy
'''
f.write(string)

f.close()
