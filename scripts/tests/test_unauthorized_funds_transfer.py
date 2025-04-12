from scripts.unauthorized_funds_transfer.unauthorized_funds_transfer import check_transfer_amount


def test_large_transfer():
    result = check_transfer_amount(15000)
    assert result["status"] == "suspicious"
    assert result["amount"] == 15000

def test_small_transfer():
    result = check_transfer_amount(500)
    assert result["status"] == "normal"