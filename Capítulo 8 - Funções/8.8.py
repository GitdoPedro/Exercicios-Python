def make_album(artista,titulo,faixas =''):
    album = {'artista': artista, 'titulo': titulo}
    if faixas:
        album['faixas'] = faixas
    return album


while True:
    print("\nNome da banda: ")

    banda = input()
    if banda == '':
        break
    titulo = input("nome do album: ")
    if titulo == '':
        break

    artista = make_album(banda,titulo)
    print(artista)
    
