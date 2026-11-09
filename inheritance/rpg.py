import random
import time


class Character:
    def __init__(self, name, health, damage):
        self.name = name
        self._health = health
        self._max_health = health  # Запомним максимум
        self.damage = damage

    @property
    def health(self):
        return 0 if self._health <= 0 else self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > self._max_health:
            self._health = self._max_health
        else:
            self._health = value
        print(f'Текущее здороыье {self._health}')

    def __str__(self):
        return f"{self.name} (HP: {self.health}, Dmg: {self.damage})"

    # Мы создаем "кнопку" для изменения здоровья
    def take_damage(self, damage):
        self.health -= damage

        # Внутри метода мы можем добавить ПРОВЕРКИ (Валидацию)
        if self.health < 0:
            self.health = 0

    def heal(self):
        self.health += 10
        # # Не даем вылечиться выше максимума!
        # if self._health > self._max_health:
        #     self._health = self._max_health

    def attack(self, other):
        print(f"⚔️ {self.name} наносит удар по {other.name}!")
        other.take_damage(self.damage)

    # Полезный метод, чтобы проверять, не закончилась ли игра
    def is_alive(self):
        return self.health > 0


class Hero(Character):
    # Мы не пишем __init__, он наследуется автоматически!

    def heal(self):
        # Лечим на 20% от текущего здоровья, но не больше 100 (условно)
        heal_amount = 10
        self.health += heal_amount
        print(
            f"✨ {self.name} применил магию и восстановил {heal_amount} HP. Теперь здоровья: {self.health}"
        )


class Enemy(Character):
    pass


class Warrior(Hero):
    def attack(self, other):
        # 20% шанс нанести критический урон (х2)
        if random.random() < 0.2:
            crit_damage = self.damage * 2
            print(f"⚔️ {self.name} делает ЯРОСТНЫЙ ВЫПАД! (Крит x2)")
            other.take_damage(crit_damage)
        else:
            # Если крит не выпал, бьем как обычно
            # super() обращается к родителю (Character) и берет его метод attack
            super().attack(other)


class Mage(Hero):
    def attack(self, other):
        # Магия игнорирует обычную защиту (в будущем), и выглядит эпично
        print(f"🔥 {self.name} кастует Огненный Шар в {other.name}!")
        other.take_damage(self.damage + 5)  # Маг бьет чуть больнее базового урона


# =============================================================================================

# 1. Создаем бойцов
hero = Character("Korg", 100, 20)
monster = Character("Goblin", 50, 10)

# 2. Проверяем статус
print(hero)
print(monster)
print("-" * 20)

# 3. Обмен любезностями
hero.attack(monster)  # Корг бьет Гоблина
monster.attack(hero)  # Гоблин дает сдачи
hero.attack(monster)  # Корг добивает
hero.attack(monster)  # Контрольный удар (проверка на 0 HP)

print("-" * 20)
print(f"Жив ли гоблин? {monster.is_alive()}")

# =============================================================================================

# Создаем персонажей через НОВЫЕ классы
player = Hero("Lancelot", 100, 20)  # Использует __init__ от Character
monster = Enemy("Dragon", 200, 5)  # Использует __init__ от Character

print("--- Битва началась ---")

# Герой атакует (метод взят у родителя)
player.attack(monster)

# Монстр атакует (метод взят у родителя)
monster.attack(player)

print("--- Ход героя ---")
# Герой решает подлечиться (УНИКАЛЬНЫЙ метод)
player.heal()

# А вот монстр так не может!
# monster.heal() # <--- Это вызовет ошибку: 'Enemy' object has no attribute 'heal'
# Создаем отряд
conan = Warrior("Conan", 150, 15)
gandalf = Mage("Gandalf", 80, 20)

# Список бойцов
party = [conan, gandalf]

# Создаем грушу для битья
dummy_monster = Character("Dummy", 500, 0)

print("--- Атака отряда ---")
for hero in party:
    # МАГИЯ ТУТ: Мы вызываем один и тот же метод attack()
    # Но каждый герой делает это по-своему!
    hero.attack(dummy_monster)

# 1. СОЗДАНИЕ БОЙЦОВ
# Игрок выбирает класс (в нашем коде жестко зададим Воина)
player = Warrior("Conan", 120, 15)

# Генерируем врага
enemy = Character("Goblin", 100, 10)

print("--- 🔔 БОЙ НАЧИНАЕТСЯ! ---")
print(player)
print(enemy)
print("-" * 30)

# 2. ИГРОВОЙ ЦИКЛ
# Битва идет, пока оба живы (используем метод is_alive, который мы писали ранее)
while player.is_alive() and enemy.is_alive():
    time.sleep(1.5)  # Пауза для драматизма

    # --- Ход Игрока ---
    # Нам не важно, Воин это или Маг. Метод attack() сам разберется, что делать.
    player.attack(enemy)

    # Проверка победы сразу после удара
    if not enemy.is_alive():
        print(f"\n🏆 {player.name} ОДЕРЖАЛ ПОБЕДУ!")
        break

    # --- Ход Врага ---
    enemy.attack(player)

    # Проверка поражения
    if not player.is_alive():
        print(f"\n💀 {player.name} пал в бою... Game Over.")
        break

    # --- Дополнительная логика (Фишка ООП) ---
    # Если герой сильно побит, он может попытаться полечиться
    # Проверяем: если здоровье меньше 30% и повезло с рандомом
    if player.health < 40 and random.random() < 0.3:
        print("   🚑 Герой пытается найти зелье...")
        player.heal()  # Этот метод есть только у Hero и его наследников!

print("-" * 30)
