class Employee:

    def __init__(self, salary, name, bond):
        self.salary = salary #created an instance attribute of name salary and assign it with salary
        self.name = name 
        self.bond = bond
    
    def get_salary(self):
       return self.salary

e1 = Employee(35000, "Jhon Doe", 4)
print(e1.get_salary())


