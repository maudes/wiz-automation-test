from communication import udp_socket, send_and_receive
import time
# common features: on/off, change brightness

test_cases = {
    "get_state": {
        "method": "getPilot",
        "env": "pro"
    },
    "turn_off": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": False
        }
    },
    "turn_on_brightness": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "dimming": 38
        }
    }
}


def run(device_type, ip):
    if device_type != "Dimmable light":
        return False
    is_passed = 0
    is_failed = 0
    results = {}
    for tc_name, msg in test_cases.items():
        try:
            response = send_and_receive(udp_socket, msg, ip)
            results[tc_name] = response
            is_passed += 1
            time.sleep(0.5)
        except Exception as e:
            results[tc_name] = f"Error: {e}"
            is_failed += 1
    return results, is_passed, is_failed
