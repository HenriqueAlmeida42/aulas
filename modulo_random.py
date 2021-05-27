"""
- Módulos são arquivos python, ou seja qualquer arquivo python é um modulo
_ Módulo random possui varias funções para a geração de numeros pseudo-aleatorios

- Tem duas formas de se usar os modulos:
1- vc importa o modulo interio e todas as funções desse modulo ficam disponiveis para uso,
mas isso faz com que vc ocupe mais memória ja que agora todo o modulo esta importado.
sendo assim esse método NÃO É O MAIS RECOMENDADO

2 - vc importa somente a função do módulo que vc deseja usar, assim ocupa a sua memória somente
com uma função. RECOMENDADO.


# Forma 1 - importando todo o módulo

import random

# random() é uma função do módulo random que gera um numero real entre 0 e 1
print(random.random())

# OBS: para utilizar a função nesse método de importação vc presisa escrever:
# O nome do Módulo (.) o nome da função(), nao esquecendo de usar o ponto!!
------------------------------------------------------------------------------

# Forma 2 - importando uma função expecifica

from random import random

# É indicado de qual modulo vc deseja a função e depois importado a função desejada

for i in range(10):
    print(random())

# veja agora q para usar a função vc precisa somente chamar por ela sem ter q colocar o modulo na frente
----------------------------------------------------------------------------------------------------------

- Outras funções que se pode usar do módulo random:

1 - uniform() = essa função gera valores REAIS pseudo - aleatórios entre os valores determinados,
lembrando que o segundo valor nunca vai ser mostrado pois é ate ele.

# Exemplo uniform()

from random import uniform

for i in range(10):
    print(uniform(5, 10))
# OBS: o 10 não é incluido
--------------------------------------------

2 - randint() = gera valores INTEIROS pseudo-aleatorios entre os valores estabelecidos
segue as mesmas regras do anterior

# Exemplo randint()

from random import randint

# gerando valores para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # começa em 1 e vai ate 60, separa os vaores por , e nao por linha.
---------------------------------------------------------------------------------------------------------

3 - choice() = mostra um valor aleatório entre um interavel

# Exemplo choice()

from random import choice

jogadas = ['pedra', 'tesoura', 'papel']

print(choice(jogadas))

print(choice("Buceta Gostosa"))
# Imprime uma letra da string
-----------------------------------

4 - shuffle() = tem a função de embaralhar dados

# Exemplo shuffle()

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '6', '7', '4', '3']

print(cartas)

shuffle(cartas)  # embaralha a ordem dos dados na lista

print(cartas)
print(cartas.pop())

"""
