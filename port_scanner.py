import socket
import argparse
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except Exception as e:
        pass

def main():
    parser = argparse.ArgumentParser(description="Basic Port Scanner")
    parser.add_argument("target", help="Target IP address to scan")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range (e.g., 1-1024 or 80,443)")
    args = parser.parse_args()

    target = args.target
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports_to_scan = range(start, end + 1)
    else:
        ports_to_scan = [int(p) for p in args.ports.split(",")]

    print(f"[*] Starting scan on {target} for ports {args.ports}...")
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in ports_to_scan:
            executor.submit(scan_port, target, port)
            
if __name__ == "__main__":
    main()
