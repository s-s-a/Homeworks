from loguru import logger

try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("Произошла ошибка при вычислении.")
