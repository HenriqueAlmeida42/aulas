"""
reduce() - é uma função que precisa ser importada a partir do modulo 'functools'

- assim como o map() recebe 2 parametros, uma função e um interavel, mas diferente do map()
a função do reduce precisa receber 2 parametros

99% das vezes da pra resolver usando um loop for, que provalvelmente vai ser mais legivel

 Para entender o reduce()

# Imagine que vc tem uma coleção de dados (qualquer tipo, desde que, seja interavel)

dados = [a1, a2, a3,..., an]

# E vc tem uma função que recebe 2 parametros

def função(x, y):
    return x * y

reduce(função, dados)

# A função reduce funciona da seguinte forma:
    passo 1: res1 = f(a1, a2) #aplica a função nos dois primeiros elementos da coleção e guarda o resutado
    passo 2: res2 = f(res1, a3) #aplica a função passando o resutado do passo 1 mais o terceiro elemento
    passo 3: res3 = f(res2, a4)

    isso é repetido ate o final.
    .
    .
    .
    passo n: resn = f(resn-1, an)

- ou seja a cada passo o reduce() aplica a função passando como primeiro dado o resultado do passo anterior.
no final reduce() irá retornar o resultado final

"""
# Como funciona na pratica:

# utilizando reduce para multiplicar os dados de uma lista

from functools import reduce

dados = [2, 34, 56, 77, 42, 11, 13, 21]

# Para usar o reduce() precisamos de uma função que utilize 2 parametros

mult = lambda x, y: x * y

res = reduce(mult, dados)
print(res)

# Utilizando um loop normal:

res = 1
for n in dados:
    res = res * n

print(res)
