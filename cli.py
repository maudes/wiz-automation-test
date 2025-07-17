import argparse
from modules.runner import run_tests


parser = argparse.ArgumentParser()
parser.add_argument("--ip", type=str, required=True)
parser.add_argument(
    "--type",
    type=str,
    choices=["Color light", "Tuneable white light", "Dimmable light"],
    required=True
    )
args = parser.parse_args()

device_type = args.type
ip = args.ip

results, passed, failed = run_tests(device_type, ip)
print(f"Total {passed + failed} with {passed} tests passed and {failed} tests failed.")
print(f"{results}")
