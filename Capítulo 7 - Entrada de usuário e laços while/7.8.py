sandwich_orders = ['cachorro-quente','misto-quente','bauru','narutal','hamburguer']
finished_sandwiches = []


while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(current_sandwich + " foi feito")
    finished_sandwiches.append(current_sandwich)


print("sanduíches prontos: ")

for sanduiche in finished_sandwiches:
    print(sanduiche.title())
