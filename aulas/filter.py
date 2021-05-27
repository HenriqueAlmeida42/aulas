"""
FILTER - serve para filtrar dados de uma determinada coleção

OBS 1: Assim como no map() o filter() recebe 2 parametros, 1 função e 1 interavel;
OBS 2: Assim como no map() o dado é apagado da memoria apos a primeira utilização
OBS 3: Gera um filter object



# Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados usados para o exemplo
dados =[1.3, 2, 65, 42, -5, 3]

# Calculando a média utilizando a função mean() da biblioteca
media = statistics.mean(dados)

print(f'media: {media}')

res = filter(lambda valor: valor > media, dados)
print(list(res))

# Mostrando que limpa quando usado pela segunda vez
print(list(res))
----------------------------------------------------------------

# exemplo 2
paises = ['', 'Argentina', '', '', 'Brasil', 'Rusia', '', 'Japao', '', '', 'Nova Zelandia']

print(paises)

# res = filter(None, paises)
# res = filter(lambda pais: len(pais) > 0, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))
---------------------------------------------------------------------------------------

# exemplo mais complexo
usuarios = [
    {"username": "lucas", "tweets": ["zzz"]},
    {"username": "lu34", "tweets": []},
    {"username": "had", "tweets": ["fdp", "bolsolixo"]},
    {"username": "lo34", "tweets": []},
    {"username": "bob333", "tweets": []},
    {"username": "amanda", "tweets": ["buceta", "laranja"]},
]

print(usuarios)

# Filtrar usuarios que estao inativos no Tweets

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios ))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

----------------------------------------------------------------------------------------

# Combinar filter() com map()

nomes = ['Vanessa', 'Ana', 'Maria', 'le']

# devemos criar uma lista contendo 'sua instrutora é' + nome, desde q cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)

"""
# exemplo mais complexo
usuarios = [
    {"username": "lucas", "tweets": ["zzz"]},
    {"username": "lu34", "tweets": []},
    {"username": "had", "tweets": ["fdp", "bolsolixo"]},
    {"username": "lo34", "tweets": []},
    {"username": "bob333", "tweets": []},
    {"username": "amanda", "tweets": ["buceta", "laranja"]},
]

print(usuarios)

# Filtrar usuarios que estao inativos no Tweets

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios ))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

