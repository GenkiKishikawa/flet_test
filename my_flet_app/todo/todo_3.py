import flet as ft
from components.TodoApp import TodoApp

def main(page: ft.Page):
    app = TodoApp()

    page.add(app)

ft.app(target=main)