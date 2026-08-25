#função que define mensagem e dados email
def envia_email(mensagem):
    print("\n[EMAIL]")
    print(mensagem)

#função que define mensagem e dados whatsapp
def envia_zapp(mensagem):
    print("\n[WHATSAPP]")
    print(mensagem)

#função que envia mensagens
def notificando(mensagem):

    envia_email(mensagem)
    envia_zapp(mensagem)