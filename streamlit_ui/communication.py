import socket
import json

port = 38866


def udp_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)
    return sock


def send_and_receive(udp_socket, msg, ip):
    udp_socket.sendto(json.dumps(msg).encode(), (ip, port))
    try:
        data, _ = udp_socket.recvfrom(1024)
        response = json.loads(data.decode())
        return response
    except socket.timeout:
        return False
    except json.JSONDecodeError:
        return False
    except Exception:
        return False


def close(udp_socket):
    udp_socket.close()
