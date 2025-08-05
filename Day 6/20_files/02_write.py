#Write to a file called Jhon Doe.txt
#It should contain data about Jhon Doe

f =open("Jhon Doe.txt", "w")

string = '''
Jhon Doe i a nice guy. He Lives in NYC and he works with python His favorite package is pandas
'''
f.write(string)

f.close()
