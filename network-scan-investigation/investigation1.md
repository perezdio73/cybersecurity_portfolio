# Network Scan Investigation

## Objective

Investigate a controlled Nmap TCP SYN scan against a Kali Linux
system and analyze the network traffic using Wireshark.

## Environment

- Kali Linux
- Nmap
- Wireshark
- Controlled lab environment

## Investigation

### Source

[192.168.1.185]

### Destination

[104.18.213.185]

### Scan Type

TCP SYN scan (`-sS`)

### Targeted Ports

[443, 53]

### Packet Evidence

Wireshark was used to identify TCP SYN packets during
the scan.

### Observed Behavior

Multiple connection attempts were observed against different
destination ports.

### Analysis

The traffic pattern is consistent with the network to locate.
An attacker could use this type of scan to identify open
services before attempting any type of activity.

## Security Relevance

Port scanning can provide an attacker with information about
services exposed by the system.

## Recommendations

- Restrict any network exposure.
- Monitor unusual scanning.
- Use firewall rules to limit access to services.
- Investigate repeated scans from untrusted sources.

## Conclusion

The investigation demonstrates how network investigation appears
in packet captures and how Wireshark can be used to identify the
source, destination, protocols, and targeted ports in a scan.
