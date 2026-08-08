# MITRE ATT&CK Mapping

## Technique

T1110 - Brute Force

## Description

Repeated authentication attempts were observed against
the SSH service.

## Evidence

The authentication logs contained multiple failed
SSH login attempts.

## Detection

The Python analysis script counted multiple failed authentication
attempts by source IP and generated an alert when the
configured threshold was exceeded.

## Recommended Detection

Monitor authentication logs for repeated failed
attempts
from the same source IP within a short period.
