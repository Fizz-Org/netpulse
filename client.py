import psutil
import socket
import json
import time

SERVER_HOST = "localhost"
SERVER_PORT = 1236

MACHINE = socket.gethostname()

while True:
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    payload = {
        "machine": MACHINE,
        "cpu": cpu_usage,
        "ram": ram_usage
    }

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SERVER_HOST, SERVER_PORT))
        s.sendall(json.dumps(payload).encode())
        s.close()
        print(f"Sent: {payload}")
    except ConnectionRefusedError:
        print("Server not available")

    time.sleep(30)
