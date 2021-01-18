usuarios = ['pedro','plinio','lucas','veronica','admin']


for usuario in usuarios:
    if usuario != 'admin':
        print ("Ola "+ usuario+ ",obrigado por fazer login novamente")
    else:
        print("Olá admin, gostaria de ver um relatório de status")
