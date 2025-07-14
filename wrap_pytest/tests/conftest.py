import pytest
import socket
import json
'''
import os

WIZ_IP = os.getenv('WIZ_IP')
WIZ_PORT = int(os.getenv('WIZ_PORT'))
'''

#  wiz_ip = "192.168.0.20"
wiz_port = 38899


def pytest_addoption(parser):
    parser.addoption("--ip", action="store")  # default='192.168.0.20'


@pytest.fixture(scope='module')
def wiz_ip(request):
    return request.config.getoption("--ip")


# Build up UDP socket
@pytest.fixture(scope='module')
def udp_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)
    yield sock
    sock.close()


@pytest.fixture(scope='module')
def wiz_client(udp_socket, wiz_ip):
    def _send_receive(msg):
        udp_socket.sendto(json.dumps(msg).encode(), (wiz_ip, wiz_port))
        try:
            data, _ = udp_socket.recvfrom(1024)
            response = json.loads(data.decode())
            # print(f'WiZ response for {msg.get("method", "unknown")}: {response}')
            return response  # 給系統比對用
        except socket.timeout:
            return None
        except json.JSONDecodeError:
            return None
        except Exception as e:
            return None
    return _send_receive
