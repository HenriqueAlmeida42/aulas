"""
Sorted
- Serve para ordenar; gera uma lista com os elementos ordenados e mantem o interavel original

- OBS 1: Não confunda sorted com sort() de lista. O sort() só funciona em lista e o Sorted funciona com todo
interavel

- OBS 2: O sorted SEMPRE retorna uma lista com os elementos do interavel ordenados


# Exemplo

numeros = (1, 3, 99, 42, 3)
print(numeros)

print(sorted(numeros))
print(numeros)

numeros = [1, 3, 99, 42, 3]
print(numeros)
print(sorted(numeros))

# Adicionando parametros ao sorted

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor
--------------------------------------------------------------------------
# Podemos usar o sorted para coisa mais complexas

usuarios = [
    {"username": "lucas", "tweets": ["zzz"]},
    {"username": "lu34", "tweets": []},
    {"username": "had", "tweets": ["fdp", "bolsolixo"]},
    {"username": "lo34", "tweets": []},
    {"username": "bob333", "tweets": []},
    {"username": "amanda", "tweets": ["buceta", "laranja"]},
]

print(usuarios)

# Ordenar por username - Ordem alfabetica
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de Tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

"""
