import flet as ft
from database import Database

def main(page: ft.Page):
    db = Database("db.sqlite")
    page.title = "Ваши контакты"
    page.scroll = "auto"

    сontact_input = ft.TextField(label="Имя контакта", width=180)
    number_input = ft.TextField(label="Номер телефона", width=180)
    additionally_input = ft.TextField(label="Дополнительная пометка(может быть пустой)", width=180)

    contacts_list = ft.Column()

    def load_contacts():
        contacts_list.controls.clear()
        for contact in db.get_contact():
            contacts_list.controls.append(
                ft.Row(
                    controls=[
                        ft.Text(f"{contact[1]} | {contact[2]} | {contact[3]}", size=20),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color=ft.Colors.RED,
                            on_click=lambda e, id=contact[0]: delete_contact(id)
                        )
                    ]
                )
            )
        page.update()

    def add_contact(e):
        if сontact_input.value and number_input.value and additionally_input.value:
            db.add_contact(сontact_input.value, number_input.value, additionally_input.value)
            сontact_input.value = ""
            number_input.value = ""
            additionally_input.value = ""
            load_contacts()

    def delete_contact(contact_id):
        db.delete_contact(contact_id)
        load_contacts()

    def clear_all(e):
        db.clear_all()
        load_contacts()

    add_btn = ft.ElevatedButton("Добавить", on_click=add_contact)
    clear_btn = ft.ElevatedButton("Очистить всё", on_click=clear_all, bgcolor=ft.Colors.RED, color=ft.Colors.WHITE)

    page.add(
        ft.Text("Студенты IT Курса GEEK", size=32, weight="bold"),
        ft.Row([сontact_input, number_input, additionally_input, add_btn]),
        clear_btn,
        contacts_list
    )

    load_contacts()

ft.app(target=main)
