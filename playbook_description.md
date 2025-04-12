# Cortex XSOAR Playbook – Banking Use Case

### Use Case: Suspicious Login Attempt in Online Banking

This playbook is triggered when a suspicious login is detected for a customer’s online banking account. The goal is to automate the triage and escalation process to reduce fraud investigation time and ensure rapid response.

---

## Playbook Flow

1. **Trigger**
   - Event is triggered from SIEM when a login is attempted from an unusual geo-location or blacklisted IP address.

2. **Enrichment**
   - Perform GeoIP lookup on the source IP.
   - Extract the bank account number and user ID from the alert metadata.

3. **Reputation Check**
   - Run the IP through a threat intelligence source (e.g., Palo Alto Autofocus, VirusTotal).
   - If the IP is flagged as malicious or suspicious, proceed to escalation.

4. **Decision Logic**
   - If:
     - GeoIP ≠ usual country AND
     - IP reputation = malicious or suspicious
     - → Escalate as potential fraud attempt
   - Else:
     - → Close alert and log as benign anomaly

5. **Action**
   - Automatically create a ticket using the `create_ticket.py` automation script.
   - Include all relevant information (IP, geo-location, customer ID, account number).

6. **Update Incident**
   - Update case in XSOAR with ticket ID, status, and fraud analyst assignment.
   - Notify fraud team via email or ticket system.

---

## Scripts Used

- `check_url_reputation.py` – for mock threat intelligence check
- `create_ticket.py` – for simulating ticket creation to fraud investigation system

---

## Example Data (Mock)

| Field           | Value                        |
|----------------|------------------------------|
| IP Address      | 45.83.1.12                   |
| Country         | Finland                      |
| Customer ID     | 987654                       |
| Account Number  | FI2112345600007890           |
| Event Type      | Failed Login                 |
| Risk Level      | High                         |

---

## Notes

This playbook demonstrates a typical security automation use case in the banking/financial sector. It can be adapted to work with Cortex XSOAR’s visual playbook editor and deployed with integrations like:

- Palo Alto Threat Intelligence
- Jira or ServiceNow
- Banking-specific case management systems