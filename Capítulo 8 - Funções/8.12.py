def make_sandwich(*ingredients):
    print('Your sandwich has: ')
    for ingredient in ingredients:
        print('- ' + ingredient)



make_sandwich('pão','ovo')
make_sandwich('pão','carne','queijo')
make_sandwich('2 hambúrgueres', 'alface', 'queijo', 'molho especial', 'cebola' , 'picles','pão com gergelim')

