""""
exercicios da secao04
1-
numero = 34
print(numero)
2-
numero = 42.5
print(numero)
print(type(numero))
3-
n1 = int(input('informe o primeiro numero: '))
n2 = int(input('informe o segundo numero: '))
n3 = int(input('informe o terceiro numero: '))
soma = n1 + n2 + n3
print(soma)
4-
n1 = int(input('informe o numero: '))
quadrado = n1 * n1
print('o quadrado do numero é: {}'.format(quadrado))
5-
n1 = int(input('informe o numero: '))
q = n1/5
print('a quinta parte do numero é: {}'.format(q))
6-
celcius = float(input('informe a temperatura: '))
farenat = (celcius * (9/5) + 32)
print('a temperatura em farenat é: {}'.format(farenat))
7-
farenat = float(input('informe a temperatura: '))
celcius = (5 * (farenat - 32) / 9)
print('a temperatura em celcius é: {}'.format(celcius))
10-
km = float(input('informe a velocidade em km/h: '))
ms = (km / 3.6)
print('a velocidade em m/s é: {}'.format(ms))
12-
milha = float(input('informe a distancia em milhas: '))
km = (1.61 * milha)
print('a distancia em km é: {}'.format(km))
28-
n1 = float(input('informe o primeiro valor: '))
n2 = float(input('informe o segundo valor: '))
n3 = float(input('informe o terceiro valor: '))
n1 = n1 * n1
n2 = n2 * n2
n3 = n3 * n3
soma = (n1 + n2 + n3)
print('a soma dos quadrados é = {}'.format(soma))
29-
n1 = float(input('informe o primeiro valor: '))
n2 = float(input('informe o segundo valor: '))
n3 = float(input('informe o terceiro valor: '))
n4 = float(input('informe o quarto valor: '))
media = (n1 + n2 + n3 + n4) / 4
print('a media é = {}'.format(media))
31-
numero = int(input('informe o valor: '))
n1 = numero - 1
n2 = numero + 1
print('seu antecessor é: {}, e seu sucessor é: {}'.format(n1,n2))
32-
numero = int(input('informe o valor: '))
n1 = (numero * 3) + 1
n2 = (numero * 2) - 1
soma = n1 + n2
print('a soma é = {}'.format(soma))
40-
dias = int(input('informe a quantidade de dias trabalhados: '))
imposto = ((dias * 30) * 8) / 100
pagamento = (dias * 30) - imposto
print("o pagamento será de {}".format(pagamento))
43-

"""
valor = float(input('informe o valor do produto :'))
opcao = 0
while opcao != 6:
    print(""""[1] compra a vista
    [2] parcelamento em 3x sem juros
    [3] comissao do vendedor a vista
    [4] comissao do vendedor parcelado
    [5] informar outro valor
    [6] encerrar o programa""")
    opcao = int(input('qual a opcao desejada?  '))
    if opcao == 1:
        desconto = valor - ((valor * 10) / 100)
        print("o valor com desconto de 10% é: {} reais".format(desconto))
    elif opcao == 2:
        parcelamento = valor / 3
        print('serao 3 parcelas de: {} reais'.format(parcelamento))
    elif opcao == 3:
        desconto = valor - ((valor * 10) / 100)
        cav = ((desconto * 5) / 100)
        print('a comissao do vendedor sera: {} reais'.format(cav))
    elif opcao == 4:
        cp = ((valor * 5 ) / 100)
        #print('a comissao do vendedor sera: {} reais'.format(cp))
        print(f'a comissao do vendedor sera: {cp} reais')
    elif opcao == 5:
        valor = float(input('informe o novo valor: '))
    elif opcao == 6:
        print('finalizando...')
    else:
        print("opcao invalida, tente novamente")
    print('=-=' * 10)
print('program encerrado')

