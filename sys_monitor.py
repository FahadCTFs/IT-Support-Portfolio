#!/usr/bin/env python3
"""
Simple System Monitor
"""

import psutil
import time

def main():
    print("System Monitor - Press Ctrl+C to stop\n")
    
    try:
        while True:
            # Get usage
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            
            # Display
            print(f"CPU: {cpu:5.1f}% | RAM: {ram:5.1f}%", end="")
            
            # Alerts
            if cpu > 80:
                print(" 🚨 CPU HIGH", end="")
            if ram > 85:
                print(" 🚨 RAM HIGH", end="")
            
            print()  # New line
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\nMonitor stopped.")

if __name__ == "__main__":
    main()