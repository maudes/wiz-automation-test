from communication import udp_socket, send_and_receive
import time
# common features: change temperate 2700 - 6500
# # change temperature lightmodes: 6, 11-16, 18 (brightness, speed)

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
    },
    "change_temp_warm": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "temp": 4200,
            "dimming": 55
        }
    },
    "change_temp_cold": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "temp": 5500,
            "dimming": 70
        }
    },
    "scene_daylight": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 21,
            "dimming": 38
        }
    }, 
    "scene_relax": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 16,
            "dimming": 38
        }
    }
}


def run(device_type, ip):
    if device_type != "Tuneable white light":
        return False
    is_passed = 0
    is_failed = 0
    results = {}
    for tc_name, msg in test_cases.items:
        try:
            response = send_and_receive(udp_socket, msg, ip)
            results[tc_name] = response
            is_passed += 1
            time.sleep(0.5)
        except Exception as e:
            results[tc_name] = f"Error: {e}"
            is_failed += 1
    return results, is_passed, is_failed
