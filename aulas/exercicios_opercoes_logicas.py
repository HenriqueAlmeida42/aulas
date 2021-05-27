""""
teste de raiz quadrada e tripla:

numero = float(input('insira um numero: '))
rq = numero ** (1/2)
rt = numero ** (1/3)
print(f'a raiz quadra é: {rq} \na raiz tripla é: {rt:.2f} ')
2-
numero = float(input('insira um numero: '))
if numero > 0:
    rq = numero ** (1/2)
    print(f'a raiz quadrada é: {rq:.2f}')
elif numero == 0:
    print('zero nao possui raiz')
else:
    print('numero invalido.')
3-
numero = float(input('insira um numero: '))
if numero > 0:
    rq = numero ** (1/2)
    print(f'a raiz quadrada é: {rq:.2f}')
else:
    quadrado = numero ** 2
    print(f'numero ao quadrado é: {quadrado:.2f}')
5-
numero = float(input('insira um numero: '))
if numero % 2 == 0:
    print('o numero é par')
else:
    print('o numero é impar')
6 e 7 juntos -
n1 = float(input('insira o primeiro numero: '))
n2 = float(input('insira o segundo numero: '))

if n1 > n2:
    d1 = n1 - n2
    print(f'o numero {n1} é o maior e a diferenca entre eles é de {d1}')
elif n2> n1:
    d2 = n2 - n1
    print(f'o numero {n2} é o maior e a diferenca é de {d2}')
else:
    print('numeros iguais')
8-
nota1 = float(input('insira a primeira nota: '))
nota2 = float(input('insira a segunda nota: '))

if not -0.9 < nota1 < 10.1:
    print('primeira nota invalida')
elif not -0.9 < nota2 < 10.1:
    print('segunda nota invalida')
else:
    print('a media é de: {:.2f}'.format((nota1 + nota2)/2))
9-
salario = float(input('insira seu salario: '))
emprestimo = float(input('insira o valor de emprestimo desejado: '))
prestacao = int(input('insira quantas prestacoes deseja pagar o emprestimo: '))

parcela = emprestimo / prestacao
porcentagem = (salario * 20) / 100

if parcela > porcentagem:
    print('emprestimo negado')
else:
    print('emprestimo concedido')

"""
for num in range(10, 55, 5):
    print(num)