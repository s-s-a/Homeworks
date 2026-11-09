from loguru import logger

@logger.catch
def calculate(a, b, c):
    return a / b + c

calculate(10, 0, 5) # Эта строка вызовет ошибку