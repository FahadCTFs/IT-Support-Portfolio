#!/usr/bin/env python3
"""
Simple ICMP Packet Loss Monitor
"""

import os
import time
import subprocess
import argparse

targets = []
interval = 3
packet_count = 3

def ping_host(host):
    try:
        result = subprocess.run(
            ["ping", "-c", str(packet_count), "-W", "1", host],
            capture_output=True,
            text=True,
            timeout=10
        )

        for line in result.stdout.split('\n'):
            if "packet loss" in line:
                loss = line.split('%')[0].split(' ')[-1]
                return int(loss)

        return 100

    except (subprocess.TimeoutExpired, Exception):
        return 100

def main():
    parser = argparse.ArgumentParser(description='ICMP Packet Loss Monitor')
    parser.add_argument('--dns', type=str, help='DNS hostname to monitor (e.g., google.com)')
    parser.add_argument('--ip', type=str, help='IP address to monitor (e.g., 8.8.8.8)')
    args = parser.parse_args()
    
    # Add targets based on command line arguments
    if args.dns:
        targets.append(args.dns)
    if args.ip:
        targets.append(args.ip)
    
    # If no targets specified, use defaults
    if not targets:
        targets.extend(["8.8.8.8", "google.com", "1.1.1.1"])
    
    print("Simple ICMP Packet Loss Monitor")
    print("=" * 40)
    print(f"Monitoring: {', '.join(targets)}")
    print(f"Interval: {interval}s | Packets: {packet_count}")
    print("Press Ctrl+C to stop\n")

    try:
        while True:
            print(f"\n{time.strftime('%H:%M:%S')} - Checking...")
            print("-" * 40)

            for target in targets:
                loss = ping_host(target)

                if loss == 0:
                    status = "✅ EXCELLENT"
                elif loss < 10:
                    status = "⚠️  GOOD" 
                elif loss < 30:
                    status = "🔶 FAIR"
                elif loss < 100:
                    status = "🔴 POOR"
                else:
                    status = "❌ DOWN"

                print(f"{target:15} {loss:2}% loss {status}")
            
            print(f"\nNext check in {interval} seconds...")
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")

if __name__ == "__main__":
    main()
