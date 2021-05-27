""""
Collections - Default Dict

# Recapitulando dicionarios
dicionario = {'chave': 'valor'}
print(dicionario)

print(dicionario['chave'])

print(dicionario['teste']) # gera keyerror

Default Dict = ao criar um dicionario usando o Default Dict, nós informamos um valor default,
podendo utilizar uma lambda para isso. Esse valor será utilizado  sempre que não houver um valor definido.
Caso tentarmos acessar essa chave que não exite, essa chave será criada e o valor default será atribuido.

#OBS:
1- lambdas são funções sem nome que podem ou não receber parametros de entrada e retorna valores;
2- necessario importa a biblioteca
3- podemos ultilizar todas as funções de um dicionario comum
4- podemos acessar  a docmentação do python para mais informações:
https://docs.python.org/3/library/collections.html#collections.defaultdict

"""
# fazemdo o import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['vagina'] = 'lambida bem gostosa'
print(dicionario)

print(dicionario['no cuzinho']) # por estar usando o defaultdict não gera erro

print(dicionario)
