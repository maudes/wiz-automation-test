import socket
import json
import time

port = 38899


def scan():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(3)
    msg = {
        "method": "getPilot",
        "env": "pro"
        }
    sock.sendto(json.dumps(msg).encode(), ("192.168.0.255", port))

    try:
        data, _ = sock.recvfrom(1024)
        response = json.loads(data.decode())
        time.sleep(3)
        return response
    except socket.timeout:
        return {"error": "timeout"}
    except json.JSONDecodeError:
        return {"error": "invalid JSON"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        sock.close()
