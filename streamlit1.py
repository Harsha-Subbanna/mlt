import streamlit as st

def find_largest(A, B, C):
    """
    This function finds the largest among three given natural numbers.
    """
    if A >= B and A >= C:
        return A
    elif B >= A and B >= C:
        return B
    else:
        return C

def main():
    """
    This function defines the Streamlit app UI and logic.
    """
    st.title("Find the largest among 3 natural numbers")
    A = st.number_input("Enter the first natural number", value=0, step=1)
    B = st.number_input("Enter the second natural number", value=0, step=1)
    C = st.number_input("Enter the third natural number", value=0, step=1)

    if st.button("Find the largest"):
        largest_num = find_largest(A, B, C)
        st.success(f"The largest number is {largest_num}")

if _name_ == "_main_":
    main()
