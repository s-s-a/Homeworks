import re


def main():
    print("Hello from re-homework!")


if __name__ == "__main__":
    main()

# ❌ ТАК НЕЛЬЗЯ (вызовет ошибку re.error: look-behind requires fixed-width pattern)
# Мы пытаемся заглянуть назад на неизвестное количество букв (\w+)
# re.search(r'(?<=\w+: )\d+', "Price: 100") 

# ✅ А ТАК МОЖНО
# Мы точно знаем, что ищем ровно 7 символов "Price: "
re.search(r'(?<=Price: )\d+', "Price: 100")