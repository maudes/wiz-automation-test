#!/usr/bin/env python3
import socket
import json

# WiZ specific info for connection
wiz_ip = '192.168.0.21'  # Change based on the WiZ device you're testing
wiz_port = 38899          # Fixed port WiZ using

# Build up UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)

# Prepare getPilot msg
msg = {"method": "getPilot", "env": "prod"}
# Send out the msg to WiZ lights
sock.sendto(json.dumps(msg).encode(), (wiz_ip, wiz_port))

# Wait to receive Response from the network
for _ in range(3):
    try:
        data, _ = sock.recvfrom(1024)
        print('WiZ response: ', json.loads(data.decode()))
    except socket.timeout:
        print('No response')

# Close the connection
sock.close()
