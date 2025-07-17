import streamlit as st
from modules.runner import run_tests
import time
import json

st.title("Run local test with my WiZ light!")

ip = st.text_input("Input the device IP address", "192.168.0.20")

device_type = st.selectbox(
    "What device type is your light?",
    ("Color light", "Tuneable white light", "Dimmable light"),
)

if st.button("Run the test", type="primary"):
    with st.spinner("Running test", show_time=True):
        time.sleep(2)
        results, passed, failed = run_tests(device_type, ip)

    st.subheader("Test result", divider=True)
    with st.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("Total", passed + failed)
        col2.metric("Passed", passed)
        col3.metric("Failed", failed)
        st.write("Detailed results: ")
        for name, result in results.items():
            st.markdown(f"**{name}:** `{result}`")

st.download_button(
    label="Download results as JSON",
    data=json.dumps(results, indent=2),
    file_name="wiz_test_results.json",
    mime="application/json"
)
