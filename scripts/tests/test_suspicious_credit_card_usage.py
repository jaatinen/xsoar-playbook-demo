from scripts.suspicious_credit_card_usage.suspicious_credit_card_usage import is_suspicious_location


def test_foreign_country():
    assert is_suspicious_location("Russia", ["Finland", "Sweden"]) == True

def test_allowed_country():
    assert is_suspicious_location("Finland", ["Finland", "Sweden"]) == False