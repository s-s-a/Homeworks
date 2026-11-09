import time
import schedule
from plyer import notification


def send_notification(title:str, message:str):
    """
    Универсальная функция отправки уведомлений.
    """
    try:
        notification.notify(
            title=title, message=message, app_name="My Task Manager", timeout=10
        ) # type: ignore
    except Exception as e:
        print(f"Ошибка отправки уведомления: {e}")


# --- Функции-обработчики задач ---


def morning_standup():
    send_notification(
        "Daily Meeting", "Подключайся к Zoom. Подготовь статус по задачам."
    )


def check_services():
    # В реальном проекте здесь был бы код: response = requests.get('http://localhost:8000')
    # Мы эмулируем проверку
    print("[LOG] Проверка сервисов выполнена.")
    send_notification(
        "System Monitor", "Локальные сервисы работают штатно. Очередь задач пуста."
    )


def log_work_time():
    send_notification(
        "Конец рабочего дня", "Не забудь списать часы в трекер и запушить код."
    )


# --- Конфигурация планировщика ---


def run_scheduler():
    # 1. Утренний митинг (фиксированное время)
    schedule.every().day.at("10:00").do(morning_standup)

    # 2. Периодическая проверка (интервал)
    schedule.every(2).hours.do(check_services)

    # 3. Закрытие задач (фиксированное время)
    schedule.every().day.at("18:00").do(log_work_time)

    print("Планировщик запущен. Нажмите Ctrl+C для остановки.")

    # Основной цикл событий (Event Loop)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    run_scheduler()
