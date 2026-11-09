from loguru import logger

logger.add("my_app.log")

logger.info("Это сообщение попадет и в консоль, и в файл my_app.log")