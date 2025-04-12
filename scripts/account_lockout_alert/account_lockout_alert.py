def should_lock_account(failed_attempts, threshold=5):
    return failed_attempts >= threshold