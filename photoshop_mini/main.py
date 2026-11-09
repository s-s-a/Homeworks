import flet as ft
from PIL import Image, ImageFilter
import io
import base64


def main(page: ft.Page):
    # --- НАСТРОЙКИ ОКНА ---
    page.title = "Flet Image Editor"
    page.window_width = 600
    page.window_height = 800
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.snack_bar = ft.SnackBar(content=ft.Text("Сообщение!"))

    # --- ПЕРЕМЕННЫЕ СОСТОЯНИЯ ---
    current_image: Image = None

    # --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---
    def update_image_view(img_obj: Image):
        """Конвертирует объект Pillow в base64 и обновляет виджет."""
        buffer = io.BytesIO()
        img_obj.save(buffer, format="PNG")
        base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")
        image_view.src_base64 = base64_img
        page.update()

    # --- ОБРАБОТЧИКИ СОБЫТИЙ ---
    def on_file_picker_result(e: ft.FilePickerResultEvent):
        nonlocal current_image
        if e.files:
            file_path = e.files[0].path
            current_image = Image.open(file_path)
            image_view.src = file_path
            image_view.visible = True
            filters_row.visible = True
            save_button.disabled = False
            page.update()

    def on_save_file_result(e: ft.FilePickerResultEvent):
        if e.path and current_image:
            try:
                current_image.save(e.path)
                page.snack_bar.content = ft.Text(
                    f"Изображение успешно сохранено в {e.path}"
                )
                page.snack_bar.open = True
                page.update()
            except Exception as ex:
                page.snack_bar.content = ft.Text(f"Ошибка при сохранении: {ex}")
                page.snack_bar.open = True
                page.update()

    def apply_bw_filter(e):
        nonlocal current_image
        if current_image:
            current_image = current_image.convert("L")
            update_image_view(current_image)

    def apply_blur_filter(e):
        nonlocal current_image
        if current_image:
            current_image = current_image.filter(ImageFilter.BLUR)
            update_image_view(current_image)

    def apply_rotate_filter(e):
        nonlocal current_image
        if current_image:
            current_image = current_image.rotate(90, expand=True)
            update_image_view(current_image)

    # --- FILE PICKERS ---
    open_file_picker = ft.FilePicker(on_result=on_file_picker_result)
    save_file_picker = ft.FilePicker(on_result=on_save_file_result)
    page.overlay.extend([open_file_picker, save_file_picker])

    # --- ВИДЖЕТЫ ИНТЕРФЕЙСА ---
    open_button = ft.ElevatedButton(
        "Открыть",
        on_click=lambda _: open_file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["jpg", "jpeg", "png", "bmp"],
            dialog_title="Выберите изображение",
        ),
    )
    save_button = ft.ElevatedButton(
        "Сохранить",
        disabled=True,
        on_click=lambda _: save_file_picker.save_file(
            dialog_title="Сохранить как...",
            file_name="edited_image.png",
            allowed_extensions=["png", "jpg", "bmp"],
        ),
    )

    image_view = ft.Image(
        visible=False,
        width=500,
        height=500,
        fit=ft.ImageFit.CONTAIN,
    )

    filters_row = ft.Row(
        controls=[
            ft.ElevatedButton("Ч/Б", on_click=apply_bw_filter),
            ft.ElevatedButton("Размытие", on_click=apply_blur_filter),
            ft.ElevatedButton("Поворот", on_click=apply_rotate_filter),
        ],
        visible=False,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    # --- СБОРКА ИНТЕРФЕЙСА ---
    page.add(
        ft.Row([open_button, save_button], alignment=ft.MainAxisAlignment.CENTER),
        image_view,
        filters_row,
    )


# --- ЗАПУСК ПРИЛОЖЕНИЯ ---
ft.app(target=main)
