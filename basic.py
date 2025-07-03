#!/usr/bin/env python3
import socket
import json

# print('Hello World!')

wiz_ip = "192.168.0.21"  # Should change to input for receiving light's IP
wiz_port = 38899          # wiz port

# 建立 UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)    # 3 seconds the top

# 傳送 getPilot
msg = {"method": "getPilot", "env": "pro"}
sock.sendto(json.dumps(msg).encode(), (wiz_ip, wiz_port))

# 等待回應
try:
    data, _ = sock.recvfrom(1024)
    print("WiZ response：", json.loads(data.decode()))
except socket.timeout:
    print("No response")

sock.close()
