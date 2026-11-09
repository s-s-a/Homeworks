from datetime import datetime


def analyze_timestamps(start_time, end_time):
    """
    Функция, которая принимает две строки с временными метками:
    start_time = "2025-09-26 10:55:00" и end_time = "2025-09-26 11:07:30".
    Вычисляет разницу между ними и возвращает результат в виде строки:
    "Операция заняла: 12 минут 30 секунд.".

    Args:
        start_time (str): Начальное время в формате "ГГГГ-ММ-ДД ЧЧ:ММ:СС"
        end_time (str): Конечное время в формате "ГГГГ-ММ-ДД ЧЧ:ММ:СС"

    Returns:
        str: Строка с разницей во времени
    """
    diff_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S") - datetime.strptime(
        start_time, "%Y-%m-%d %H:%M:%S"
    )
    return (
        f"Операция заняла: {diff_time.seconds//60} минут {diff_time.seconds%60} секунд."
    )


if __name__ == "__main__":
    print(analyze_timestamps("2025-09-26 10:55:00", "2025-09-26 11:07:30"))
