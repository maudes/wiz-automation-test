import socket
import json
from contextlib import contextmanager
import time

port = 38899


@contextmanager
def udp_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)
    try:
        yield sock
    finally:
        sock.close()


def send_and_receive(sock, msg, ip):
    sock.sendto(json.dumps(msg).encode(), (ip, port))
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
