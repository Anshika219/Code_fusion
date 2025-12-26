import streamlit as st
st.set_page_config(
    page_title="AI-Driven Expense Tracker For Indian Students",
    layout="centered"
)
st.title("AI Expense Tracker For Indian Students")
st.write("Upload bill/UPI screenshots or enter expense text.")
options=st.radio("Choose input method:",["Text","Image"])
if options=="Text":
    text_input=st.text_input("enter your expense details",placeholder="paid \u20B9250 to zomato via UPI")
elif options=="Image":
    image_input=st.file_uploader("upload UPI screenshot or Bill")
    if image_input:
        st.image(image,caption="Uploaded Image",use_column_width=True)
if st.button("Extract Expense"):
    st.subheader("Extracted Expense (prototype output)")
    dumy_json={
    "amount":250,
    "catogory":"food",
    "merchant":"zomato",
    "date":"2025-12-25",
    "payment_method":"UPI"
    }
    st.json(dumy_json)