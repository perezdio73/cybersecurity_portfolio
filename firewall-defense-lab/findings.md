# Firewall Defense Findings

## Finding 1 — Restricted TCP Port

### Observation

TCP port 8080 was purposely exposed by a local Python
HTTP server during the lab.

### Baseline

The service can be reached  before the firewall restriction
was applied.

### Control Implemented

A UFW rule was created to deny incoming TCP connections
to the port 8080.

### Verification

A following  connection attempt to port 8080 failed after
the firewall rule was applied.

### Security Impact

Restricting any unnecessary network services reduces the
number of open services and that
reduces the potential attack surface.

### Recommendation

Only expose services that are required and restricted
to trusted networks or hosts.
