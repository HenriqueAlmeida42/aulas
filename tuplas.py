""""
                tuplas (tuple)
 sao iguais as listas com duas principais diferencas
 1- sao representads por (), mas nao precisao de () para serem criadas pois sao defenidas por ,

 2- tuplas sao imutaveis, ou seja, toda alteracao em uma tupla gera uma nova tupla

 DICA: usar tuplas SEMPRE que nao precisar modificar os dados contidos em uma colecao

 por que ultilizar tuplas???

 1- tuplas sao mais rapidas que listas
 2- por serem imutaveis acabam deixando o codgo mais seguro

 -----------------------------------------------------------------------------------------------
 # Podemos gerar uma tupla dinamicamente com o comando tuple e o range(inicio:fim:passo)

tupla = tuple(range(11))
print(tupla)
print(type(tupla))
-----------------------------------------------------------------------------
# Desempacotamento de tuplas

tupla1 = ('Perna Longa:', 'isso é tudo pessoal!')
personagem, fala = tupla1
print(personagem)
print(fala)

#OBS: gera erro se o numero de elementos for diferente pra desempacotar
---------------------------------------------------------------------------------
# soma*, maior valor*, menor valor* e tamanho (* só funciona se forem numeros inteioros ou reais)

tupla = (99, 5, 7, 112, 34, 87, 65, 12.34, 10)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
------------------------------------------------
# Concatenacão de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (99, 98, 97)
print(tupla2)

print(tupla1 + tupla2) # Concatenacao, as tuplas continuam inalteradas
print(tupla1)
print(tupla2)
---------------------------------------------------------------
# Verificar se um valor esta em uma tupla

tupla = (99, 5, 7, 112, 34, 87, 65, 12.34, 10)

print(12.34 in tupla) # retorna verdadeiro ou falso
----------------------------------------------------------------
# interando em tuplas com for

tupla = (99, 12, 56, 76)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
-------------------------------------------------
# interando com while
i = 0
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')

while i < len(meses):
    print(meses[i])
    i = i + 1
---------------------------------------------------------------------------
# Contando elementos em uma tupla usando .count

tupla = ('d', 'g', 'r', 't', 't')
print(tupla.count('t'))

vontade = tuple('lamber uma buceta')
print(vontade)
print(vontade.count('a'))
----------------------------------------------------------
# Acesso a um elemento em uma tupla

meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')
print(meses[5])
---------------------------------------------------------
# Slicing = tupla[incio:fim:passo]
meses = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez')

print(meses[2::3])

"""

tupla = 2, 'a', 43, 'f'
print(type(tupla))
print(tupla)