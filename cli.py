import argparse
from modules.runner import run_tests
from modules.scan import scan


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--scan", action="store_true")
    parser.add_argument("--ip", type=str)
    parser.add_argument(
        "--type",
        type=str,
        choices=["Color light", "Tuneable white light", "Dimmable light"]
        )
    args = parser.parse_args()

    if args.scan == True:
        result = scan()
        print(f"Scan result: {result}")
        return

    device_type = args.type
    ip = args.ip

    if device_type is None or ip is None:
        print("Please provide both --ip and --type arguments.")
        return

    results, passed, failed = run_tests(device_type, ip)
    print(f"Total {passed + failed} with {passed} tests passed and {failed} tests failed.")
    for name, result in results.items():
        print(f"{name}: {result}")


if __name__ == "__main__":
    main()
