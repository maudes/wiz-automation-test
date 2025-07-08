#!/usr/bin/env python3
import socket
import json

# WiZ specific info for connection
wiz_ip = '192.168.0.20'  # Change based on the WiZ device you're testing
wiz_port = 38899          # Fixed port WiZ using

# Build up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)

# Test results report
is_passed = 0
is_failed = 0


# Shared send and receive actions
def send_receive(sock, msg, ip, port):
    sock.sendto(json.dumps(msg).encode(), (ip, port))
    try:
        data, _ = sock.recvfrom(1024)
        print('WiZ response: ', json.loads(data.decode()))
        return True
    except socket.timeout:
        print('No response')
        return False


def check_state(sock, ip, port):
    # Prepare getPilot msg
    msg = {
        "method": "getPilot",
        "env": "pro"
    }
    return send_receive(sock, msg, ip, port)


def check_off(sock, ip, port):
    # Turn off
    msg = {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": False
        }
    }
    return send_receive(sock, msg, ip, port)


def check_white(sock, ip, port):
    # Turn on with white light
    msg = {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "temp": 6500,
            "dimming": 30
        }
    }
    return send_receive(sock, msg, ip, port)


def check_lightmode(sock, ip, port):
    # Change light mode
    msg = {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 21,
            "dimming": 60,
            "speed": 100,
        }
    }
    return send_receive(sock, msg, ip, port)


def check_rgb(sock, ip, port):
    # Change RGB
    msg = {
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
    return send_receive(sock, msg, ip, port)


# Run the tests
for check in [check_state, check_off, check_white, check_lightmode, check_rgb]:
    if check(sock, wiz_ip, wiz_port):
        is_passed += 1
    else:
        is_failed += 1

print(f"Total {is_passed} tests passed, and {is_failed} tests failed.")

# Close the connection
sock.close()
