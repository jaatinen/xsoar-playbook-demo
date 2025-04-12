def check_transfer_amount(amount, threshold=10000):
    if amount > threshold:
        return {"status": "suspicious", "amount": amount}
    return {"status": "normal", "amount": amount}