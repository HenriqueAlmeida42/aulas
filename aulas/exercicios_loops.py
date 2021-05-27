""""
1-
for num in range(1,6):
    mult = num * 3
    print(mult)
3-
num = 10
while num != -1:
    print(num)
    num = num - 1
print("fim!")
5-
n = 0
conta = 0

while n != 10:
    num = float(input('quanto devo somar a conta? '))
    conta = conta + num
    n = n + 1
print(conta)
11-
num = int(input('informe o numero: '))
n = 0
for n in range(0, num + 1):
    if n != (num + 1):
        print(n)
12-
num = int(input('informe o numero: '))
n = num
for n in range(num, -1, -1):
    if n != -1:
        print(n)
    n - 1
13-
num = int(input('informe o numero: '))
n = 0
for n in range(0, num + 1, 2):
    if n != (num + 1):
        print(n)
16-
num = int(input('informe um numero impar: '))

while num %2 == 0:
    num = int(input('esse numero não é impar, por favor infome um numero impar: '))
for n in range(num, -1, -1):
    if n %2 != 0:
        print(n)
20-
num = int(input('informe um numero de 0 a 999: '))
pares = 0
qd = 0

while num != 1000:
    if num %2 == 0:
        pares = pares + 1
    qd = qd + 1
    num = int(input('digite 1000 para encerrar ou informe um numero de 0 a 999: '))
print(f'foram informados {pares} numeros pares em {qd} ciclos do programa')
21-
num1 = int(input('informe o primeiro numero: '))
num2 = int(input("informe o segundo numero: "))
pares = 0
impares = 0

if num1 > num2:
    impares = 1
    for n in range(num2, num1 + 1):
        if n %2 == 0:
            pares = pares + n
        else:
            impares = impares * n
elif num2 > num1:
    impares = 1
    for n in range(num1, num2 + 1):
        if n %2 == 0:
            pares = pares + n
        else:
            impares = impares * n
print(f'a soma dos numeros pares desse intervalo é = {pares}, e a multiplicacao dos impares é = {impares}')
41-
opcao = 0
while opcao != 2:
    print(  [1] calcular associacao de resistores em paralelo
    [2] sair do programa)
    opcao = int(input('qual a opcao desejada?: '))
    if opcao == 1:
        r1 = float(input('valor do primeiro resistor: '))
        r2 = float(input('valor do segundo resistor: '))
        r = ((r1*r2)/(r1+r2))
        print(f'o resistor equivalente é de: {r:.2f} ohms')
"""
opcao = 0
while opcao != 2:
    print(""""   [1] calcular associacao de resistores em paralelo
    [2] sair do programa""")
    opcao = int(input('qual a opcao desejada?: '))
    if opcao == 1:
        r1 = float(input('valor do primeiro resistor: '))
        r2 = float(input('valor do segundo resistor: '))
        r = ((r1*r2)/(r1+r2))
        print(f'o resistor equivalente é de: {r:.2f} ohms')


