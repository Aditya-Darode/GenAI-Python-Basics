#Class: Class is a blueprint or a template. Eg. Form for an Exam that conatains name, age, electives, father's name etc

#Object: Specific instance created from the template(class.). Eg. form which contains the data for Jhon Doe

class Employee:
    company = "Dell"

    def get_salary(self): # Self is important here because self is a way to reference the object of the class which is being used
        return 35000
    
e = Employee() #An object of class Employee is created here
print(e.get_salary()) #Employee e's get salary method is called

e2 = Employee()
print((e2.get_salary()))