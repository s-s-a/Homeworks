from plyer import notification


def send_notification(title: str, message: str):
    """
    Отправляет системное уведомление.

    :param title: Заголовок уведомления (например, тип задачи)
    :param message: Основной текст напоминания
    """
    notification.notify(
        title=title,
        message=message,
        app_name="Task Manager",
        # app_icon='icon.ico',  # Путь к иконке (должен быть абсолютным или в той же папке)
        timeout=10,  # Время отображения уведомления в секундах
    ) # type: ignore


# Тестовый вызов для проверки работы системы
if __name__ == "__main__":
    send_notification("Проверка системы", "Уведомления настроены и работают корректно.")
