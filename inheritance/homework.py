# Шаг 1
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} ест.")

    def sleep(self):
        print(f"{self.name} спит.")

    def make_sound(self):
        f"{self.name} издает звук."


# Шаг 2
class Dog(Animal):
    def __init__(self, name, age, breed):
        self.breed = breed
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} ГАВ!")

    def fetch(self):
        print(f"{self.name} приносит палку.")


# Шаг 3
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} МЯУ!")

    def purr(self):
        print(f"{self.name} мурлычет.")


# Шаг 4
class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def fly(self):
        print(f"{self.name} летит.")


class Parrot(Bird):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print("Кар! Я хороший!")


# Шаг 5

if __name__ == "__main__":
    dog = Dog("Шарик", 5, "Дворняга")
    cat = Cat("Мурка", 3)
    parrot = Parrot("Кеша", 2)

    zoo_animals = [dog, cat, parrot]
    for animal in zoo_animals:
        animal.make_sound()
