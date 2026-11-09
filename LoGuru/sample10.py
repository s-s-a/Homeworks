from loguru import logger
import uuid

# Создаем логгер с привязанным ID запроса
request_id = str(uuid.uuid4())
context_logger = logger.bind(request_id=request_id)

context_logger.info("Получен новый запрос.")
# ... какой-то код
context_logger.info("Данные из базы успешно получены.")
# ... еще код
context_logger.warning("Внешний API ответил с задержкой.")