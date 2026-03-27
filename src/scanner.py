import socket
import argparse
from datetime import datetime


def scan_port(host, port, timeout=0.5):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            return result == 0
    except:
        return False


def scan_ports(host, start_port, end_port, timeout=0.5):
    print("=" * 50)
    print(f"Cible       : {host}")
    print(f"Ports       : {start_port} à {end_port}")
    print(f"Démarré à   : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(host, port, timeout):
            print(f"[OUVERT] Port {port}")
            open_ports.append(port)
        else:
            print(f"[FERMÉ]  Port {port}")

    print("=" * 50)
    print(f"Ports ouverts : {open_ports}")
    print("=" * 50)


def main():
    parser = argparse.ArgumentParser(description="Scanner de ports TCP en Python")
    parser.add_argument("host", help="IP ou domaine")
    parser.add_argument("start_port", type=int)
    parser.add_argument("end_port", type=int)

    args = parser.parse_args()

    scan_ports(args.host, args.start_port, args.end_port)


if __name__ == "__main__":
    main()