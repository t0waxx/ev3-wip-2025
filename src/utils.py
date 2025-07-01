def log(message: str) -> None:
    import datetime
    now = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{now}] {message}")
