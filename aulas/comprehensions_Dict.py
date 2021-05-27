""""
dicionary comprehensions

- Mesma coisa q list comprehensions só que para dicionarios

- Sintaxe:
{chave: valor for valor in interavel}

#exemplos

#1
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
# .items() transforma numeros em uma lista cheia de tuplas: ex: [('a', 1), ('b',2)]
print(quadrado)

#2
numeros = [1, 2, 3, 4, 5, 1, 2]

quadrado = {valor: valor ** 2 for valor in numeros}
print(quadrado)
# faz a chave recebe o mesmo valor de numeros e o valor receber ele ao quadrado
# ele nao imprime os ultimos 1 e 2 pois dicionario nao repete chave

#3

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
# nesse caso eu chamos as listas e informo q pocisão eu quero delas para formar um dicionario

-----------------------------------------------------------------------------------------------
# exemplos de loigica condicional ( da pra fazer mais q nem se faz com lista)

numeros = [1, 2, 3, 4, 5, 6]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)

"""
