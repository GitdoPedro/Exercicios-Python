def make_album(artista,titulo,faixas =''):
    album = {'artista': artista, 'titulo': titulo}
    if faixas:
        album['faixas'] = faixas
    return album


nirvana = make_album('nirvana','nevermind')
linkin_park = make_album('linkin park','meteora')
spc = make_album('só pra contrariar','ao vivo' , faixas = 27)


    
print(nirvana)
print(linkin_park)
print(spc)
