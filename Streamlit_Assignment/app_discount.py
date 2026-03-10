import streamlit as st

price = st.number_input("Enter the price")

discount = st.slider("Select Discount (%)", 0,50)

if st.button("Calculate Discount"):
    
    final_price = price - (price*(discount/100))
    
    st.success(f"final discount price {final_price}") 
    
    table_data = [
        ["Original Price", price],
        ["Discount %", discount],
        ["Final Price", final_price]
    ]

    st.table(table_data)