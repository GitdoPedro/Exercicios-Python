
ingrediente = input("Qual ingrediente? ")
ingrediente += "\n (Escreve 'quit' quando finalizar)"

while True:
    pizza = input(ingrediente)

    if pizza == 'quit':
        break;
    else:
        print(pizza.title()+ " adicionado!")
