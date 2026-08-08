import re
from collections import Counter

LOG_FILE = "security.log"
THRESHOLD = 3

failed_attempts = []

with open(LOG_FILE, "r") as file:
    for line in file:
        if "Failed password" in line:

            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            user_match = re.search(r"for (\S+)", line)

            if ip_match and user_match:
                ip = ip_match.group(1)
                username = user_match.group(1)

                failed_attempts.append((ip, username))

ip_counts = Counter(ip for ip, username in failed_attempts)
user_counts = Counter(username for ip, username in failed_attempts)

print("================================")
print(" SECURITY LOG ANALYZER")
print("================================")

print(f"\nTotal failed login attempts: {len(failed_attempts)}")

print("\nFailed attempts by IP:")
for ip, count in ip_counts.items():
    print(f"  {ip}: {count}")

print("\nTargeted usernames:")
for username, count in user_counts.items():
    print(f"  {username}: {count}")

print("\nPotentially suspicious sources:")

alerts = 0

for ip, count in ip_counts.items():
    if count >= THRESHOLD:
        print(f"  ALERT: {ip} - {count} failed attempts")
        alerts += 1

if alerts == 0:
    print("  No sources exceeded the threshold.")

print("\nAnalysis complete.")
