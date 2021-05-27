""""
Set comprehension
- mesma coisa que os outros só que com sets

- sinatxe:
{valor for valor in interavel}

-OBS: lembre-se que sets não tem valor repetido e nem seguem a ordenação

# Exemplo

# 1
numero = {num for num in range(1, 7)}
print(numero)

# 2
numeros = {x ** 2 for x in range(10)}
print(numeros)

# 3 - A mesma de cima transformada em dicionario para verificar as semelhanças

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# 4

letras = {letra for letra in 'Gardians of the galaxy'}
print(letras)

# 5
print({x for x in range(5)})

"""
