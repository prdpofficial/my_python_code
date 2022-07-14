class Employee:
    def __init__(self, basic_salary):
        self.emp_id = 'employee1'
        self.basic_salary = basic_salary
        self.hra = (basic_salary*10)/100
        self.da = (basic_salary*10)/100
        self.pf = (basic_salary*5)/100
    def salary(self):
        print("You("+self.emp_id+") Gross salary is: " + str(self.basic_salary+ self.hra + self.da + self.pf))
        print("You("+self.emp_id+") in hand salary is: " + str(self.basic_salary+ self.hra + self.da - self.pf))

Basic_Salary= int(input("Enter basic salary"))
p=Employee(Basic_Salary)
p.salary()
