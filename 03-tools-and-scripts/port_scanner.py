import socket
import sys
from datetime import datetime

# Target definition
target_host = "127.0.0.1"  # Replace with target IP (or localhost)
ports_to_scan = [21, 22, 80, 443, 8080]

print("-" * 50)
print(f"Scanning target: {target_host}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    for port in ports_to_scan:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target_host, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: Closed")
        s.close()

except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nCould not connect to server.")
    sys.exit()
