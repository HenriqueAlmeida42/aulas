""""
conjuntos (sets)

- conjuntos em qualquer linguagem de programação faz referencia a Teoria dos Conjuntos em Matematica

dito isso, na mesma forma como na matematica:

- Sets não possuem valores duplicados
- Sets não possuem valores ordenados
- Elementos não são acessados via indice, ou seja, conjuntos nao são indexados

Conjuntos (Sets) são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos nos preocupar
com chaves, valores e itens duplicados

os Sets são referenciados em python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionarios) em python:
    - Um Dicionario tem chave/valor
    - Um conjunto apenas valor
-------------------------------------------------------------------
# Definindo um Conjunto:

# Forma 1
dados = (2, 3, 4, 'f', 4, 99, 35, 'f')
s = set(dados)
print(s)
print(type(s))

#OBS: Ao criar um Set, caso seja adicionado um valor ja existente, o mesmo sera ignorado sem gerar erro

# Forma 2 (mais comum)

s = {1, 3, 4, 'd', 6, 4, 2}
print(s)

# Podemos ver se determidado elemento esta contido no conjunto

if 'd' in s:
    print('tem d')
else:
    print('não tem d')
--------------------------------------------------------------------------------------
# Importante lembrar que, alem de não termos valores repitidos, não temos ordem

#Listas aceitam valores duplicados, então temos 10 elementos
lista = [1, 42, 99, 5, 13, 1, 'f', 99, 73, 69]
print(f'lista = {lista} com {len(lista)} elementos')

#tuplas aceitam valores duplicados, então temos 10 elementos
tupla = 1, 42, 99, 5, 13, 1, 'f', 99, 73, 69
print(f'lista = {tupla} com {len(tupla)} elementos')

#dicionarios não aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys( [1, 42, 99, 5, 13, 1, 'f', 99, 73, 69], 'f')
print(f'lista = {dicionario} com {len(dicionario)} elementos')

#conjuntos aceitam valores duplicados, então temos 8 elementos
conjunto = {1, 42, 99, 5, 13, 1, 'f', 99, 73, 69}
print(f'lista = {conjunto} com {len(conjunto)} elementos')
# repare q a ordem impressa difere da ondem digitada
---------------------------------------------------------------------------------------
# interando com sets
s = {'t', 0, 'm', 4, 'n', 'o', 'c', 6}
for valor in s:
    print(valor)
-------------------------------------------
# Adicionar elementos a um conjunto
s = {666, 69, 42}
print(s)

s.add(73)
s.add(73)
print(s)
#OBS: não gera erro ao tentar adicionar um elemento que ja exite no conjunto
----------------------------------------------------------------------------------
# Removendo elementos de um conjunto
s = {666, 69, 42}
print(s)

#forma 1 .remove

s.remove(666)
print(s)
#OBS: caso o valor nao seja encontrado gera erro

#forma 2 .discard

s.discard(42)
print(s)
#OBS: se o valor nao for encontrado nao gera erro
-------------------------------------------------------------
# copiando comjuntos
s = {666, 69, 42}

#forma 1 deep copy

novo = s.copy()

novo.add(12)
print(novo)
print(s)

# Forma 2 shallow copy

novo = s

novo.add(12)
print(novo)
print(s)
-----------------------------------------------------
# Metodos matematicos de conjuntos

# Imagine que temos dois conjuntos: gosta de whisky e gosta de cerveja

gosta_whisky = {'fernanda', 'jhen', 'lucas', 'pedrinho', 'tua mãe', 'jony'}
gosta_cerveja ={'zeca', 'paty', 'fernanda', 'pedrinho'}

#veja que algumas pessoas q gostam de whisky tambem gostam de cerveja

#1- Precisamos gerar um conjunto com nomes unicos independente do gosto

# Forma 1 - ultilizando union

unicos1 = gosta_cerveja.union(gosta_whisky)
print(unicos1)

# Forma 2 - ultilizando o caracter pipe |

unicos2 = gosta_whisky | gosta_cerveja
print(unicos2)

#2- Gerar um conjunto de bebados que estao em ambos os conjuntos

#Forma 1- ultilizando intersection

ambos1 = gosta_cerveja.intersection(gosta_whisky)
print(ambos1)

#Forma 2 - usando o &

ambos2 = gosta_whisky & gosta_cerveja
print(ambos2)

#3- Gerar um conjuto de bebados que não estão no outro grupo

#ultiliza o .difference

cerveja = gosta_cerveja.difference(gosta_whisky)
print(cerveja)

whisky = gosta_whisky.difference(gosta_cerveja)
print(whisky)
---------------------------------------------------------------------
# soma, maior valor, menor valor e total de elemnetos
s = {1, 34, 45, 93, 99, 335}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

"""
