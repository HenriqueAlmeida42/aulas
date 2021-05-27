""""
lista execicios coleções parte 2
------------------------------------------------
# exercicio 1
matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
mqd = []

for l in range(0, 4):
    for c in range(0, 4):
        matrix [l] [c] = int(input(f'digite um valor para [{l} {c}]: '))

for l in range(0, 4):
    for c in range(4):
        print(f'{matrix [l] [c]:^5}', end='')
        if matrix [l] [c] > 10:
            mqd.append(matrix [l] [c])

    print()
print(f'essa matriz tem {len(mqd)} numeros maiores que 10')
--------------------------------------------------------------
# exercicio 2
matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
mqd = []

for l in range(0, 5):
    for c in range(0, 5):
        matrix [l] [c] = 0
        if l == c:
            matrix [l] [c] = 1

for l in range(0, 5):
    for c in range(5):
        print(f'{matrix [l] [c]:^5}', end='')
    print()
---------------------------------------------------------
# exercicio 4
matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
mqd = []
me = 0

for l in range(4):
    for c in range(4):
        matrix [l] [c] = int(input(f'digite o valor da pocisão [{l}, {c}]: '))
        if matrix [l] [c] > me:
            me = matrix [l] [c]
            a = l + 1
            b = c + 1

for l in range(4):
    for c in range(4):
        print(f'{matrix [l] [c]:^5}', end='')
    print()

print(f' o maior elemento esta na linha:{a}, coluna:{b}')
--------------------------------------------------------------
# exercicio 4
matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
mqd = []
me = 0

for l in range(4):
    for c in range(4):
        matrix [l] [c] = int(input(f'digite o valor da pocisão [{l}, {c}]: '))
        if matrix [l] [c] > me:
            me = matrix [l] [c]
            a = l + 1
            b = c + 1

for l in range(4):
    for c in range(4):
        print(f'{matrix [l] [c]:^5}', end='')
    print()

print(f' o maior elemento esta na linha:{a}, coluna:{b}')
--------------------------------------------------------------------------------------
# exercicio 5
matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
s = 0
for l in range(5):
    for c in range(5):
        matrix [l] [c] = int(input(f'digite o valor da pocisão [{l}, {c}]: '))

x = int(input('digite o valor a ser procurado: '))
for l in range(5):
    for c in range(5):
        if x == matrix[l] [c]:
            print(f'o valor {x} se encontra na pocisao: {l + 1}, {c + 1}')
            s = 1

if s != 1:
    print(f'valor {x} não encontrado')

for l in range(5):
    for c in range(5):
        print(f'{matrix [l] [c]:^5}', end='')
    print()
-------------------------------------------------------------
# exercicio 6
matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matrix2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(4):
    for c in range(4):
        matrix [l] [c] = int(input(f'digite o valor para a matriz 1: '))

for l in range(4):
    for c in range(4):
        matrix2 [l] [c] = int(input(f'digite o valor para a matriz 2: '))

for l in range(4):
    for c in range(4):
        if matrix [l] [c] > matrix2 [l] [c]:
            matriz [l] [c] = matrix [l] [c]
        else:
            matriz [l] [c] = matrix2 [l] [c]

for l in range(4):
    for c in range(4):
        print(f'{matriz [l] [c]:^5}', end='')
    print()
-----------------------------------------------------------------
# exercicio 7
matrix = [[], [], [], [], [], [], [], [], [], []]

for l in range(len(matrix)):
    for c in range(len(matrix)):
        if l < c:
            v = (2*l) + (7*c) -2
            matrix[l].insert(c,  v)

        elif l == c:
            v = (3 * l**2)-1
            matrix[l].insert(c, v)

        elif l > c:
            v = (4 * l**3) - (5 * c**2) + 1
            matrix[l].insert(c, v)

for l in range(len(matrix)):
    for c in range(len(matrix)):
        print(f'{matrix[l][c]:^5}', end='')
    print()
--------------------------------------------------
# exercicio 8
matrix = [[], [], []]
soma = 0

for l in range(len(matrix)):
    for c in range(len(matrix)):
        v = int(input(f'digite o valor da posição {l},{c}: '))
        matrix[l].insert(c, v)
        if c > l:
            soma += v


for l in range(len(matrix)):
    for c in range(len(matrix)):
        print(f'{matrix[l][c]:^5}', end='')
    print()

print(f'a soma dos valores acima da diagonal principal é = {soma}')
--------------------------------------------------------------------------
# exercicio 9
matrix = [[], [], []]
soma = 0

for l in range(len(matrix)):
    for c in range(len(matrix)):
        v = int(input(f'digite o valor da posição {l},{c}: '))
        matrix[l].insert(c, v)
        if l > c:
            soma += v


for l in range(len(matrix)):
    for c in range(len(matrix)):
        print(f'{matrix[l][c]:^5}', end='')
    print()

print(f'a soma dos valores a baixo da diagonal principal é = {soma}')
--------------------------------------------------------------------------
# exercicio 10
matrix = [[], [], []]
soma = 0

for l in range(len(matrix)):
    for c in range(len(matrix)):
        v = int(input(f'digite o valor da posição {l},{c}: '))
        matrix[l].insert(c, v)
        if l == c:
            soma += v


for l in range(len(matrix)):
    for c in range(len(matrix)):
        print(f'{matrix[l][c]:^5}', end='')
    print()

print(f'a soma dos valores da diagonal principal é = {soma}')
--------------------------------------------------------------------------
# exercicio 11
matrix = [[], [], []]
soma = 0

for l in range(len(matrix)):
    for c in range(len(matrix)):
        v = int(input(f'digite o valor da posição {l},{c}: '))
        matrix[l].insert(c, v)
        if (l + c) == 2:
            soma += v


for l in range(len(matrix)):
    for c in range(len(matrix)):
        print(f'{matrix[l][c]:^5}', end='')
    print()

print(f'a soma dos valores diagonal secundaria é = {soma}')
------------------------------------------------------------------
# exercicio 12
matrix = [[], [], []]
matrizT = [[], [], []]

for l in range(len(matrix)):
    for c in range(len(matrix)):
        v = int(input(f'digite o valor da posição {l},{c}: '))
        matrix[l].insert(c, v)
        matrizT[c].insert(l, v)


for l in range(len(matrix)):
    for c in range(len(matrix)):
        print(f'{matrix[l][c]:^5}', end='')
    print()

print('a matriz transposta é:')

for l in range(len(matrizT)):
    for c in range(len(matrizT)):
        print(f'{matrizT[l][c]:^5}', end='')
    print()
-------------------------------------------------------
# exercicio 13
matrix = [[], [], [], []]
matrizT = [[], [], [], []]
v = 0
for l in range(len(matrix)):
    for c in range(len(matrix)):
        v += 1
        matrix[l].insert(c, v)
        matrizT[l].insert(c, v)
        if c > l:
            matrizT [l].insert(c, 0)

for l in range(len(matrix)):
    for c in range(len(matrix)):
        print(f'{matrix[l][c]:^5}', end='')
    print()

print('a matriz triangular inferior é:')

for l in range(len(matrizT)):
    for c in range(len(matrizT)):
        print(f'{matrizT[l][c]:^5}', end='')
    print()
------------------------------------------------------------
# exercicio 14
import random
matrix = [[], [], [], [], []]

for l in range(len(matrix)):
    for c in range(len(matrix)):
        v = random.randint(0, 99)
        matrix[l].insert(c, v)

for l in range(len(matrix)):
    for c in range(len(matrix)):
        print(f'{matrix[l][c]:^5}', end='')
    print()
INCOMPLETO!!!!!
----------------------------------------------------
# exercicio 15

matrix = [['a', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'b', 'a'],
          ['b', 'a', 'c', 'a', 'd', 'a', 'c', 'a', 'c', 'a'],
          ['c', 'a', 'd', 'c', 'b', 'a', 'b', 'd', 'c', 'b'],
          ['d', 'b', 'a', 'd', 'a', 'a', 'a', 'b', 'd', 'c'],
          ['d', 'c', 'b', 'a', 'd', 'c', 'b', 'a', 'd', 'c']]

resp = ('d', 'c', 'b', 'a', 'd', 'c', 'b', 'a', 'd', 'c')
resutado = [[], [], [], [], []]

for l in range(5):
    for c in range(10):
        if matrix [l] [c] == resp[c]:
            resutado[l].insert(c, 1)
    print(f'a pontuação do aluno {l} é: {sum(resutado[l])}')
---------------------------------------------------------------------
# exercicio 16
matrix = [['d', 'c', 'b', 'a', 'd', 'c', 'b', 'a', 'b', 'a'],
          ['b', 'a', 'c', 'a', 'd', 'a', 'c', 'a', 'c', 'a'],
          ['c', 'a', 'd', 'c', 'b', 'a', 'b', 'd', 'c', 'b']]

resp = ('d', 'c', 'b', 'a', 'd', 'c', 'b', 'a', 'd', 'c')
resutado = [[], [], []]

for l in range(3):
    for c in range(10):
        if matrix [l] [c] == resp[c]:
            resutado[l].insert(c, 1)
    print(f'o aluno {l} teve nota: {sum(resutado[l])}')
    for c in range(10):
        print(f'{matrix[l][c]:^5}', end='')
    print()
    if sum(resutado[l]) >= 7:
        print('aluno aprovado')
    else:
        print('aluno reprovado')
    print()
------------------------------------------------------------------
# exercicio 17
import random
matrix = [[], [], [], [], [], [], [], [], [], []]
p1 = 0
p2 = 0
p3 = 0

for l in range(len(matrix)):
    for c in range(3):
        v = random.randint(0, 100)
        matrix[l].insert(c, v)

for l in range(10):
    if matrix[l][0] < matrix[l][1] or matrix[l][0] < matrix[l][2]:
        p1 += 1
    elif matrix[l][1] < matrix[l][0] or matrix[l][1] < matrix[l][2]:
        p2 += 1
    elif matrix[l][2] < matrix[l][0] or matrix[l][2] < matrix[l][1]:
        p3 += 1

print(f'o numero de alunos cuja a nota foi pior na primeira prova é: {p1}')
print(f'o numero de alunos cuja a nota foi pior na segunda prova é: {p2}')
print(f'o numero de alunos cuja a nota foi pior na terceira prova é: {p3}')
-------------------------------------------------------------------------------
# exercicio 18
matrix = [[], [], []]
matrixT = [[], [], []]
soma = []

for l in range(len(matrix)):
    for c in range(3):
        v = int(input('digite um valor: '))
        matrix[l].insert(c, v)
        matrixT[c].insert(l, v)

for c in range(3):
    soma.append(sum(matrixT[c]))

print(soma)
--------------------------------------------------------------
# exercicio 19
matrix = [[], [], [], [], []]
mm = 0
nf = 0

for l in range(len(matrix)):
    for c in range(4):
        if c == 0:
            v = int(input('informe a matricula do aluno: '))
            matrix[l].insert(c, v)
        if c == 1:
            v = int(input('informe a media da prova: '))
            matrix[l].insert(c, v)
        if c == 2:
            v = int(input('informe a media dos trabalhos: '))
            matrix[l].insert(c, v)
        if c == 3:
            v = (matrix[l][1] + matrix[l][2]) / 2
            matrix[l].insert(c, v)

for c in range(4):
    if mm < matrix[c][3]:
        mm = matrix[c][3]
        aluno = matrix[c][0]
        nf += matrix[c][3]

print(f'a media aritimetica dos alunos é: {(nf / 5)}')
print(f'o aluno que tirou a maior foi o: {aluno}')
------------------------------------------------------------

"""
# exercicio 20
matrix = [[], [], []]
sdq = 0
si = 0

for l in range(len(matrix)):
    for c in range(6):
        v = float(input('informe um valor para a matriz: '))
        matrix[l].insert(c, v)

for l in range(len(matrix)):
    for c in range(6):
        print(f'{matrix[l][c]:^5}', end='')
    print()

for l in range(len(matrix)):
    for c in range(6):
        if (c % 2) != 0:
            v = matrix[l][c]
            si += v
        if c == 1 or c == 3:
            v = matrix[l][c]
            sdq += v
        if c == 5:
            v = (matrix[l][0] + matrix[l][1])
            matrix[l].insert(c, v)
print()
print('matriz atualizada')

for l in range(len(matrix)):
    for c in range(6):
        print(f'{matrix[l][c]:^5}', end='')
    print()
