import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning {target}...")
    print(f"Ports: {start_port} to {end_port}\n")
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        sock.close()
    print(f"\nScan complete! Open ports: {open_ports}")

target = input("Enter target IP or website: ")
scan_ports(target, 1, 100)
