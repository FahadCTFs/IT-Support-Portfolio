#!/usr/bin/env python3
import psutil
import time
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def kbps(bytes_per_sec):
    return bytes_per_sec / 1024

def main():
    print("Starting NetWatch...")
    time.sleep(1)

    old = psutil.net_io_counters()

    while True:
        time.sleep(1)

        new = psutil.net_io_counters()

        rx = new.bytes_recv - old.bytes_recv
        tx = new.bytes_sent - old.bytes_sent

        clear()
        print("=== NetWatch - Real-Time Bandwidth Monitor ===\n")
        print(f"Download: {kbps(rx):.2f} KB/s")
        print(f"Upload  : {kbps(tx):.2f} KB/s")

        old = new

if __name__ == "__main__":
    main()
