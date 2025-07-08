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


def check_status(sock, ip, port):
    # Prepare getPilot msg
    get_msg = {
        "method": "getPilot",
        "env": "prod"
    }
    # Send out the msg to WiZ lights
    sock.sendto(json.dumps(get_msg).encode(), (ip, port))

    # Wait to receive Response from the network
    # for _ in range(3):
    try:
        data, _ = sock.recvfrom(1024)
        print('WiZ response: ', json.loads(data.decode()))
        return True
    except socket.timeout:
        print('No response')
        return False


def check_off(sock, ip, port):
    # Turn off
    off_msg = {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": False
        }
    }
    sock.sendto(json.dumps(off_msg).encode(), (ip, port))

    try:
        data, _ = sock.recvfrom(1024)
        print('WiZ response: ', json.loads(data.decode()))
        return True
    except socket.timeout:
        print('No response')
        return False


def check_white(sock, ip, port):
    # Turn on with white light
    on_msg = {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "temp": 6500,
            "dimming": 30
        }
    }
    sock.sendto(json.dumps(on_msg).encode(), (ip, port))

    try:
        data, _ = sock.recvfrom(1024)
        print('WiZ response: ', json.loads(data.decode()))
        return True
    except socket.timeout:
        print('No response')
        return False

# time.sleep(3)


def check_lightmode(sock, ip, port):
    # Change light mode
    scene_msg = {
        "method": "setPilot",
        "env": "pro",
        "params": {
            "state": True,
            "sceneId": 21,
            "dimming": 60,
            "speed": 100,
        }
    }
    sock.sendto(json.dumps(scene_msg).encode(), (ip, port))

    try:
        data, _ = sock.recvfrom(1024)
        print('WiZ response: ', json.loads(data.decode()))
        return True
    except socket.timeout:
        print('No response')
        return False

# time.sleep(3)


def check_rgb(sock, ip, port):
    # Change RGB
    rgb_msg = {
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
    sock.sendto(json.dumps(rgb_msg).encode(), (ip, port))

    try:
        data, _ = sock.recvfrom(1024)
        print('WiZ response: ', json.loads(data.decode()))
        return True
    except socket.timeout:
        print('No response')
        return False


# Run the tests
if check_status(sock, wiz_ip, wiz_port):
    is_passed += 1
else:
    is_failed += 1

if check_off(sock, wiz_ip, wiz_port):
    is_passed += 1
else:
    is_failed += 1

if check_white(sock, wiz_ip, wiz_port):
    is_passed += 1
else:
    is_failed += 1

if check_lightmode(sock, wiz_ip, wiz_port):
    is_passed += 1
else:
    is_failed += 1

if check_rgb(sock, wiz_ip, wiz_port):
    is_passed += 1
else:
    is_failed += 1

print(f"Total {is_passed} tests passed, and {is_failed} tests failed.")

# Close the connection
sock.close()
