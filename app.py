import streamlit as st
from generator import generate_random_password, generate_memorable_password, generate_pin

st.image('./banner.jpeg')
st.title("Password Generator")

option = st.radio("Password Type:" , ('Random Password','Memorable Password' ,'Pin Code'))

if option == "Random Password":
    length = st.slider("Length", min_value=5, max_value=50, value=5)
    include_numbers = st.checkbox("Include Numbers")
    include_symbols = st.checkbox("Include Symbols")

    generator = generate_random_password(length, include_numbers, include_symbols)

elif option == "Memorable Password":
    no_of_words = st.slider("Number of Words", min_value=2, max_value=4, value=3)
    separator = st.text_input("Separator", value="-")
    capitalization = st.checkbox("Capitalization")

    generator = generate_memorable_password(no_of_words, separator, capitalization)

elif option == "Pin Code":
    length = st.slider("Length", min_value=4, max_value=12, value=4)
    generator = generate_pin(length)

password = generator
st.write("Your password is:")
st.header(fr"```{password}```")
