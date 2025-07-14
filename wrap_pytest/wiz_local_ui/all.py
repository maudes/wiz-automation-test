import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--ip", type=str, required=True)
args = parser.parse_args()  # 實例化

ip = args.ip