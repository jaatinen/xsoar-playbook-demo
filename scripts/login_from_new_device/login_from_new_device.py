def is_known_device(user_id, device_id, known_devices):
    return device_id in known_devices.get(user_id, [])