pesquisa = {}


flag_pesquisa = True



while flag_pesquisa:
    nome = input("Nome: ")
    desejo  = input("Teu desejo pra 2021: ")

    pesquisa[nome] = desejo


    adiciona = input('adiciona? S/N ')
    if adiciona.upper() == 'N':
        flag_pesquisa = False





for nome, desejo in pesquisa.items():
    print(nome.title() + " gostaria de " + desejo)
    
