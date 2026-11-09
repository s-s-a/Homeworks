from loguru import logger

logger.add("structured_data.log", serialize=True)

user_data = {"id": 123, "name": "John Doe"}
logger.info(f"Пользователь {user} обновил профиль", user=user_data)