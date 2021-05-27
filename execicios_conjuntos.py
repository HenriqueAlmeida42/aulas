""""
lista de exercicios de coleções

# exercicio 1
# letra a
lista = []
lista.extend([1, 0, 5, -2, -5, 7])
#letra b
soma = lista[0] + lista[1] + lista[5]
print(f'a soma dos elementos é {soma}')
#letra c
lista.insert(4, 100)
lista.pop(5)
#letra d
for n in lista:
    print(n)
-----------------------------------------------
# exercicio 2
e = 0
lista = []
while e < 6:
    valor = int(input('qual o valor a ser adicionado?  '))
    lista.append(valor)
    e = e + 1
print(lista)
----------------------------------------------------------
# exercicio 3
e = 0
lista = []
quadrado = []

while e < 10:
    valor = float(input('qual o valor a ser adicionado?  '))
    lista.append(valor)
    valor = valor * valor
    quadrado.append(valor)
    e = e + 1
print(lista)
print(quadrado)
-------------------------------------------------------------
# exercicio 4
lista = [99, 34, 56, 78, 2, 13, 32, 42]
x = int(input('insira uma posição para x de 0 á 7: '))
y = int(input('insira uma posição para y de 0 á 7: '))

soma = lista[x] + lista[y]
print(soma)
--------------------------------------------------------
# exercicio 5
lista = [99, 34, 56, 78, 2, 13, 32, 42, 76, 44]
pares = 0
for valor in lista:
    if valor % 2 == 0:
        pares = pares + 1

print(f'essa lista tem {pares} pares')
--------------------------------------------------
# exercicio 7
lista = []
x = 0
while x < 10:
    valor = int(input('insira um valor: '))
    lista.append(valor)
    x = x + 1
print(lista)
print(f'o maior elemento é:{max(lista)}')
print(f'o maior elemento esta em: {lista.index(max(lista))}')
--------------------------------------------------------------
# exercicio 8

lista = []
x = 0
while x < 6:
    valor = int(input('insira um valor: '))
    lista.append(valor)
    x = x + 1
lista.reverse()
print(lista)
------------------------------------------------------
# exercicio 10
media = []
alunos = int(input('quantos alunos fizeram a prova?: '))
x = 0

while x < alunos:
    nota = int(input('insira a nota do aluno: '))
    media.append(nota)
    x = x + 1

resutado = sum(media) / len(media)
print(f'a media da sala foi: {resutado}')
--------------------------------------------------
# exercicio 11
lista = []
x = 0
soma = 0
negativos = 0

while x < 10:
    valor = float(input('insira um valor: '))
    lista.append(valor)
    x = x + 1
    if valor > 0:
        soma = soma + valor
    else:
        negativos = negativos + 1


print(f'a soma dos elementos positivos é: {soma}')
print(f'a quantidade de elementos negativos é: {negativos}')
---------------------------------------------------------------
# exercicio 12 e 13 juntos
lista = []
x = 0

while x < 5:
    valor = float(input('insira um valor: '))
    lista.append(valor)
    x = x + 1

print(lista)
print(f'o maior valor da lista é: {max(lista)}')
print(f'a posição do maior valor é: {lista.index(max(lista))}')
print(f'o menor valor da lista é: {min(lista)}')
print(f'a posição do menor valor é: {lista.index(min(lista))}')
--------------------------------------------------------------------
# exercicio 14

vetor = [11, 11, 34, 23, 56, 99, 99, 132, 87, 11]
num = []
for n in vetor:
    #print(vetor.count(n))
    if vetor.count(n) >= 2:
        if not n in num:
            num.append(n)

print(num)
---------------------------------------------
# exercicio 15

vetor = [11, 11, 34, 23, 56, 99, 99, 132, 87, 12, 12, 13, 34, 23, 57, 79, 95, 135, 87, 16]
singulares = []
for n in vetor:
    if vetor.count(n) < 2:
        singulares.append(n)

print(singulares)
-------------------------------------------------------------------
# exercicio 16

#vetor = [11, 13, 24, 12, 56]
operaçao = 3
while operaçao != 0 :
    vetor = [11, 13, 24, 12, 56]
    print("escolha uma operação: "
      "0 - finaliza o programa  "
      "1 - mostrar o vetor em ordem direta  "
      "2 - mostrar o vetor em ordem inversa")
    operaçao = int(input('informe a opção: '))
    if operaçao == 1:
        print(vetor)
    elif operaçao == 2:
        vetor.reverse()
        print(vetor)
    elif operaçao == 0:
        print('programa finalizado')
    else:
        print('opção invalida, tente novamente')
--------------------------------------------------------
# exercicio 17

vetor = [11, -11, 34, 23, 56, -99, 99, 132, 87, -11]
for indice, valor in enumerate(vetor):
    if valor < 0:
        vetor.insert(indice, 0)
        vetor.pop((indice + 1))

print(vetor)
----------------------------------------------------
# exercicio 18

vetor = [11, 12, 34, 23, 56, 100, 99, 132, 87, 20]
multiplos = 0
x = int(input('informe o valor de x: '))
for n in vetor:
    if n % x == 0:
        multiplos = multiplos + 1

print(f'o vetor contem {multiplos} multiplos de {x}')
-----------------------------------------------------------
# exercicio 19
lista = []
for i in range(50):
    valor = ((i + 5 * i) % (i + 1))
    lista.append(valor)

print(lista)
print(len(lista))
------------------------------------
# exercicio 21
a = []
b = []
c = []
x = 0
w = 0
while x < 10:
    valor = int(input('informe um valor para o vetor A: '))
    x = x + 1
    a.append(valor)

while w < 10:
    valor = int(input('informe um valor para o vetor B: '))
    w = w + 1
    b.append(valor)

for i in range(10):
    elemento = a[i] - b[i]
    c.append(elemento)

print(c)
---------------------------------------------------------------------
# exercicio 22
vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 24, 56, 67, 89, 90, 22, 57]
resposta = []

for n in range(10):
    resposta.append(vetor1[n])
    resposta.append(vetor2[n])

print(resposta)
---------------------------------------------------
# exercicio 23
vetor1 = [5, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 24, 42]
resposta = []

for n in range(5):
    cal = vetor1[n] * vetor2[n]
    resposta.append(cal)

print(vetor1)
print(vetor2)
print(f'o produto escalor dos vetores é: {sum(resposta)}')
---------------------------------------------------------------
# exercicio 24
altura = [1.62, 1.70, 1.65, 1.90, 1.77, 1.60, 1.58, 1.85, 1.69, 1.64]
aluno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'o aluno mais alto é: {aluno[altura.index(max(altura))]}, com altura de {max(altura)}')
print(f'o aluno mais baixo é: {aluno[altura.index(min(altura))]}, com altura de {min(altura)}')
------------------------------------------------------------------------------------------------
# exercicio 25
vetor = []
i = 1

while len(vetor) < 100:
    if i % 7 != 0:
        if (i - 7) % 10 != 0:
            vetor.append(i)
    i = i + 1

print(vetor)
----------------------------------------------------
# exercicio 27
vetor = []
for n in range(10):
    valor = int(input('informe um valor para o vetor: '))
    vetor.append(valor)

mult = 0
primos = []

for valores in vetor:
    for cont in range(2, valores):
        if valores % cont == 0:
            mult = 1
    if mult == 0:
        print(f'o valor {valores} é primo!')
        print(f'ele se encontra na posição: {vetor.index(valores)}')
    mult = 0
--------------------------------------------------------------------
# exercicio 28
v = []
for n in range(10):
    valor = int(input('informe um valor para o vetor: '))
    v.append(valor)
v1 = []
v2 = []
for elem in v:
    if elem % 2 == 0:
          v1.append(elem)
    else:
        v2.append(elem)
print(f'os valores pares são {v1}')
print(f'os valores impares são: {v2}')
-----------------------------------------------------
# exercicio 29
v = []
for n in range(6):
    valor = int(input('informe um valor para o vetor: '))
    v.append(valor)
par = []
impar = []
for elem in v:
    if elem % 2 == 0:
          par.append(elem)
    else:
        impar.append(elem)
print(f'os valores pares são {par}')
print(f'a soma dos pares é: {sum(par)}')
print(f'os valores impares são: {impar}')
print(f'a quantidade de numeros impares é: {len(impar)}')
--------------------------------------------------------------------
# exercicio 30
v1 = []
for n in range(5):
    valor = int(input('informe um valor para o vetor 1: '))
    v1.append(valor)
v2 = []
for n in range(5):
    valor = int(input('informe um valor para o vetor 2: '))
    v2.append(valor)
sete = []
for elem in v1:
    if elem in v2:
        sete.append(elem)
s = set(sete)
print(f'a intersecção das listas é: {s}')
--------------------------------------------------
# exercicio 31
v1 = []
for n in range(5):
    valor = int(input('informe um valor para o vetor 1: '))
    v1.append(valor)
v2 = []
for n in range(5):
    valor = int(input('informe um valor para o vetor 2: '))
    v2.append(valor)
v1.extend(v2)
s = set(v1)
print(s)
-----------------------------------------------------------------
# exercicio 32
x = {}
y = {}
soma = []
mult = []
ambos = []
apx = []
elem = []
dictx = []
dicty = []

for n in range(5):
    valor = int(input('informe um valor para o vetor x: '))
    x.update({n: valor})
    valor = int(input('informe um valor para o vetor y: '))
    y.update({n: valor})

for n in range(5):
    valor1 = x.get(n)
    valor2 = y.get(n)
    soma.append((valor1 + valor2))
    mult.append((valor1 * valor2))
    elem.extend([valor1, valor2])
    #elem.append(valor2)
    dictx.append(valor1)
    dicty.append(valor2)
for d in dictx:
    if d in dicty:
        ambos.append(d)
    else:
        apx.append(d)

s = set(elem)
print(f'a soma dos elementos de x com y é igual a: {soma}')
print(f'a multiplicação dos elementos de x com y é igual a: {mult}')
print(f'os valore de x que nao tem em y são: {apx}')
print(f'os elementos que estão em ambos os vetores são: {ambos}')
print(f'todos os elementos adicionados: {s}')
------------------------------------------------------------------
# exercicio 34
vetor = []
for n in range(5):
    elemento = int(input('insira um valor: '))
    while elemento in vetor:
        print('valor repetido, por favor insira um valor novo!')
        elemento = int(input('insira um valor: '))
    vetor.append(elemento)
print(vetor)
-----------------------------------------------------------------
# exercicio 35
vetorA = []
vetorB = []
valorA = int(input('insira um valor: '))
valorB = int(input('insira um valor: '))
while valorA != 0:
    numero = valorA % 10
    vetorA.append(numero)
    valorA = (valorA/10) - (numero/10)

while valorB != 0:
    numero = valorB % 10
    vetorB.append(numero)
    valorB = (valorB/10) - (numero/10)

print(vetorB)
print(valorB)
print(vetorA)
print(valorA)

c = []
if len(vetorA) > len(vetorB):
    while len(vetorA) != len(vetorB):
        vetorB.append(0)
elif len(vetorB) > len(vetorA):
    while len(vetorB) != len(vetorA):
        vetorA.append(0)
y = 0
for n in range(len(vetorA)):
    cont = vetorA[n] + vetorB[n]
    if y == 1:
        cont = cont + 1
        y = 0
    if cont > 10:
        cont = cont - 10
        y = 1
    c.append(cont)

c.reverse()
print(c)
----------------------------------------------------
# exercicio 38
vetor = []
invertido = []

for n in range(11):
    valor = int(input('informe um valor: '))
    vetor.append(valor)
    vetor.sort()

print(vetor)
"""

