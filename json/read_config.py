import json

CONFIG_FILE = "config.json"

try:
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        # Загружаем всю конфигурацию из файла в один словарь
        config = json.load(f)

    # Теперь мы можем легко обращаться к любым параметрам
    print(f"Запускаем приложение: {config['app_name']} (версия {config['version']})")

    if config["debug_mode"]:
        print("Внимание: приложение запущено в режиме отладки!")

    db_host = config["database"]["host"]
    db_port = config["database"]["port"]
    print(f"Подключаемся к базе данных по адресу: {db_host}:{db_port}")

    print(f"Поддерживаемые фичи: {', '.join(config['supported_features'])}")

except FileNotFoundError:
    print(f"Ошибка: Файл конфигурации '{CONFIG_FILE}' не найден.")
except json.JSONDecodeError:
    print(
        f"Ошибка: Не удалось разобрать файл конфигурации '{CONFIG_FILE}'. Проверьте синтаксис JSON."
    )
except KeyError as e:
    print(f"Ошибка: В файле конфигурации отсутствует необходимый ключ: {e}")
