import flet as ft  # Import Flet


def main(page: ft.Page):
    page.title = "Data Table Example"  # Set window title

    # Define DataTable with columns and sample row data
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Text("ID")),
            ft.DataColumn(label=ft.Text("Name")),
            ft.DataColumn(label=ft.Text("Score")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text("Alice")),
                    ft.DataCell(ft.Text("90")),
                ]
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("2")),
                    ft.DataCell(ft.Text("Bob")),
                    ft.DataCell(ft.Text("85")),
                ]
            ),
        ],
    )

    page.add(data_table)  # Display table


ft.app(target=main)  # Start the GUI loop
