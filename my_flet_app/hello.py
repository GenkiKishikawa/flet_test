import flet

def main(page: flet.Page):
    page.add(flet.Text(value="Hello, world"))
    
flet.app(target=main)