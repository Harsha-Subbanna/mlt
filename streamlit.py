
import streamlit as st

def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

st.title("Find the Largest Number")
st.write("Enter three numbers below to find the largest among them.")

a = st.number_input("Enter the first number:",value=0)
b = st.number_input("Enter the second number:",value=0)
c = st.number_input("Enter the third number:",value=0)

if st.button("Find"):
    largest = find_largest(a, b, c)
    st.write(f"The largest number is {largest}.")
