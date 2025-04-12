from scripts.account_lockout_alert.account_lockout_alert import should_lock_account

def test_should_lock():
    assert should_lock_account(6) == True

def test_should_not_lock():
    assert should_lock_account(2) == False