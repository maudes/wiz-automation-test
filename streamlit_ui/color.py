from communication import udp_socket, send_and_receive
import time
# common features: change RGB, 
# lightmodes: 1 - 5, 7, 8, 19 - 28 (brightness, speed)

# dictionary
test_cases = {
    "get_state": {
        "method": "getPilot",
        "env": "pro"
        },
    "turn_off": {
        "method": "setPilot",
        "env": "pro",
        "params": {"state": False}
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
    "scene_relax": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 16,
            "dimming": 38
            }
        },
    "scene_ocean": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 1,
            "dimming": 45,
            "speed": 100
            }
        },
    "scene_romance": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 2,
            "dimming": 50,
            "speed": 100
            }
        },
    "scene_mojito": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 25,
            "dimming": 50,
            "speed": 100
            }
        },
    "change_rgb": {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "r": 100,
            "g": 0,
            "b": 140,
            "cw": 150,
            "ww": 0,
            "dimming": 20,
        }
    }
}


def run(device_type, ip):
    if device_type != "Color light":
        return False
    is_passed = 0
    is_failed = 0
    results = {}  # new dictionary for saving results
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
