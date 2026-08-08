## Automation

A Pyrhon script was created to automate analysis of 
failed SSH authentication events.


The script:


1. Reads the authentication log.
2. Extracts source IP addresses.
3. Counts failed attempts by IP.
4. Compares activity against a defined threshold.
5. Generates an alert when an IP exceeds the threshold.

Tool:
failed_login_analysis.py


Output:
analysis_result.txt
