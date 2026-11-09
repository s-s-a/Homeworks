# editor.py
import flet as ft

def main(page: ft.Page):
    # --- Настройки окна ---
    page.title = "Flet Markdown Editor"
    page.window_width = 1200
    page.window_height = 800
    page.padding = 10
    
    # Устанавливаем светлую тему по умолчанию
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.title = "Markdown Редактор"

    # --- 1. Создаем функцию-обработчик ---
    def handle_text_change(e):
        # 'e' — это объект события, который Flet передает в функцию.
        # e.control — это ссылка на виджет, который вызвал событие (наш TextField).
        # e.control.value — это текущий текст в этом виджете.
        
        # Обновляем содержимое правой панели (preview_area)
        preview_area.value = e.control.value
        
        # --- 3. Самый важный шаг: обновляем страницу ---
        page.update()

    input_field = ft.TextField(
        multiline=True,
        expand=True,
        min_lines=40,
        hint_text="Пишите ваш Markdown здесь...",
        # --- 2. Привязываем обработчик к событию on_change ---
        on_change=handle_text_change,
    )

    preview_area = ft.Markdown(
        value="Здесь будет ваш **отформатированный** текст.",
        expand=True,
    )

    app_layout = ft.Row(
        controls=[
            input_field,
            ft.VerticalDivider(),
            preview_area
        ],
        expand=True,
    )

    page.add(app_layout)

if __name__ == "__main__":
    ft.app(target=main)