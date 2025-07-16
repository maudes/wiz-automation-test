import streamlit as st
import color
import common
import temperature

st.title("Run local test with my WiZ light!")

ip = st.text_input("Input the device IP address", "192.168.0.20")

device_type = st.selectbox(
    "What device type is your light?",
    ("Color light", "Tuneable white light", "Dimmable light"),
)

if st.button("Run the test", type="primary"):
    str.write("Should trigger the test run, and print out the result below")


st.subheader("Test result", divider=True)
with st.container():
    st.write("Print out the test result here.")


# def udp_socket():


# def send_and_receive(ip, device_type):