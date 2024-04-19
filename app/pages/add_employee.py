import streamlit as st

from utils import add_employee

st.header('Employee data management.')
st.info('Add new employee.')

employee_number = st.number_input('Employee number', format='%d', step=1)
employee_name = st.text_input("Employee name")
employee_job = st.text_input("Employee job")
employee_department = st.number_input(
    "Employee job", format='%d', step=1)

# st.button(label='Add record',
#           on_click=add_employee(employee_name,
#                                 employee_name, employee_job,
#                                 employee_department))

submit = st.button(label='Submit')
if submit:
    if all([employee_number, employee_name, employee_job, employee_department]):
        print(employee_number, employee_name,
              employee_department, employee_job)
        add_employee(employee_number, employee_name,
                     employee_job, employee_department)
        st.success("New record added.")
    else:
        st.error("Please fill in all fields.")

# print(employee_number, employee_name, employee_department, employee_job)
