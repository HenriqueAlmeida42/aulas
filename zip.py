"""
ZIP()

zip() - cria um interavel (zip object) que agrega elemento de cada um dos interaveis passado como entrada
basicamenete ele pega o elemento na mesma posição de cada um dos interaveis e forma tupla com eles.

OBS 1: o zip() utiliza o tamanho do menor interavel para parar, ou seja, se vc passar uma lista com 3 valores, e outra
com 5 elementos ele vai usar somente os 3 primeiros valores.

OBS 2: o zip() tambem apaga seus dados após a primeira utilização

OBS 3: pode ser usado diferentes tipos de intevaris no zip() ao mesmo tempo


# Exemplo

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

zipl = zip(lista1, lista2, 'abcde')

print(zipl)
print(type(zipl))

# Gerando lista, tupla, set, dict

print(list(zipl))

zipl = zip(lista1, lista2, 'abcde')
print(tuple(zipl))

zipl = zip(lista1, lista2, 'abcde')
print(set(zipl))

zipl = zip(lista1, lista2)  # dicionario precisa de chave/valor se passar as letras ele buga pq tem 3 coisas
print(dict(zipl))

# diferente tamanhos de interaveis
lista3 = [42, 69, 21]

zipl = zip(lista3, lista1, lista2)
print(list(zipl))


# Diferentes tipos de interaveis

tupla = 2, 3, 4
lista = [1, 5, 7]
dicionario = {'a': 8, 'b': 6, 'c': 9}

zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Usando o * para desempacotar uma lista de tuplas e zipar

dados = [(1, 2), (3, 4), (5, 6), (7, 9)]
print(list(zip(*dados)))  # ele desempacotou como sendo duas tuplas e depois zipou


"""
# Exemplo mais complexo

prova1 = [89, 77, 69]
prova2 = [72, 99, 95]
alunos = ['maria', 'pedro', 'juliet']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
# ele zipa as listas criando uma variavel dado e como esse é um dicionary comprehension ele gera um dicionario
# com os valores das pocições especificadas

print(final)

# Fazendo o mesmo com map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
# ele primerio zipa as notas, depois usa o map para criar uma lista com as maiores notas e por fim zipa os alunos
# com as notas mais altas

print(dict(final))
