# Firewall Defense & Traffic Analysis

## Overview

This project shows the model, testing, and
investigation of a Linux firewall using UFW.

A controlled HTTP service was exposed on TCP port 8080.
The status was tested before and after a firewall rule was
applied to show the effect of network access.

## Objective

- Configure a Linux firewall
- Enable  a network service
- Restrict any unnecessary service
- Generate network traffic
- Verify that the firewall blocks traffic
- Analyze firewall logs
- Document the security option

## Environment

- Kali Linux
- UFW
- Python HTTP server
- TCP/IP
- Linux command line

## Investigation Workflow

```text
Start HTTP Service
       ↓
Verify Port 8080
       ↓
      Test
       ↓
  Configure UFW
       ↓
  Deny TCP/8080
       ↓
Generate Connection
       ↓
Review Firewall Log
       ↓
  Verify Block
       ↓
    Document

