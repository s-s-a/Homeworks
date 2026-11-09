import asyncio
import time

async def make_coffee():
    print("Начинаю делать кофе")
    await asyncio.sleep(3) # Имитация долгой работы (3 сек)
    print("Кофе готов!")

async def toast_bread():
    print("Начинаю делать тост")
    await asyncio.sleep(2) # Имитация долгой работы (2 сек)
    print("Тост готов!")

async def main():
    start_time = time.time()

    # Последовательно ждем выполнения каждой корутины
    await make_coffee()
    await toast_bread()
    
    end_time = time.time()
    print(f"Завтрак приготовлен за {end_time - start_time:.2f} секунд")

asyncio.run(main())