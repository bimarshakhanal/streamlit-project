import streamlit as st

from utils import add_department

st.header('Employee data management.')
st.info('Add new department.')

department_number = st.number_input('Department number', format='%d', step=1)
department_name = st.text_input("Department name")
department_location = st.text_input("Department Location")

submit = st.button(label='Submit')
if submit:
    if all([department_number, department_name, department_location]):
        add_department(department_number, department_name, department_location)
        st.success("New record added.")
    else:
        st.error("Please fill in all fields.")
