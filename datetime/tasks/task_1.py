from datetime import datetime, timedelta

def calculate_return_date(days):
    """
    Функция, которая принимает на вход количество дней (например, 14) 
    и возвращает будущую дату, которая наступит через указанное количество дней 
    от текущего момента.
    
    Args:
        days (int): Количество дней от текущего момента
        
    Returns:
        datetime: Будущая дата
    """
    
    return datetime.now() + timedelta(days=days)

if __name__ == "__main__":
    print(f'Будущая дата на {calculate_return_date(5).strftime("%Y-%m-%d")}')
