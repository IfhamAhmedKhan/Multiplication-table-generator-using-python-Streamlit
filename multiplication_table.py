import streamlit as st

def multiplication_table(number, limit):
    table = []
    for i in range(1, limit + 1):
        row = f"{number} x {i} = {number * i}"
        table.append(row)
    return table

def main():
    st.title("Multiplication Table Generator")

    # User input for the base number
    number = st.number_input("Enter the base number:", min_value=1)

    # User input for the table limit
    limit = st.number_input("Enter the table limit:", min_value=1)

    # Generate and display the multiplication table
    if st.button("Generate Table"):
        table_data = multiplication_table(int(number), int(limit))
        st.write(f"Multiplication Table for {number} up to {limit}")
        for row in table_data:
            st.write(row)

if __name__ == "__main__":
    main()
