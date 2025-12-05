import socket
import json
import os

HOST = "0.0.0.0"
PORT = 1236
JSON_FILE = "latest_status.json"

if os.path.exists(JSON_FILE):
    with open(JSON_FILE, "r") as f:
        latest_status = json.load(f)
else:
    latest_status = {}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data:
        conn.close()
        continue

    try:
        payload = json.loads(data.decode())
        machine = payload.get("machine", str(addr))
        latest_status[machine] = {
            "cpu": payload.get("cpu"),
            "ram": payload.get("ram")
        }

        with open(JSON_FILE, "w") as f:
            json.dump(latest_status, f, indent=4)

        print(f"Updated status for {machine}: CPU {payload['cpu']}%, RAM {payload['ram']}%")

    except json.JSONDecodeError:
        print(f"Received invalid data from {addr}")

    conn.close()
