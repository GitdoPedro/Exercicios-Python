citties = {
    'Rio de Janeiro' : {
                         'country'   : 'brasil',
                         'population': '6700000',
                         'fact'      : 'cidade maravilhosa'
                         },
    'São Paulo'      : {
                         'country'   : 'brasil',
                         'population': '100000',
                         'fact'      : 'alguma coisa acontece no meu coração'
                         },
    'Salvador' : {
                         'country'   : 'brasil',
                         'population': '3400000',
                         'fact'      : 'saudades'
                         }
    }



for city,data in citties.items():
    print("a cidade de " + city + " possui as seguintes informações: ")
    for dado,valor in data.items():
        print(dado + " : " + valor)
        
    
