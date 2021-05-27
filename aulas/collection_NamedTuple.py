""""
Modulo collections Named Tuple
https://docs.python.org/3/library/collections.html#collections.namedtuple

# Recapitulação de tupla
tupla = (1, 2, 3)

print(tupla[1])  # imprimindo o valor no indice 1

Named Tuple = são tuplas, diferenciadas, onde especificamos um nome para a mesma e tambem parametros

"""
# import
from collections import namedtuple

# precisamos definir nome e parametros, existe 3 formas

# Forma 1 - declaração NamedTuple

cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2 - declaração NamedTuple

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 1 - declaração NamedTuple

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# usando

jack = cachorro(idade=1, raça='rotwaller', nome='Jack')

print(jack)

# Acessando os dados

# Forma 1
print(jack[0]) # idade
print(jack[1]) # raça
print(jack[2]) # nome

# Forma 2

print(jack.idade) # idade
print(jack.raça) # raça
print(jack.nome) # nome

print(jack.index('rotwaller'))
print(jack.count('1'))