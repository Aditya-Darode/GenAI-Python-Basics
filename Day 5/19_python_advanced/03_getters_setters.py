class Student:
    def __init__(self, name, age):
        self.__name = name
        self.set_age(age)  #set_age checks voting eligibility

    def get_name(self):  #used to get the name 
        return self.__name

    def set_name(self, new_name): #used to set the name 
        self.__name = new_name

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if new_age > 18:
            self.__age = new_age
            print(f"{self.__name}, You are eligible to vote :)")
        else:
            self.__age = new_age
            print(f"{self.__name}, You are not eligible to vote :(")

s1 = Student("Aditya", 21)
s2 = Student("Raj", 17)

print(s1.get_name(), s1.get_age())
print(s2.get_name(), s2.get_age())
