
flamengo = {
    'Diego Alves'     : [1,12],
    'Rafinha'         : [18,2],
    'Pablo Mari'      : [24,4],
    'Rodrico Caio'    : [3,15],
    'Filipe Luis'     : [21,6],
    'William Arão'    : [5,25],
    'Gérson'          : [15,8],
    'De Arrascaeta'   : [14,10],
    'Everton Ribeiro' : [7,10],
    'Bruno Henrique'  : [27,7],
    'Gabigol'         : [9,18]

}


for jogador,numeros in flamengo.items():
    print('os números favoritos do ' + jogador + ' são: ')
    for numero in numeros:
        print(numero)
