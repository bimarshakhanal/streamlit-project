import streamlit as st
import pandas as pd

st.header('Employee data management.')
st.info('View employee records')

dept_df = pd.read_csv('dept.csv')
employee_df = pd.read_csv('employee.csv')
print(dept_df.columns)
combined_df = employee_df.join(
    dept_df.set_index('Deptno'), on='Deptno', how='left')

st.dataframe(combined_df[['Empno', 'Employee Name',
             'Job', 'Deptno', 'Department Name']])
