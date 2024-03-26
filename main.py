import flet as ft

def main(page: ft.Page): # this are called page or canvas
    
    def add_clicked(e):
        page.add(ft.Text('login'))


    page.vertical_alignment = ft.MainAxisAlignment.CENTER #They are a Function so they can be an attribute
    login = ft.Text(value= 'Login', color='black', size=30)
    email_field = ft.TextField(hint_text='Username or Email', width=300)
    pass_field = ft.TextField(hint_text='Password', width=300)
    submit_btn = ft.ElevatedButton(text= 'Submit', on_click= add_clicked)
    print(email_field.value) # Event : They are what the user is doing (ano ginawa)

    # page.add(email_field, pass_field) #append
        
    #page are append
    #controls are list
    page.add(ft.Row(controls=[login], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row(controls=[ft.Column(controls=[email_field, pass_field, submit_btn])], alignment=ft.MainAxisAlignment.CENTER)) #container (They have rows and columns)
    # page.add(ft.Row(controls=[ft.ElevatedButton('Submit', on_click=add_clicked)], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main)
