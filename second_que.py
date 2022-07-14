basic_salary = int(input("Please enter your basic salary : "))
input_da = int(input("Please enter your dearness allowance 'should be in percentage' : "))
input_hra = int(input("Please enter your house rent allowance 'should be in percentage' : "))
input_pf = int(input("Please enter your provident fund 'should be in percentage' : "))

da = int(basic_salary * (input_da/100))
hra = int(basic_salary * (input_hra/100))
pf = int(basic_salary * (input_pf/100))


monthly_salary = ((basic_salary + da + hra) - (pf))


annual_salary = monthly_salary*12

if(annual_salary > 500000):
    print("your Gross monthly salary is : " + str(monthly_salary))
    tax = int(monthly_salary*(20/100))
    print("Tax deductions : "+ str(tax))
    monthly_salary -= tax
    print("Your monthly salary is : " + str(monthly_salary) )
else:
    print("Your monthly salary is : " + str(monthly_salary))
