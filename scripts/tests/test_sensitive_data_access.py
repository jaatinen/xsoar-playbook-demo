from scripts.sensitive_data_access.sensitive_data_access import is_outside_work_hours


def test_access_at_night():
    assert is_outside_work_hours(2) == True

def test_access_during_day():
    assert is_outside_work_hours(10) == False