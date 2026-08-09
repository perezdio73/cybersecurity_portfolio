# Firewall Defense Investigation

## Incident Type

Blocked network connection attempt.

## Environment

- Kali Linux
- UFW firewall
- Python HTTP server
- TCP/IP

## Objective

Decide whether the firewall suceeds in preventing
unauthorized access to restricted TCP service.

## Timeline

### Event 1 — Service Started

A Python HTTP server was started on TCP port 8080.

### Event 2 —  Test

A connection to port 8080 was succeeded
before the firewall restriction.

### Event 3 — Firewall Rule Applied

UFW was designed to deny incoming TCP traffic to port
8080.

### Event 4 — Connection Attempt

A second connection attempt was made against port 8080.

### Event 5 — Firewall Detection

The connection was blocked and the firewall event was
recorded.

## Source

[127.0.1.1]

## Destination

[127.0.1.1]

## Destination Port

8080

## Protocol

TCP

## Result

Blocked.

## Analysis

The firewall prevented any access to the
restricted service after the deny rule took place.

## Security

Restrict unnecessary services and use firewall rules to
limit the networks exposure.

Firewall rules should only follow the least of
privilege and only allowed required traffic.
