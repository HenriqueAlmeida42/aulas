"""" exemplo do que se pode fazer com listas

lista1 = [1, 99, 27, 22, 43, 52, 3, 12,99]
lista2 = ['Geektou', 'tnt'] # pode ser caracteris separados
lista3 = []
lista4 = list(range(11)) # cria uma lista q vai do 0 a 10
lista5 = list('toma no cu') # vai criar uma lista com a frase
------------------------------------------------------------------------------------------------------------
# podemos verificar se n elemento esta dentro de uma lista ( n pode ser tanto um numero quanto uma string)
num = 45
if num in lista4:
    print(f'encontrei o num {num}')
else:
    print(f'nao encontre o num {num}')
---------------------------------------------------------------------------------------------------
# podemos ordenar uma lista usando o comando .sort(), podemos ordenar uma lista de string tambem
print(lista1)
lista1.sort()
print(lista1)
lista5.sort()
print(lista5)
------------------------------------------------------------------------------------------------------------
# podemos contar o numero de ocorrencias em uma lista usando .count(n), sendo n o elemento que vc quer conta
print(lista1.count(99))
print(lista5.count('o'))
--------------------------------------------------------------------------------------------------------------------------
# adicionar elementos em listas
 ""para adicionar elementos em lista usamos a funcao .append, a funcao .append so adiciona 1 elemento de cada vez;
usamos a funcao .extend([n, n1, n...]) para adicionar mais de um elemento a uma lista, diferente do .append
 cada elemento da lista é unico elemento ao inves de participar de um conjunto que nem no exemplo""

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([3, 5, 77])
print(lista1)

if [3, 5, 77] in lista1:
    print('encontrei a lista')
else:
    print('nao encontrei a lista')
lista1.extend(['Geek'])
print(lista1)
----------------------------------------------------------------------------------------------------------------------
# podemos adicionar um valor em uma posicao especifica de uma lista com a fucao .insert(p, n) (p = pocisao, n = valor)
lista1.insert(3, 'nono valor')
print(lista1)
-------------------------------------------------------------------------
# podemos adicionar uma lista a outra usando + ou .extend()
lista6 = lista1 + lista2
print(lista6)
lista1.extend(lista5)
print(lista1)
------------------------------------------------------------------------------------------------------------
# podemos inverter uma lista usando a funcao .reverse() ou (lista[::-1]) [::-1] = slice, comeca na posicao zero vai ate o final e inverte
print(lista2[::-1])
lista2.reverse()
print(lista2)
--------------------------------------------------
# podemos copiar uma lista com .copy # para outra forma de copia verificar o final dessa aula
lista3 = lista1.copy()
print(lista3)
------------------------------------------------------------------------------
# podmeos saber quantos elementos uma lista tem usando len
print(len(lista1))
-------------------------------------------------------------------------
# podemos retirar o ultimo elemento de uma lista usando .pop()
# OBS o .pop() nao somente remove o elemento mas tambem o retorna
# OBS2 ele pode retirar um elemento de uma posicao especifica, fazendo todos os elementos a direita desse elemento
 irem para esquerda
print(lista2)
lista2.pop(0)
print(lista2)
-----------------------------------------------------
# .clear limpa uma lista
lista3.clear()
print(lista3)
--------------------------------------------------------------------------------------
# podemos multiplicar os elementos de uma lista usando uma multiplicao normal (*)
lista5 = lista5 * 3
print(lista5)
------------------------------------------------------------------------
# da para converte uma string em uma lista usando .split()
# OBS o .split() usa o espaco como padrao para separar os elemntos mas isso pode ser alterado
ex = 'da,pra,andar?'
ex = ex.split(',')
print(ex)
------------------------------------------------------------
# da para converter uma lista em string usando .join()
# é preciso identificar um separador entre os elementos
lista6 = ['putaria','sacanagem','sexo anal']
print(lista6)
curso = ' '.join(lista6)
print(curso)
curso = 'p '.join(lista6)
print(curso)
--------------------------------------------------------------
# encontrar o indice de um elemento em uma lista
numeros = [2, 5, 6, 7, 12, 6]
# em qual indice da lista esta o valor 6?
print(numeros.index(6))

# OBS: caso nao tenha o valor na lista gera erro; retorna somente indice do priemiro valor encontrado

# podemos fazer a busca dentro de um range, ou seja, qual indice comeca a busca
print(numeros.index(6, 3))

# pode ser feito com range de inicio e de fim
print(numeros.index(12, 2, 5))
--------------------------------------------------------
# soma; valor maximo; valor minimo; tamanho
# OBS: se os valores forem inteiros ou reais

print(sum(lista1))  #soma de todos os valores da lista
print(max(lista1))  #retorna o maior valor encontrado na lista
print(min(lista1))  #retorna o menor valor da lista
print(len(lista1))  #retorna a quantidade de elementos em uma lista
------------------------------------------------------------------------------
# tranformar uma lista em tupla
tupla = tuple(lista1)
print(tupla)
---------------------------------------------------------------
# desempacotamento de listas
numeros = [1, 2, 3]

num1, num2, num3 = numeros
print(num1)
print(num2)
print(num3)
#OBS: se tiver uma quantidade de valores diferentes que variaveis  vai da merda
---------------------------------------------------------------------------
# copiando uma lista para outra (deep copy e shallow copy)

# 1- deep copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)

# a copia e a lista original sao independentes

# 2- swallow copy
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)

# a copia e a original sao ligadas e recebem a mesma modificacao
"""
