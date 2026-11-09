from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, PostgresDsn


class Settings(BaseSettings):
    # Pydantic сам найдет переменную BOT_TOKEN в окружении
    bot_token: SecretStr

    # Автоматически соберет URL для базы данных и проверит формат
    database_url: PostgresDsn

    # Превратит строки "true", "1", "yes" в Python True
    debug_mode: bool = False

    # Указание читать файл .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# В момент инициализации произойдет магия:
# 1. Загрузится .env
# 2. Прочитаются системные переменные
# 3. Все типы будут приведены и проверены
try:
    config = Settings() # pyright: ignore[reportCallIssue]
    print("Конфигурация загружена успешно!")
except Exception as e:
    print("Ошибка конфигурации! Приложение не может запуститься.")
    print(e)
