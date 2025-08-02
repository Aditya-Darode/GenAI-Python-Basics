class Employee:
    company = "DELL" #This is class attribute

    def __init__(self, salary, name, bond, company):
        self.salary = salary #created an instance attribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond
        self.company = company

    
    def get_salary(self):
       return(f"The nam eof the employee is {self.name}.The bond is for{self.bond}years")
    
e1 = Employee(35000,"Jhon", 3,"Tesla")
print(e1.company) #will alwayys print instance attribute whenever present
print(Employee.company) #This will always print the class attribute