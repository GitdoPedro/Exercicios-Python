def make_car(fabricante,modelo,**outros):
    carro = {}
    carro['fabricante'] = fabricante
    carro['modelo']     = modelo
    for key,value in outros.items():
        carro[key] = value
    return carro



car = make_car('peugeut','bmw',ano = '2019',cor = 'preto')
print(car)
