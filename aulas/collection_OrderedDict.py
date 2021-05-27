""""
Collections - Ordered Dict


# Em um dicionario a ordem de incerção dos elemnetos não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave = {chave}, valor = {valor}')

# Ordered Dict = é um dicionario que nos garante a ordem de inserção dos elementos.

#fazendo o import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave = {chave}, valor = {valor}')

"""
# Entendendo a diferença entre Dict e Ordered Dict

#fazendo o import
from collections import OrderedDict

# Dicionarios Comuns
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 2, 'a': 1}

print(dic1 == dic2) # True ja que a ordem dos elementos não importa para o dicionario

# Ordered Dict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False ja que a ordem dos elementos importa para o OrderedDict