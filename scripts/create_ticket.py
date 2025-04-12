import uuid
import datetime

def create_ticket(incident_title, severity, account_number, description):
    ticket_id = str(uuid.uuid4())[:8]
    timestamp = datetime.datetime.now().isoformat()

    ticket = {
        "ticket_id": ticket_id,
        "created_at": timestamp,
        "title": incident_title,
        "severity": severity,
        "account_number": account_number,
        "description": description,
        "status": "Open"
    }

    # Simulated push to external banking incident management system
    print(f"[MOCK] Created incident ticket:\n{ticket}")
    return ticket

if __name__ == "__main__":
    create_ticket(
        incident_title="Suspicious Login Attempt Detected",
        severity="High",
        account_number="FI2112345600007890",
        description="Login from unusual location (Russia) for customer account. Failed 2FA attempt."
    )