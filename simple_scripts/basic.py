#!/usr/bin/env python3
import socket
import json
import time

# WiZ specific info for connection
wiz_ip = '192.168.0.21'  # Change based on the WiZ device you're testing
wiz_port = 38899          # Fixed port WiZ using

# Build up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)

# Prepare getPilot msg
get_msg = {
    "method": "getPilot",
    "env": "prod"
}
# Send out the msg to WiZ lights
sock.sendto(json.dumps(get_msg).encode(), (wiz_ip, wiz_port))

# Wait to receive Response from the network
# for _ in range(3):
try:
    data, _ = sock.recvfrom(1024)
    print('WiZ response: ', json.loads(data.decode()))
except socket.timeout:
    print('No response')

time.sleep(3)

# Try the feature testing with test_msg + send + receive response
# Turn off
off_msg = {
    "method": "setPilot",
    "env": "pro",
    "params": {
        "state": False
    }
}
sock.sendto(json.dumps(off_msg).encode(), (wiz_ip, wiz_port))

try:
    data, _ = sock.recvfrom(1024)
    print('WiZ response: ', json.loads(data.decode()))
except socket.timeout:
    print('No response')

time.sleep(3)

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
sock.sendto(json.dumps(on_msg).encode(), (wiz_ip, wiz_port))

try:
    data, _ = sock.recvfrom(1024)
    print('WiZ response: ', json.loads(data.decode()))
except socket.timeout:
    print('No response')

time.sleep(3)

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
sock.sendto(json.dumps(scene_msg).encode(), (wiz_ip, wiz_port))

try:
    data, _ = sock.recvfrom(1024)
    print('WiZ response: ', json.loads(data.decode()))
except socket.timeout:
    print('No response')

time.sleep(3)

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
sock.sendto(json.dumps(rgb_msg).encode(), (wiz_ip, wiz_port))

try:
    data, _ = sock.recvfrom(1024)
    print('WiZ response: ', json.loads(data.decode()))
except socket.timeout:
    print('No response')

# Close the connection
sock.close()
