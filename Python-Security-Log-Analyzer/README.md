# Python Security Log Analyzer

## Overview

This project shows a Python based security log
analysis tool that is designed to seek  potentially suspicious activity.

The tool analyzes a controlled security log that extracts
failed authentication and identifies source IP
addresses and targeted usernames by its counts of activity and
generates alerts when a the source passes thresholds limits.

## Objective

Automate a repetitive security task that would
 require manually reviewing of authentication logs.

## Tools used

- Kali Linux
- Python 3
- Regular Expressions
- Linux command line

## Detection flow

```text
Security Log
     ↓
Python Parser
     ↓
Identify Failed Logins
     ↓
Extract IP / Username
     ↓
Count Attempts
     ↓
Compare Against Threshold
     ↓
Generate Alert
