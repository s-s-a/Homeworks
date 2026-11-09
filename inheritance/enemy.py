# Враг
import random


class Enemy:
    # Метод-конструктор, который вызывается при создании нового объекта
    def __init__(self, name, health, damage):
        self.name = name
        self._health = health
        self._damage = damage
        print(f"Враг '{self.name}' с {self.health} HP появился в мире!")

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        pass
        # Здесь можно добавить логику для проверки здоровья и реагирования на изменения

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, value):
        pass

    # Метод для атаки на какую-либо цель (target)
    def attack(self, target):
        print(f"'{self.name}' атакует {target.name} и наносит {self.damage} урона!")
        target.take_damage(self.damage)

    # Метод для получения урона
    def take_damage(self, amount):
        self._health -= amount
        if self._health <= 0:
            self._health = 0  # Здоровье не может быть отрицательным
            print(f"'{self.name}' получил {amount} урона и был побежден.")
        else:
            print(f"У '{self.name}' осталось {self.health} HP.")

    # Метод для проверки, жив ли враг
    def is_alive(self):
        return self._health > 0


# Гоблин
# А вот и наш первый наследник!
class Goblin(Enemy):
    # Переопределяем метод attack
    def attack(self, target):
        print(
            f"'{self.name}' трусливо тычет в {target.name} своим ржавым кинжалом, нанося {self.damage} урона!"
        )
        target.take_damage(self.damage)  # Логика нанесения урона остается той же


# Дракон
class Dragon(Enemy):
    def __init__(self, name, health, damage, fire_breath_damage):
        # 1. Вызываем __init__ родительского класса (Enemy)
        #    и передаём ему те параметры, за которые он отвечает.
        super().__init__(name, health, damage)

        # 2. А теперь добавляем новый, уникальный атрибут для Дракона.
        self.fire_breath_damage = fire_breath_damage

    def breathe_fire(self, target):
        print(
            f"'{self.name}' выдыхает пламя на {target.name}, нанося {self.fire_breath_damage} урона!"
        )
        target.take_damage(self.fire_breath_damage)

    def attack(self, target):
        # Сначала выполняем обычную атаку из родительского класса
        super().attack(target)

        # А потом добавляем новое действие
        print(f"Вдобавок '{self.name}' опаляет {target.name} своим дыханием!")
        target.take_damage(
            self.fire_breath_damage // 2
        )  # Например, половину урона от спец. атаки


# Нежить
class Undead(Enemy):
    # Переопределим получение урона, чтобы добавить "атмосферы"
    def take_damage(self, amount):
        print(f"'{self.name}' не чувствует боли, но получает {amount} урона.")
        # Вызываем оригинальный метод take_damage из класса Enemy, чтобы не дублировать логику
        super().take_damage(amount)

    # Добавим уникальный метод для всей нежити
    def scare(self, target):
        print(f"'{self.name}' издает леденящий душу стон, пугая {target.name}!")


# Скелет

# (Классы Enemy и Undead определены выше)


class Skeleton(Undead):
    def __init__(self, name, health, damage):
        # Используем super() для вызова конструктора родителя (в данном случае, Undead)
        super().__init__(name, health, damage)

    # Переопределяем метод take_damage ещё раз!
    def take_damage(self, amount):
        # С вероятностью 30% (0.3) скелет полностью избегает урона
        if random.random() < 0.3:
            print(f"Атака проходит сквозь кости '{self.name}', не нанося урона!")
        else:
            # Если увернуться не удалось, вызываем логику родителя (Undead)
            super().take_damage(amount)


# Вспомогательный класс для демонстрации
class Hero:
    def __init__(self, name="Герой", health=100):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        print(f"У '{self.name}' осталось {self.health} здоровья.\n")


if __name__ == "__main__":
    # --- Теперь используем наш класс Enemy ---

    # Создаем объекты
    hero = Hero()
    generic_enemy = Enemy(name="Обычный скелет", health=40, damage=10)

    # Проверяем, жив ли враг
    print(f"Статус врага: {'Жив' if generic_enemy.is_alive() else 'Мертв'}")

    # Враг атакует героя
    generic_enemy.attack(hero)

    # Герой наносит ответный удар
    print(f"'{hero.name}' наносит ответный удар!")
    generic_enemy.take_damage(25)

    # Снова проверяем статус
    print(f"Статус врага: {'Жив' if generic_enemy.is_alive() else 'Мертв'}")

    # Создаём объект класса Goblin
    hero = Hero()
    goblin = Goblin(name="Вредный гоблин", health=30, damage=5)

    # Проверяем, что он унаследовал методы родителя
    goblin.attack(hero)
    print(f"Жив ли гоблин? {'Да' if goblin.is_alive() else 'Нет'}")

    # Создаем объекты
    generic_enemy = Enemy("Солдат", 100, 15)
    goblin = Goblin("Вредный гоблин", 30, 5)
    hero = Hero()

    # Сравниваем их атаки
    generic_enemy.attack(hero)
    goblin.attack(hero)

    # --- Проверяем Дракона в бою ---

    hero = Hero("Рыцарь", 250)
    dragon = Dragon(name="Игнис", health=300, damage=20, fire_breath_damage=40)

    # Дракон выполняет свою расширенную атаку
    dragon.attack(hero)

    # Дракон использует свою уникальную способность
    dragon.breathe_fire(hero)

    # --- Проверим Скелет в бою ---

    hero = Hero("Паладин", 300)
    skeleton = Skeleton(name="Костяной воин", health=80, damage=12)

    # 1. Метод из самого "дальнего" предка - Enemy
    skeleton.attack(hero)

    # 2. Метод из промежуточного родителя - Undead
    skeleton.scare(hero)

    # 3. Уникальный, переопределенный метод самого Skeleton
    #    (результат может меняться из-за случайности)
    print("\nПаладин атакует скелета...")
    skeleton.take_damage(20)
    skeleton.take_damage(20)
    skeleton.take_damage(20)
