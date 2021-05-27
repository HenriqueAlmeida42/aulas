""""
list comprehension

- Utilizando list comprehension nos podemos gerar novas listas com dados processados a partir
de outro interavel

-sintaxe:
[dado for dado in interavel]

# exemplos

#1

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

#2

nome = 'Gardians of the Galaxy'

print([letra.upper() for letra in nome])

#3


def maiscula(nome):
    nome = nome.replace(nome[0], nome[0].upper()) # .replace troca um elemento pelo outro, no caso a primeira letra
    return nome


amigos = ['todinho', 'joao', 'fernanda']

print([maiscula(amigo) for amigo in amigos])

#4

print([numero * 3 for numero in range(1, 10)])

#5

print([bool(valor) for valor in [0, [], '', True, 1, 3.12]])
# bool - tranforma o valor em bolleano(verdadeiro ou falso) 0, e lista e string vazias sao considerados falsos

#6

print([str(numero) for numero in [1, 2, 3, 4, 5]])
---------------------------------------------------------------
-Tambem é posivel colocar estruturas logicas em comprehensions

# exemplos

#1

numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# reformulando

# o % 2 para numeros pares é 0, logo seria False e nao adicionaria o numero, mas com o not nos invertemos
# e o que era False vira True e vice versa
pares = [numero for numero in numeros if not numero % 2]

# aqui so vai adicionar quando o numero for impar pois o %2 para um numero impar é maior que 0
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# exemplo 2

res = [numero * 2 if numero %2 == 0 else numero / 2 for numero in numeros]
print(res)
# ele começa em for numero in numeros e executa os IFs
------------------------------------------------------------
listas aninhadas (matrizes)

- da para fazer comprehensions com matrizes, eliminando a nessecidade
de usar mais de uma linha de codgo

# exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(valor) for valor in lista] for lista in listas]
# o utimo for sao as linhas e o primeiro sao as colunas, ele le do final e depois o começo
---------------------------------------------------------------------------------------------
# gerando um tabuleiro (matriz 3 x 3)

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
# para cada valor de 1 a 3 cria uma lista de 1 a 3, tudo isso dentro de uma lista, ou seja, cria uma matriz 3 x 3
--------------------------------------------------------------------------------------------------------------------
# gerando jogadas para um jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)
--------------------------------------------------------------------------------------------------
# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])

"""
