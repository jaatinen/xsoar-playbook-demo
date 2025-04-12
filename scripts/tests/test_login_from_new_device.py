from scripts.login_from_new_device import is_known_device

def test_known_device():
    known = {"user123": ["dev001", "dev002"]}
    assert is_known_device("user123", "dev001", known) == True

def test_unknown_device():
    known = {"user123": ["dev001", "dev002"]}
    assert is_known_device("user123", "dev999", known) == False