import asyncio
import time

async def make_coffee():
    print("Начинаю делать кофе")
    await asyncio.sleep(3)
    print("Кофе готов!")

async def toast_bread():
    print("Начинаю делать тост")
    await asyncio.sleep(2)
    print("Тост готов!")

async def main():
    start_time = time.time()

    # Создаем "корзину" задач, которые должны выполниться одновременно
    # asyncio.gather запускает их все и ждет, пока последняя не завершится
    await asyncio.gather(make_coffee(), toast_bread())
    
    end_time = time.time()
    print(f"Завтрак приготовлен за {end_time - start_time:.2f} секунд")

asyncio.run(main())