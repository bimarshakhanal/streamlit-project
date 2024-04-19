import streamlit as st
import pandas as pd

from utils import add_employee

st.header('Employee data management.')
st.info('Add new employee.')

emp_df = pd.read_csv('employee.csv')
emp_ids = emp_df['Empno'].unique().tolist()

dept_df = pd.read_csv('dept.csv')
dept_to_id = dict(zip(dept_df['Department Name'], dept_df['Deptno']))

employee_number = st.number_input('Employee number', format='%d', step=1)
employee_name = st.text_input("Employee name")
employee_job = st.text_input("Employee job")
employee_department = st.selectbox(
    label='Department', options=dept_to_id.keys())

submit = st.button(label='Submit')
if submit:
    if not all([employee_number, employee_name, employee_job, employee_department]):
        st.error("Please fill in all fields.")
    elif employee_number in emp_ids:
        st.error(f"Employ with id {employee_number} already exists.")
    else:
        add_employee(employee_number, employee_name,
                     employee_job, dept_to_id[employee_department])
        st.success("New record added.")
