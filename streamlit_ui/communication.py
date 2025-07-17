import socket
import json
from contextlib import contextmanager

port = 38866


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
        return response
    except (socket.timeout, json.JSONDecodeError, Exception):
        return False
