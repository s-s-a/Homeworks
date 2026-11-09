from datetime import datetime

def calculate_age(birth_date_str):
    """
    Функция, которая принимает на вход строку с датой рождения в формате "ГГГГ-ММ-ДД" 
    и вычисляет, сколько полных лет исполнилось человеку на сегодняшний день.
    
    Args:
        birth_date_str (str): Дата рождения в формате "ГГГГ-ММ-ДД"
        
    Returns:
        int: Количество полных лет
    """
    return (datetime.now() - datetime.strptime(birth_date_str, "%Y-%m-%d")).days//365



if __name__ == "__main__":
    birth_date_str = '1965-06-11' # input("Введите дату рождения в формате ГГГГ-ММ-ДД: ")
    age = calculate_age(birth_date_str)
    print(f"Вам {age} лет.")