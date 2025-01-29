import flet as ft

def main(website):
    title = ft.Text("Web Chat")


    def send_message_tunel(message):
        text = ft.Text(message)
        chat.controls.append(text)
        website.update()

    website.pubsub.subscribe(send_message_tunel)

    def send_message(event):
        name_user = field_popup.value
        text_user = field_message.value
        text = f"{name_user}: {text_user}"
        website.pubsub.send_all(text)
        field_message.value = ""
        website.update()
    
    field_message = ft.TextField(label="Digite sua mensagem", on_submit=send_message)
    button_send = ft.ElevatedButton("Enviar", on_click=send_message)
    row_send = ft.Row([field_message, button_send])
    chat = ft.Column()

    def open_chat(event):
        if field_popup != "":
            popup.open = False
            website.remove(title)
            website.remove(button)
            website.add(chat)
            website.add(row_send)
            name_user = field_popup.value 
            text = f"{name_user} entrou no chat"
            website.pubsub.send_all(text)
            
            website.update()


    title_popup = ft.Text("Bem vindo ao Web chat")
    field_popup = ft.TextField(label="Insira seu nome")
    button_popup = ft.ElevatedButton("Entrar no chat", on_click=open_chat)

    popup = ft.AlertDialog(title=title_popup, content=field_popup, actions=[button_popup])

    def open_popup(event):
        website.dialog = popup
        popup.open = True
        website.update()

    button = ft.ElevatedButton("iniciar chat", on_click=open_popup)
    
    website.add(title)
    website.add(button)
    


ft.app(main, view=ft.WEB_BROWSER)
