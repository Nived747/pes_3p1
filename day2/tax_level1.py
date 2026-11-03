name = input('Enter employee name:')
employee_id = int(input('Enter employee Id: '))
basic_monthly_salary = float(input('Enter basic monthly salary of the employee: '))
allowance = float(input('Enter employee allowance: '))
bonus_percentage = float(input('Enter employee bonus percentage: '))

gross_monthly_salary = basic_monthly_salary + allowance
annual_gross_salary = (gross_monthly_salary * 12) + (gross_monthly_salary * (bonus_percentage / 100) * 12)

print(f'Employee Name: {name}')
print(f'Employee ID: {employee_id}')
print(f'Basic Monthly Salary: {basic_monthly_salary}')
print(f'Employee Monthly Allowance: {allowance}')
print(f'Gross Monthly Salary: {gross_monthly_salary}')
print(f'Bonus Percentage: {bonus_percentage}')
