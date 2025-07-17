from modules.communication import udp_socket, send_and_receive
from modules.type_data import color_test_case, tuneable_test_case, dimmable_test_case
import time


def test_model(sock, test_case, ip):
    results = {}  # new dictionary for saving results
    passed, failed = 0, 0
    for tc_name, msg in test_case.items():
        try:
            response = send_and_receive(sock, msg, ip)
            results[tc_name] = response
            passed += 1
        except Exception as e:
            results[tc_name] = f"Error: {e}"
            failed += 1
        time.sleep(0.5)
    return results, passed, failed


def run_tests(device_type, ip):
    with udp_socket() as sock:
        if device_type == "Color light":
            return test_model(sock, color_test_case, ip)
        elif device_type == "Tuneable white light":
            return test_model(sock, tuneable_test_case, ip)
        else:
            return test_model(sock, dimmable_test_case, ip)
