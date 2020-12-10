famosos = ['albert eisten','maradona','buda']

for famoso in famosos:
    print("Seja bem vindo,", famoso.title())


famosos.insert(0,'jesus cristo')
famosos.insert(1,'michael jackson')
famosos.append('tony stark')

for famoso in famosos:
    print("O jantar será servido,",famoso.title())
