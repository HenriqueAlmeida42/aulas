""""
lista de exercicios funções

# exercicio 1


def dobro(numero):
    return numero * 2


numero = float(input('informe o valor que deseja dobrar: '))
print(dobro(numero))
--------------------------------------------------------------------
# exercicio 2


def data(dia, mes, ano):

    def mez(mes):
        meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
                 'outubro', 'novembro', 'dezembro')
        return meses[(mes - 1)]

    print(f'{dia} de {mez(mes)} de {ano}.')


dia = int(input('informe o dia: '))
mes = int(input('informe o mes: '))
ano = int(input('informe o ano: '))

data(dia, mes, ano)
---------------------------------------------------------------
# exercicio 3


def verificacao(numero):
    if numero > 1:
        return 1
    elif numero == 0:
        return 0
    return -1


numero = float(input('informe o numero: '))
print(verificacao(numero))
----------------------------------------------------
# exercicio 5


def volume(raio):
    v = (4/3) * 3.14 * (raio**3)
    return v


raio = float(input('informe o raio da esfera em metros: '))
print(f'o volume será de {volume(raio):.2f} metros cubicos')
--------------------------------------------------------------------
# exercicio 6


def convercao(hora, minuto, segundo):
    hora = hora * 3600
    minuto = minuto * 60
    return hora + minuto + segundo


hora = int(input('informe a hora: '))
minuto = int(input('informe os minutos: '))
segundo = int(input('informe os segundos: '))
print(f'esse horario em segundos é {convercao(hora, minuto, segundo)}s')
-------------------------------------------------------------------------------
# exercicio 4


def quadrado(valor):
    raizq = int(valor ** (1/2))
    if (raizq ** 2) == valor:
        return f'o numero {valor} é um quadrado perfeito'
    return f'o numero {valor} não é um quadrado perfeito'


valor = int(input('informe o valor para saber se é um quadrado perfeito: '))
print(quadrado(valor))
-------------------------------------------------------------------------------
# exercicio 7


def farenait(celcios):
    f = celcios * (9.0 / 5.0) + 32
    return f


celcios = float(input('informe a temperatura em celcios: '))
print(f'a temperatura em fahrenheit é {farenait(celcios)}F')
-----------------------------------------------------------------------------------
# exercico 8


def hipotenusa(a, b):
    h = ((a ** 2) + (b ** 2)) ** (1/2)
    return h


catetoA = int(input('informe o primeiro cateto: '))
catetoB = int(input('informe o segundo cateto: '))
print(f'a hipotenusa é = {hipotenusa(catetoA, catetoB):.2f}')
----------------------------------------------------------------------
# exercico 9


def volume(r, h):
    v = 3.141592 * (r ** 2) * h
    return v


print('insira o raio e a altura para descobrir o volume do cilindro')

raio = float(input('informe o valor do raio em metros: '))
altura = float(input('informe o valor da altura em metros: '))

print(f'o vlume do cilindro é de {volume(raio, altura):.2f} metros cubicos')
--------------------------------------------------------------------------------
# exercico 10


def maior(a, b):
    if a > b:
        return a
    return b


valor1 = float(input('informe o primeiro valor: '))
valor2 = float(input('informe o segundo valor: '))

print(f'o maior valor é {maior(valor1, valor2)}')
-------------------------------------------------------------
# exercico 11


def media(n1, n2, n3, letra):
    if letra == 'a':
        v = (n1 + n2 + n3) / 3
        return v
    elif letra == 'p':
        v = (n1 * 5 + n2 * 3 + n3 * 2) / 10
        return v


print('informe as notas do aluno')

nota1 = float(input('informe a primeira nota: '))
nota2 = float(input('informe a segunda nota: '))
nota3 = float(input('informe a terceira nota: '))

print('digite "a" se deseja saber a media aritimetica ou digite "p" se deseja saber a media ponderada')
letra = input('informe a letra: ')

print(f'a media é {media(nota1, nota2, nota3, letra):.2f}')
-------------------------------------------------------------------------------
# exercico 12


def soma(valor):
    soma = 0
    i = 0
    while i == 0:
        soma = soma + (valor % 10)
        valor = int(valor / 10)
        if valor == 0:
            i = 1
    return soma


valor = int(input('informe um valor: '))
print(f'a soma dos algarismos é = {soma(valor)}')
----------------------------------------------------------
# exercico 13


def operacao(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2


n1 = float(input('informe o primeiro valor: '))
n2 = float(input('informe o segundo valor: '))

print("informe a operção desejada:"
      "\ndigite '+' para somar os valores"
      "\ndigite '-' para subtrair os valores"
      "\ndigite '*' para multiplicar os valores"
      "\ndigite '/' para dividir os valores")

op = input('digite a operação desejada: ')

print(f'o resultado da operação é de {operacao(n1, n2, op):.2f}')
---------------------------------------------------------------------
# exercico 14


def eficiencia(km, l):
    valor = km / l
    if valor < 8:
        return 'Venda o carro!'
    elif valor < 12:
        return 'Economico!'
    return 'Super economico!'


km = float(input('informe os quilometros rodados: '))
litros = float(input('informe a quantida de litros de gasolina comsumida: '))
print(eficiencia(km, litros))
---------------------------------------------------------------------------------
# exercico 15


def triangulo(n1, n2, n3):
    i = 0
    if n1 < (n2 + n3):
        i += 1
    if n2 < (n1 + n3):
        i += 1
    if n3 < (n1 + n2):
        i += 1
    return i


def tipo(n1, n2, n3):
    if n1 == n2 and n1 == n3:
        return 'Triangulo Equilatero'
    elif n1 == n2 and n1 != n3:
        return 'Triangulo Isósceles'
    elif n1 != n2 and n1 == n3:
        return 'Triangulo Isósceles'
    elif n2 == n3 and n2 != n1:
        return 'Triangulo Isósceles'
    return 'Triangulo Escaleno'


n1 = int(input('informe um dos lados do triangulo: '))
n2 = int(input('informe um dos lados do triangulo: '))
n3 = int(input('informe um dos lados do triangulo: '))

if triangulo(n1, n2, n3) == 3:
    print(f'esse é um {tipo(n1, n2, n3)}')
else:
    print('esses valores não formam um triangulo')
-------------------------------------------------------------
# exercico 16


def desenha_linha(quantidade):
    print('=' * quantidade)


linha = int(input('informe o tamanho da linha que deseja: '))
desenha_linha(linha)
---------------------------------------------------------------
# exercico 17


def soma(n1, n2):
    i = n1
    soma = 0
    while i != (n2 - 1):
        i += 1
        soma += i
    return soma


n1 = int(input('informe um numero: '))
n2 = int(input('informe um numero: '))
print(f'a soma dos valores entre {n1} e {n2} é = {soma(n1, n2)}')
--------------------------------------------------------------------------
# exercico 22


def interrogacao(n1):
    for n in range(n1 + 1):
        print('!' * n)


n1 = int(input('informe um numero: '))
interrogacao(n1)
--------------------------------------------
# exercico 23


def asterisco(n1):
    for n in range((2*n1)):
        if n <= n1:
            print('*' * n)
        if n > n1:
            v = (n1 * 2) - n
            print('*' * v)


n1 = int(input('informe um numero: '))
asterisco(n1)
------------------------------------------
# exercico 24


def asterisco(n1):
    v = 1
    for n in range(n1):
        print(' '* n1, '*' * v)
        v += 2
        n1 = n1 - 1


n1 = int(input('informe um numero: '))
asterisco(n1)
-------------------------------------------------
# exercico 25


def serie(n1):
    i = 1
    valor = 0
    while i != (n1 + 1):
        valor += (i ** 2 + 1) / (i + 3)
        i += 1
    return valor


n1 = int(input('informe um numero: '))
print(f'o valor da serie é = {serie(n1)}')
---------------------------------------------------
# exercico 26


def somatorio(n1):
    valor = 0
    i = 1
    while i != (n1 + 1):
        valor += i
        i += 1
    return valor


n1 = int(input('insira um valor: '))
print(f'o somatorio dos numero ate o valor {n1} é = {somatorio(n1)}')
------------------------------------------------------------------------------
# exercico 32


def simplifica(n1, n2):
    mmc = []
    n = 2
    v1 = n1
    v2 = n2
    while n != 100:
        va1 = int(n1 / n)
        va2 = int(n2 / n)
        if (va1 * n) == n1 and (va2 * n) == n2:
            n1 = va1
            n2 = va2
            mmc.append(n)
            #print(mmc)
        else:
            n = n + 1
    variavel = 1
    for g in range(len(mmc)):
        valor = mmc[g]
        variavel = variavel * valor
    return f'o valor simplificado é = {(v1 / variavel)} / {(v2 / variavel)}'


n1 = int(input('inforne o numerador: '))
n2 = int(input('inforne o denominador: '))

print(simplifica(n1, n2))
------------------------------------------------------------------------------
# exercico 33


def fatorial(n1):
    valor = 1
    n = 1
    lista = []
    while n != (n1 + 1): # aqui é feita a fatoração
        valor = valor * n
        n += 1
        #print(valor)
    while valor != 0: # aqui se adiciona os valores de forma individual na lista
        a = valor % 10
        lista.append(a)
        valor = int(valor / 10)
        #print(valor)
    return print(f'a soma dos algarismos fatorados é:{sum(lista)}!')


n1 = int(input('inforne o numerador: '))
fatorial(n1)
----------------------------------------------------------------------
# exercico 34


def fatorial_impar(n1):
    lista = []
    valor = 1
    if (n1 % 2) == 0:
        return 'esse não é um valor impar!'
    for n in range(1, (n1 +1)):
        if (n % 2) != 0:
            lista.append(n)
    for g in range(len(lista)):
        valor = valor * lista[g]
    return valor


n1 = int(input('inforne um numero impar: '))
print(f'o fatorial duplo de {n1} é: {fatorial_impar(n1)}')
--------------------------------------------------------------
# exercico 39


def troca(a, b):
    v = a
    a = b
    b = v
    print('os valores foram trocados com sucesso!')
    print(f'o valor de A agora é: {a} e o valor de B é: {b}')


a = int(input('informe o valor de A: '))
b = int(input('informe o valor de B: '))
troca(a, b)
------------------------------------------------------------------
# exercico 40


def pares(*args):
    par = []
    for n in range(len(args)):
        if (args[n] % 2) == 0:
           par.append(args[n])
    return len(par)


vetor = []


def entrada():
    print('digite 0 para adicionar um numero ao vetor\n'
          'digite 1 para saber quantos numeros pares tem o vetor')
    op = int(input('digite a opção desejada: '))
    if op == 0:
        numero = int(input('informe qual numero deseja adicionar ao vetor: '))
        vetor.append(numero)
        entrada()
    elif op == 1:
        print(f'a quantidade de numeros pares no vetor é: {pares(*vetor)}')


entrada()
-----------------------------------------------------------------------------------
# exercico 41
vetor = []


def entrada():
    print('digite 0 para adicionar um numero ao vetor\n'
          'digite 1 para saber qual o numero de maior valor do vetor')
    op = int(input('digite a opção desejada: '))
    if op == 0:
        numero = int(input('informe qual numero deseja adicionar ao vetor: '))
        vetor.append(numero)
        entrada()
    elif op == 1:
        print(f'o maior valor dentro do vetor é: {max(vetor)}')


entrada()
-------------------------------------------------------------------------------
# exercico 44


def funcao(*args):
    a = []
    b = []
    for n in range(len(args)):
        if (args[n] % 2) == 0:
            a.append(args[n])
        else:
            b.append(args[n])
    print(f'os valores pares do vetor são: {a}\n'
          f'os valores impares do vetor são: {b}')


x = []
while (len(x)) != 30:
    numero = int(input('informe um numero para o vetor: '))
    x.append(numero)
    print(len(x))
funcao(*x)

----------------------------------------------------------------

"""
# exercico 52


def entrada():
    matriz = []
    int(input())