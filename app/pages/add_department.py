import streamlit as st
import pandas as pd

from utils import add_department

st.header('Employee data management.')
st.info('Add new department.')

# get list of department IDs to enforce unique ID
dept_df = pd.read_csv('dept.csv', usecols=['Deptno'])
dept_ids = dept_df['Deptno'].unique().tolist()

department_number = st.number_input('Department number', format='%d', step=1)
department_name = st.text_input("Department name")
department_location = st.text_input("Department Location")

submit = st.button(label='Submit')
if submit:
    if not all([department_number, department_name, department_location]):
        st.error("Please fill in all fields.")
    elif department_number in dept_ids:
        st.error(f"Department with id {department_number} already exists.")
    else:
        add_department(department_number, department_name, department_location)
        st.success("New record added.")
