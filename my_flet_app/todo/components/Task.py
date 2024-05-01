import flet as ft


class Task(ft.Column):
    def __init__(self, task_name):
        super().__init__()
        self.task_name = task_name
        
    def build(self):
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=1)
        
        self.display_view = ft.Row(
			alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
			vertical_alignment=ft.CrossAxisAlignment.CENTER,
			controls=[
				self.display_task,
				ft.Row(
					spacing=0,
					controls=[
						ft.IconButton(
							icon=ft.icon.CREATE_OUTLINE,
							tooltip="Edit To-Do",
							on_click=self.edit_clicked,
						),
						ft.IconButton(
							ft.icons.DELETE_OUTLINE,
							tooltip="Delete To-Do",
							on_click=self.delete_clicked,
						),
					],
				),
			],
		)
        
        self.edit_view = ft.Row(
			visible=False,
			alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
			vertical_alignment=ft.CrossAxisAlignment.CENTER,
			
		)