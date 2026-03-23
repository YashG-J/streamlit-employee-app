import streamlit as st

st.title("Employee Management Dashboard")

name = st.text_input("Enter Employee Name")

department = st.selectbox(
    "Select Department",
    ["HR", "IT", "Finance", "Marketing"]
)

salary = st.number_input("Enter Salary")

if st.button("Submit"):
    st.success("Employee Added Successfully")
    st.write("Name:", name)
    st.write("Department:", department)
    st.write("Salary:", salary)