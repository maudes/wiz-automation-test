import streamlit as st

st.title("Run local test with my WiZ light!")

ip = st.text_input("Input the device IP address", "xxx.xxx.xxx.xxx")

device_type = st.selectbox(
    "What device type is your light?",
    ("Color light", "Tuneable white light", "Dimmable light"),
)
st.write("You selected:", device_type)
