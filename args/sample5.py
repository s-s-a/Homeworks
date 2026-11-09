class BaseComponent:
    def __init__(self, name, **kwargs):
        print(f"BaseComponent __init__ с {name=} и {kwargs=}")
        self.name = name
        self.config = kwargs

class AdvancedComponent(BaseComponent):
    def __init__(self, name, version, **kwargs):
        print(f"AdvancedComponent __init__ с {name=}, {version=} и {kwargs=}")
        # Мы явно обрабатываем 'version', а остальное проксируем в родительский класс
        super().__init__(name, **kwargs)
        self.version = version

# Если в будущем в BaseComponent добавят новый параметр, например, 'enabled=True',
# AdvancedComponent продолжит работать корректно.

# Пример: 'author' и 'license' не объявлены ни в одном из конструкторов,
# но они будут корректно обработаны и собраны в **kwargs.
adv = AdvancedComponent("Logger", version="2.1", author="John Doe", license="MIT")