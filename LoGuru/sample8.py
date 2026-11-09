from loguru import logger
import sys

logger.remove()

# Добавляем простой формат БЕЗ тегов
logger.add(sys.stderr, colorize=True, format=f"{time:HH:mm:ss} | {level} | {message}")

logger.info("Информационное сообщение.")
logger.warning("Сообщение с предупреждением.")
logger.error("Сообщение об ошибке.")


# Удаляем предыдущий обработчик
logger.remove()

# Создаем свой, очень подробный формат с тегами
custom_format = (
    f"<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    f"<level>{level: <8}</level> | " # <level> отвечает за цвет уровня
    f"<cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>" # и здесь тоже
)

logger.add(sys.stderr, format=custom_format, colorize=True)

logger.info("Лог в кастомном, снова цветном формате.")