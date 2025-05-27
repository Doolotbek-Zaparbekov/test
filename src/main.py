import flet as ft
from database import Database


def main(page: ft.Page):
    page.title = "Рейтинг кинг"
    title = ft.Text(value="Ваши книги", size=28)
    page.data = 0
    db = Database("book.sqlite3")
    db.create_tables()

    def add_book(e):
        books = f"Книга: {book.value}|Рейтинг: {rating.value}|Прочтено: {reading.value} раз."
        books_list_area.controls.append(ft.Text(value=books, size=18))
        db.add_book(book.value, rating.value, reading.value)
        page.data += 1
        book.value = ""
        rating.value = ""
        reading.value = ""
        consumption.value = f"Всего книг: {page.data}"
        page.update()

    consumption = ft.Text(value=f"Всего книг: {page.data}", size=25)
    page.update()
    book = ft.TextField(label="Название книги")
    rating = ft.TextField(label="Рейтинг книги")
    reading = ft.TextField(label="Сколько раз прочитано")
    add_button = ft.ElevatedButton("Добавить", on_click=add_book)
    form_area = ft.Row(controls=[book, rating, reading, add_button])
    books_list_area = ft.Column()
    page.add(title, form_area, consumption, books_list_area)


ft.app(main)
