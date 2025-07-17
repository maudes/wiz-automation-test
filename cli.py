import argparse
import color
import dimmable
import tuneable

parser = argparse.ArgumentParser()
parser.add_argument("--ip", type=str, required=True) 
parser.add_argument("--type", type=str, required=True) 
args = parser.parse_args()  

device_type = args.type
ip = args.ip

def run_tests(device_type, ip):
    if device_type == "Color light":
        return results, passed, failed = color.run(device_type, ip)
    elif device_type == "Tuneable white light":
        return results, passed, failed = tuneable.run(device_type, ip)
    else:
        return results, passed, failed = dimmable.run(device_type, ip)

run_tests(device_type, ip)
print(f"Total {passed + failed}} {passed} tests passed, and {failed} tests failed.")

