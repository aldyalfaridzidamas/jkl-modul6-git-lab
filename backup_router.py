#!/usr/bin/env python3
"""Backup konfigurasi perangkat jaringan melalui SSH."""
import os
import time

DEVICES = ["192.168.1.254", "192.168.1.253"]
SSH_PORT = 22
SSH_TIMEOUT = 60
RETRIES = 3
BACKUP_DIR = os.path.expanduser("~/backup")


def backup_device(ip):
    """Mengambil running-config dari perangkat (simulasi)."""
    print(f"SSH ke {ip} port {SSH_PORT} timeout {SSH_TIMEOUT}s")
    time.sleep(1)
    return f"hostname R-{ip.split('.')[-1]}\n!\nend\n"


def main():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    for ip in DEVICES:
        config = backup_device(ip)
        path = os.path.join(BACKUP_DIR, ip + ".cfg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(config)
        print("Backup " + ip + " -> " + path)


if __name__ == "__main__":
    main()
