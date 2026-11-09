# editor.py
import flet as ft

def main(page: ft.Page):
    page.title = "Markdown Редактор"

    # 1. Поле для ввода Markdown текста
    input_field = ft.TextField(
        multiline=True, # Позволяет вводить несколько строк текста
        expand=True,    # Растягивает поле на всю доступную высоту и ширину
        min_lines=40,   # Задает минимальную высоту, чтобы окно не было слишком маленьким
        hint_text="Пишите ваш Markdown здесь..." # Подсказка для пользователя
    )

    # 2. Область для отображения отформатированного результата
    preview_area = ft.Markdown(
        value="Здесь будет ваш **отформатированный** текст.",
        expand=True, # Также растягиваем на все доступное пространство
    )

    # 3. Собираем все в один горизонтальный ряд
    app_layout = ft.Row(
        # `controls` — это список дочерних элементов
        controls=[
            input_field,
            ft.VerticalDivider(), # Аккуратный вертикальный разделитель
            preview_area
        ],
        expand=True, # Растягиваем сам ряд на все окно
    )

    page.add(app_layout)

if __name__ == "__main__":
    ft.app(target=main)