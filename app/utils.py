"""
Helper functions to manage employee data
"""
import os

DEPARTMENT_CSV = 'dept.csv'
EMPLOYEE_CSV = 'employee.csv'

# create csv files if it doesn't exist
if not os.path.exists(DEPARTMENT_CSV):
    with open(DEPARTMENT_CSV, 'w', encoding='utf-8') as dept_csv:
        dept_csv.write('Deptno, Department Name, Location')

if not os.path.exists(EMPLOYEE_CSV):
    with open(EMPLOYEE_CSV, 'w', encoding='utf-8') as emp_csv:
        emp_csv.write('Empno, Employee Name, Job, Department No')


def add_employee(empno, name, job, dept):
    '''
    Function to add employee recotd to csv file
    Args:
        empno: int - Employee ID
        name: str - Employee name
        job: str - Employee job
        dept: int - Department ID of employee  
    '''
    with open(EMPLOYEE_CSV, 'a', encoding='utf-8') as emp_csv:
        emp_csv.write(f'\n{empno}, {name}, {job}, {dept}')


def add_department(deptno, name, location,):
    '''
    Function to add department recotd to csv file
    Args:
        deptno: int - Department ID
        name: str - Department name
        location: str - Location of department
    '''
    with open(EMPLOYEE_CSV, 'a', encoding='utf-8') as emp_csv:
        emp_csv.write(f'\n{deptno}, {name}, {location}')
