def log_event(event_type, *details, **metadata):
    """
    Логирует событие с обязательным типом, опциональными деталями
    и опциональными метаданными.
    """
    print(f"[ТИП СОБЫТИЯ]: {event_type}")

    if details:
        # details - это кортеж
        print("[ДЕТАЛИ]:")
        for detail in details:
            print(f"  - {detail}")

    if metadata:
        # metadata - это словарь
        print("[МЕТАДАННЫЕ]:")
        for key, value in metadata.items():
            print(f"  - {key}: {value}")

# Пример вызова функции со всеми типами аргументов
log_event(
    "USER_LOGIN_SUCCESS",                        # pos_arg1
    "user_id:101", "ip_address:192.168.1.100",    # *args
    request_id="abc-123-xyz", status_code=200     # **kwargs
)