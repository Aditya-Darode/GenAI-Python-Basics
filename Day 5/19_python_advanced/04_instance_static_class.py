class Employee:
    company = "DELL"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    #Instance method (default)
    def print_info(self):
        info =f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    #static method 
    #this method does not required self
    @staticmethod
    def sum(a,b):
        return a+b
    
    #class method
    @classmethod
    def print_company(cls):
        print(cls.company)

e1 = Employee("Aditya",45000)
e2 = Employee("Raj",50000)

e1.print_info()
e2.print_info()

print(e2.sum(13,22))
e1.print_company()



