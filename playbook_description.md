# XSOAR Playbook Description

### 🎯 Goal
Automate triage of a phishing alert using the following steps:

1. **Trigger**: Email reported by user via phishing button
2. **Extract URL(s)** from email body
3. **Check URL reputation** using external API (`check_url_reputation.py`)
4. **If malicious**, create a ticket in external ticketing system (mock)
5. **Update incident status** in XSOAR

### 🔄 Decision Points
- If URL is malicious → escalate
- If URL is clean → close as false positive
