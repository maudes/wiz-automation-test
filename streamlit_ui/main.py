import streamlit as st
from stareamlit_ui import color, dimmable, tuneable
from stareamlit_ui.communication import close, udp_socket
import time

st.title("Run local test with my WiZ light!")

ip = st.text_input("Input the device IP address", "192.168.0.20")

device_type = st.selectbox(
    "What device type is your light?",
    ("Color light", "Tuneable white light", "Dimmable light"),
)

if st.button("Run the test", type="primary"):
    with st.spinner("Running test", show_time=True):
        time.sleep(5)
        if device_type == "Color light":
            results, passed, failed = color.run(device_type, ip)
        elif device_type == "Tuneable white light":
            results, passed, failed = tuneable.run(device_type, ip)
        else:
            results, passed, failed = dimmable.run(device_type, ip)

    st.subheader("Test result", divider=True)
    with st.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("Total", passed + failed)
        col2.metric("Passed", passed)
        col3.metric("Failed", failed)
        st.write("Detailed results: ")
        for name, result in results.items():
            st.markdown(f"**{name}:** `{result}`")

    close(udp_socket)
