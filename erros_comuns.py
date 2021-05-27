"""
ERROS MAIS COMUNS

ATENÇÃO: é mais importante prestar atenção e aprender a ler as saidas de erros geradas pela execução
dos codigos.

1 - SintaxError = ocorre quando o python encontra um erro de sintaxe. Ou seja, vc escreveu algo que
o python nao reconhece como parte da lingua

Exemplo de SintaxError

a)
def funcao:
    print("buceta")

b)
def = 1

-------------------------------

2 - NameError = Ocorre quando uma variavel ou função não foi definida

Exemplo de NameError

a)
print(geek)

b)
buceta()

-------------------------------

3 - TypeError = Ocorre quando uma função/ação/operação é aplicada a um tipo errado

Exemplo TypeError

a)
print(len(5))

b)
print('buceta' + [])
----------------------------------------

4 - IndexError = Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
utilizando um indice invalido

Exemplo IndexError

a)
lista = ['buceta']
print(lista[2])

b)
lista = ['buceta']
print(lista[0][10])

c)
tupla = ('buceta')
print(tupla[0][10])
--------------------------------------

5 - ValueError = Ocorre quando uma função/operação built-in (integrada) recebe um argumento com o tipo correto
mas valor inapropriado

Exemplo ValueError

a)
print(int('buceta')) # o erro vem pq o int esta esperando uma string, mas ele espera um numero e nao somente letras
--------------------------------------------------------------------------------------------------------------------

6 - KeyError = Ocorre quando tentamos acessar um dicionario com uma chave que nao existe

Exemplo KeyError

a)
dic = {'python':'buceta'}
print(dic['sexo'])
--------------------------------

7 - AttributeError = Ocorre quando uma variavel não tem um atributo/função.

Exemplo AttributeError

a)
tupla = (2, 42, 69)
print(tupla.sort())
------------------------------

8 - IdentationError = Ocorre quando não é respeitado a indentação do python (4 espaços)

Exemplo IndentationError

a)
def nova():
print('buceta')

b)
for i in range(10):
i + 1

OBS: Exceptions e Erros são sinonimos na programação
"""
