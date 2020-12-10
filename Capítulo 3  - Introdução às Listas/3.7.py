famosos = ['albert eisten','maradona','buda']

for famoso in famosos:
    print("Seja bem vindo,", famoso.title())


famosos.insert(0,'jesus cristo')
famosos.insert(1,'michael jackson')
famosos.append('tony stark')

for famoso in famosos:
    print("O jantar será servido,",famoso.title())


print("infelizmente só 2 podem entrar")

mesa = len(famosos)-2

for i in range(mesa):
    print("Tchau,",famosos[-1])
    famosos.pop()


print(famosos[0]+" e "+famosos[1]+", vcs ainda estão no jantar, bom apetite!")
del famosos[1]
del famosos[0]

print("fim do jantar, "+ str(len(famosos)) + " pessoas à mesa")
