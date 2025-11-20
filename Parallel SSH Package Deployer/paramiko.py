#!/usr/bin/env python3
import paramiko
import json
import argparse
from concurrent.futures import ThreadPoolExecutor

def install_packages(ssh, packages):
    for pkg in packages:
        print(f"[+] Installing {pkg}...")
        stdin, stdout, stderr = ssh.exec_command(f"sudo apt install -y {pkg}")

        # Print output from remote host
        print(stdout.read().decode())
        print(stderr.read().decode())



def deploy(host_info, packages):
    host = host_info["host"]
    user = host_info["user"]
    password = host_info["password"]

    print(f"\n=== Connecting to {host} ({user}) ===")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, username=user, password=password)
        print(f"[+] Connected to {host}")

        install_packages(ssh, packages)

        ssh.close()
        print(f"[✓] Finished on {host}")

    except Exception as e:
        print(f"[!] Failed on {host}: {e}")



def main():
    parser = argparse.ArgumentParser(
        description="Parallel Linux Software Deployment Tool"
    )

    parser.add_argument(
        "--hosts",
        required=True,
        help="Path to JSON file with host credentials"
    )

    parser.add_argument(
        "--packages",
        required=True,
        nargs="+",
        help="List of packages to install"
    )

    args = parser.parse_args()

    # Load hosts JSON
    with open(args.hosts, "r") as f:
        hosts = json.load(f)

    # Parallel execution across all hosts
    with ThreadPoolExecutor(max_workers=10) as executor:
        for host_info in hosts:
            executor.submit(deploy, host_info, args.packages)


if __name__ == "__main__":
    main()
