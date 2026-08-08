import re
from collections import Counter

log_file = "failed_logins.txt"

ip_addresses = []

with open (log_file, "r") as file:
    for line in file:
       match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)


       if match:
           ip_addresses. append(match.group(1))

ip_counts = Counter (ip_addresses)

print("SSH Failed Login Analysis")
print("=========================")

total_attempts = len(ip_addresses)

print (f"Total failed attempts: {total_attempts}")
print()

print("Attempts by source IP: ")

for ip, count in ip_counts.items ():
    print(f"{ip}: {count}")

print()

threshold = 3

print (f"IPs with more than {threshold} failed attempts:")

for ip, count in ip_counts.items():
    if count > threshold:
        print(f"ALERT: {ip} had {count} failed attempts")
