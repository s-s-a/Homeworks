from enemy import Goblin, Dragon, Skeleton


class Hero:
    def __init__(self, name="Герой", health=200, damage=25):
        self.name = name
        self.health = health
        self.damage = damage
        print(f"Навстречу приключениям выходит {self.name} с {self.health} HP!\n")

    def attack(self, target):
        print(f"'{self.name}' наносит удар по '{target.name}', причиняя {self.damage} урона.")
        target.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            print(f"'{self.name}' пал в бою.")
        else:
            print(f"У '{self.name}' осталось {self.health} HP.")

    def is_alive(self):
        return self.health > 0


# Создаем нашего героя
hero = Hero(name="Сэр Уильям", health=500, damage=30)

# Создаем армию врагов
enemies = [
    Goblin(name="Вонючка", health=50, damage=10),
    Dragon(name="Игнис Пожиратель", health=250, damage=25, fire_breath_damage=50),
    Skeleton(name="Безымянный Страж", health=100, damage=15),
]

# --- Основной цикл боя ---
for enemy in enemies:
    print(f"\n--- {hero.name} встречает нового противника: {enemy.name}! ---")

    # Бой продолжается, пока оба участника живы
    while hero.is_alive() and enemy.is_alive():
        # Ход героя
        hero.attack(enemy)

        # Если враг еще жив после атаки героя, он отвечает
        if enemy.is_alive():
            enemy.attack(hero)
        print("-" * 20)  # Разделитель для наглядности

    if not hero.is_alive():
        print("Игра окончена. Враги победили.")
        break  # Завершаем цикл, если герой погиб
    else:
        print(f"{hero.name} одержал победу над {enemy.name}!")

# Финальное сообщение
if hero.is_alive():
    print(f"\nВеликая победа! {hero.name} выжил, одолев всех врагов!")
