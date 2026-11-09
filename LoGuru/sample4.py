# Создавать новый файл, как только текущий достигнет 500 MB
logger.add("big_file.log", rotation="500 MB")

# Создавать новый файл каждую неделю
logger.add("weekly_log.log", rotation="1 week")

# Создавать новый файл каждый день в полночь
logger.add("daily_log.log", rotation="00:00")


# Хранить логи за последние 10 дней
logger.add("cleaned_log.log", retention="10 days")


# При ротации сжимать старые файлы в zip-архив
logger.add("compressed_log.log", rotation="10 MB", compression="zip")


