"""
4.1 –
Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os
nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada
pizza.
• Modifique seu laço for para mostrar uma frase usando o nome da pizza em vez
de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha na
saída contendo uma frase simples como Gosto de pizza de pepperoni.
• Acrescente uma linha no final de seu programa, fora do laço for, que informe
quanto você gosta de pizza. A saída deve ser constituída de três ou mais linhas
sobre os tipos de pizza que você gosta e de uma frase adicional, por exemplo,
Eu realmente adoro pizza!
"""


pizzas = ['calabresa', 'muçarella' , 'frango com catupiry', 'carne seca','4 queijos']
friend_pízzas = pizzas[:]

pizzas.append('portuguesa')
friend_pízzas.append('marguerita')


print("Minhas pizzas são:")
for pizza in pizzas:
    print(pizza)


print("As pizzas favoritas de meu amigo são:")
for pizza in friend_pízzas:
    print(pizza)
    
