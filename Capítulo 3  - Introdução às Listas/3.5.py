famosos = ['albert eisten','maradona','buda']

for famoso in famosos:
    print("Seja bem vindo,", famoso.title())


print("Infelizmente o " + famosos[0].title()+ " não poderá comparecer")

del famosos[0]
famosos.insert(0,"jesus Cristo")

for famoso in famosos:
    print("Seja bem vindo,", famoso.title())
