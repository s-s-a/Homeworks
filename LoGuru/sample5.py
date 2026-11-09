from loguru import logger

# Настраиваем логирование для продакшена:
# - Пишем в файл `prod.log`
# - Уровень - INFO и выше
# - Ротация при достижении 10 MB
# - Храним файлы 1 месяц
# - Сжимаем старые логи в .gz
logger.add("prod.log", level="INFO", rotation="10 MB", retention="1 month", compression="gz")

logger.info("Система запущена и готова к работе!")

user_id = 123
status = "success"

# Привычный и читаемый синтаксис
logger.info(f"Аутентификация для пользователя {id} прошла со статусом: {status}", id=user_id, status=status)