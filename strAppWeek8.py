import streamlit as st
st.write("""
# Finding the greatest number

This app finds the greatest number out of 3 numbers given as input
""")

st.header('User Input Parameters')
def user_input_features():
    Number1 = st.number_input("Number1",min_value=0)
    Number2 = st.number_input("Number2",min_value=0)
    Number3 = st.number_input("Number3",min_value=0)

    max = 0
    if Number1 > max:
        max = Number1

    if Number2 > max:
        max = Number2

    if Number3 > max:
        max = Number3

    return max
maximum_number = user_input_features()
st.subheader('Maximum value of the number entered by the user:')
st.write(maximum_number)
