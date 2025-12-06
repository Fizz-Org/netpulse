import json
import os

JSON_FILE = "latest_status.json"

def load_status():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    return {}

def main():
    latest_status = load_status()
    print("Latest machine statuses:\n")
    for machine, stats in latest_status.items():
        print(f"{machine}: CPU {stats.get('cpu')}%, RAM {stats.get('ram')}%")

if __name__ == "__main__":
    main()

