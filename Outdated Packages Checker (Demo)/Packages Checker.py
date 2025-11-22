#!/usr/bin/env python3
import subprocess

def run_command(command):
    """Run a shell command and return its output as text."""
    try:
        return subprocess.getoutput(command)
    except Exception as e:
        print(f"Error running command: {e}")
        return ""

def get_upgradable_packages():
    """
    Returns a list of tuples: (package_name, installed_version, available_version)
    """
    outdated = []
    output = run_command("apt list --upgradable 2>/dev/null")

    for line in output.splitlines():
        if "upgradable" in line and "/" in line:
            parts = line.split()
            pkg_name = parts[0].split("/")[0]         # package name
            new_version = parts[1]                     # version in repo
            old_version = parts[-1].replace("]", "").split(":")[1]  # installed version
            outdated.append((pkg_name, old_version, new_version))

    return outdated

def main():
    print("Checking for outdated packages...\n")
    outdated = get_upgradable_packages()

    if not outdated:
        print("All packages are up to date! 🎉")
        return

    print("=== Outdated Packages ===")
    for pkg_name, old_ver, new_ver in outdated:
        print(f"{pkg_name}: {old_ver} → {new_ver}")

    # Optional: save to a file
    with open("outdated_packages.txt", "w") as f:
        for pkg_name, old_ver, new_ver in outdated:
            f.write(f"{pkg_name}: {old_ver} → {new_ver}\n")
    print("\nResults saved to outdated_packages.txt")

if __name__ == "__main__":
    main()
