#!/usr/bin/env python3

import subprocess

# Define ANSI color codes
COLOR_INTERFACE = "\033[1;34m"   # Blue color for the interface name
COLOR_IPV4 = "\033[1;32m"        # Green color for the IPv4 address
COLOR_MAC = "\033[1;31m"         # Red color for the MAC address
COLOR_RESET = "\033[0m"          # Reset color back to default

# Run 'ip addr' command and capture its output
try:
    ip_output = subprocess.check_output(["ip", "addr"], text=True)
except subprocess.CalledProcessError as e:
    print(f"Failed to run 'ip addr': {e}")
    exit(1)

# Process output to highlight the desired fields
for line in ip_output.splitlines():
    if ":" in line and "link/" not in line:
        interface = line.split(":")[1].strip()
        print(line)
        print(f"\t\t{COLOR_INTERFACE}{interface}{COLOR_RESET}")
    elif "inet " in line:
        ipv4 = line.split()[1]
        print(line)
        print(f"\t{COLOR_IPV4}{ipv4}{COLOR_RESET}")
    elif "link/ether" in line:
        mac = line.split()[1]
        print(line)
        print(f"\t\t{COLOR_MAC}{mac}{COLOR_RESET}")
    else:
        print(line)
