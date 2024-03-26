import flet as ft

# Capital letter are all classes

def main(page: ft.Page): #page is a canvas that you can put any controls (elements) ()
    page.title = "Flet counter example" 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100) # required parameters or arguments

    def minus_click(e): #the function in a class is 
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click), 
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)

ft.app(target=main, view=ft.AppView.WEB_BROWSER) # run code to be a website


#node are a canvas