# main.py
from app.logging_config import setup_logging
from loguru import logger

# Вызываем настройку в самом начале работы приложения
setup_logging()

@logger.catch
def main_logic():
    logger.info("Приложение начинает работу.")
    logger.debug("Это отладочное сообщение, которое не попадет в прод-консоль, но попадет в прод-файл.")
    # ... ваш основной код ...

if __name__ == "__main__":
    main_logic()