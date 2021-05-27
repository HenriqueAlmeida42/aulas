""""
como definir uma função:

def nome_da_função(parametro_da_função):
    bloco_da_função

OBS: 1: o nome da função deve estar semprem em minusculo e se for composto deve ser separado por underline(_);
2: uma função pode receber/ retornar dados;
3: uma função nao precisa de um dado de entrada mas SEMPRE deve conter os parenteses ();
4: a função pode ter mais de um dado de entrada, sendo necessario separar por virgula os dados.
------------------------------------------------------------------------------------------------

funções com retorno
basicamente vc usa a palavra return para retornar o valor desejado

ex de função comum com retorno:

def quadrado_d_7():
    return 7 * 7

print(quadrado_d_7())

OBS sobre a palavra return:
1- ela finaliza a função, ela sai da execução da função;
2- podemos ter, em uma função, diferentes returns;
3- podemos, em uma função, retornar multiplos valores e qualquer tipo de dado

#exemplo 1

def diz_oi():
    print('estou sendo executado antes do return...')
    return 'oi'
    print('estpu sendo executado depois do return...')

print(diz_oi())

#exemplo 2


def nova_funcao():
    valor = None
    if valor == True:
        return 5
    elif valor is None:
        return 4.2
    return 'b'


print(nova_funcao())

#exemplo 3


def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()

print(outra_funcao()) # ele gera uma tupla por causa das virgulas no return
print(num1, num2, num3, num4)
-------------------------------------------------------------------------------
#criar uma função para jogar moeda
from random import random


def joga_moeda():
    if random() > 0.5:
        return 'cara'
    return 'coroa'


print(joga_moeda())
---------------------------------------------------------------------
funções com parametros (entradas)

1- podem receber mais de um parametro e mais de um tipo de parametro, ultulizando (,) para separar os elementos;
2- parametros são os elementos colocados na definição da função, argumentos sao os valores colocados
para que se haja o processamento da função (entradas)
3- se informar o numero errado de parametros ou argumentos gera um TypeError
4- de nomes que façam sentido para a função e não somente A e B (genericos sem relação)
5- cuuidado com a ordem dos argumentos pois a função vai atuar em relaçao a ordem q recebe
e nao nessasariamente só pq eu utilizei o mesmo nome q no parametro
OBS: a exceção para a regra 5 é a utilização dos KeyWord Arguments (nome='argumento')
nesse caso como vc nomeia oq aquele parametro vai receber a ordem pode ser alterada

# exemplos função com parametros


def soma(a, b):
    return a + b


def outra (num1, b, msg):
    return (num1 + b) * msg


def nome_completo (nome, sobrenome):
    return f'o seu nome completo é {nome} {sobrenome}'


print(soma(4, 6))
print(outra(3, 2, 'batmam '))
print(nome_completo(sobrenome='jonson', nome='jj'))
-------------------------------------------------------------------------------------

Funções com parametro padrão ( Default Paramters)

- são funções em que se ultiliza um valor default para o parametro,
tornando assim a entranda de algum valor para esse paramtro opcional;
- o valor com Default deve SEMPRE vir no final dos parametros;
- podemos utilizar qualquer tipo de dado como Default;
- deve-se tomar cuidado com variaveis globais, para se usar uma dentro de uma função
é preciso 'a visar o codgo', chamando a variavel para dentro da função com 'globla 'variavel'';
- da para utilizar uma função como Default;
- podemos declarar funções dentro das funções, elas so seram validas para as funções;

# Por que utilizar funções com valor Default?

- nos permite ser mais flexiveis nas funções;
- evita erros com parametros incorretos;
- nos permite trabalhar com exemplos mais legiveis de codgo;

# exemplo


def mostra_informacao(nome='geek', instrutor=False):
    if nome == 'geek' and instrutor:
        return 'bem-vindo estrutor Geek!'
    elif nome == 'geek':
        return 'pensei que vc era o instrutor'
    return f'Ola {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True)) # os argumentos seguem em ordem
print(mostra_informacao('ozzy'))
print(mostra_informacao(nome='tadeu'))
-------------------------------------------------------------------
# exemplo de usar uma função como Default


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3)) # faz a soma ja que eu chamo a funçao soma
print(mat(4, 2, subtracao)) # faz a subtração pois eu chamo a função subtraçao
--------------------------------------------------------------------------------
# exemplo de usar a variavel global na função

total = 0


def incrementa():
    global total # to chamando a variavel global para dentro do codgo

    total = total + 1
    return total


print(incrementa())
print(incrementa())
-------------------------------------------------
# exemplo de usar uma função dentro da outra


def fora():
    contador = 0

    def dentro():
        nonlocal contador # chama a variavel local da função anterior
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora()) # por causa do contador receber 0 no inicio da função fora ele sempre vai ficar com 1

OBS nao posso fazer por exemplo " print(dentro())", pois dentro() só exite para a função fora()

"""
def mostra_informacao(nome='geek', instrutor=False):
    if nome == 'geek' and instrutor:
        return 'bem-vindo estrutor Geek!'
    elif nome == 'geek':
        return 'pensei que vc era o instrutor'
    return f'Ola {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True)) # os argumentos seguem em ordem
print(mostra_informacao('ozzy'))
print(mostra_informacao(nome='tadeu'))