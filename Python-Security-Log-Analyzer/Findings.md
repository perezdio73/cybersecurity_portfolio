# Python Security Log Analysis

## Objective

The objective of this project was to create a Python script
able of automatically analyzing authentication logs and
identify potentially suspicious login activity.

## Problem

Manually reviewing large authentication logs can be
time wasting for a security analyst.

The script was designed to automate basic analysis by
identifying failed attempts by extracting source IP addresses and usernames, counting activity,
and flagging sources that push a threshold limits.

## Detection Logic

The script:

1. Reads the security log.
2. Searches for failed password events.
3. Extracts source IP addresses.
4. Extracts targeted usernames.
5. Counts failed attempts.
6. Compares IP activity against a threshold.
7. Generates an alert for suspicious activity.

## Results

The analysis identified:

- Total failed attempts: 6
- Most active source: 192.168.1.50
- Failed attempts from that source: 4
- Threshold: 3 attempts
- Alert generated: Yes

## Security Relevance

Repeated failed attempts can be an indicator of credential attacks or brute force activity.

Automating this type of analysis can help security analysts
identify suspicious activity more efficiently.

## Future Improvements

Possible improvements include:

- Detecting activity within a specific time
- Reading real time logs
- Adding danger levels
- Generating CSV reports
- Combine the detection with a SIEM
- Sending alerts when thresholds are pass their limits

## Conclusion

This project demonstrates how Python can be used to automate
basic security log analysis and locate suspicious activity.
