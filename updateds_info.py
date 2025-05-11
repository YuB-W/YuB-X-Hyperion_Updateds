import requests
import re
import os
import time

VERSION_FILE = "last_version.txt"
DEPLOY_URL = "https://setup.rbxcdn.com/DeployHistory.txt"
CHECK_INTERVAL = 30 

def read_saved_version():
    return open(VERSION_FILE).read().strip() if os.path.exists(VERSION_FILE) else None

def save_version(version):
    with open(VERSION_FILE, "w") as f:
        f.write(version)

def get_latest_client_version(session):
    try:
        r = session.get(DEPLOY_URL, timeout=5)
        r.raise_for_status()
        for line in reversed(r.text.splitlines()):
            if line.startswith("New WindowsPlayer version-"):
                match = re.search(r"version-[a-f0-9]+", line)
                return match.group(0), line if match else (None, None)
        return None, None
    except Exception as e:
        print(f"[ERROR] {e}")
        return None, None

def main():
    print("🔁 Starting Roblox version monitor loop...")
    session = requests.Session()
    last_version = read_saved_version()

    try:
        while True:
            current_version, line = get_latest_client_version(session)

            if current_version and current_version != last_version:
                print(f"\n[🆕] NEW VERSION: {current_version}")
                print(f"[ℹ️] Info: {line}")
                save_version(current_version)
                last_version = current_version
            else:
                print(f"[✅] No new version. Last known: {last_version}", end="\r")

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\n🛑 Exiting version watcher.")

if __name__ == "__main__":
    main()
