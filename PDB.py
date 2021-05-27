"""
PDB - python debugger

OBS: debuggar usando o print() é uma pratica ruim, deve-se usar o PDB

No PyCharm existe uma forma de debuggar sem usar o PDB diretamente, mas caso esteja em outra ide
use o PDB

# Exemplo de debuggar no PyCharm


def divisao(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu o problema: {err}'


print(divisao(4, 0))

# No PyCharm vc pode clicar ao lado da linha na qual vc quer a informação e clicar no simbolo de inseto
# para começar a debuggar e então usar os comandos do painel do PyCharm para realizar o debugge
# se vc copiar uma função tipo: int(a) / int(b), e clicar com o botao direito e ir em add to whatches,
# ele vai passar a verificar o resultado da ação
------------------------------------------------------------------------------------------------------------

# Exemplo de debuggar no PDB - Python Debugger (importando) 1

# ** Para usar o PDB temos q importar a blibioteca PDB e usar o comando pdb.set_trace()
# ** NÃO É NEECESSARIO IMPORTAR A PARTIR DO PYTHON VERSÃO 3.7, usa-se agora o comando breakpoint()

# Comandos para usar o PDB
# l (lista onde estamos no codgo)
# n (vai para a proxima linha)
# p (imprime a variavel)
# c (continua a execução - finaliza o debugge)

# OBS: ele somente apresenta o valor da variavel a cima da linha em que esta

import pdb

nome = 'fernanda'
sobrenome = 'price'
pdb.set_trace()
nome_completo = nome + '  ' + sobrenome
gosta = 'sexo anal'
final = nome_completo + ' gosta de ' + gosta
print(final)
----------------------------------------------------------------------------------------

# Exemplo de debuggar no PDB - Python Debugger (importando) 2

# ** Para usar o PDB temos q importar a blibioteca PDB e usar o comando pdb.set_trace()
# ** NÃO É NEECESSARIO IMPORTAR A PARTIR DO PYTHON VERSÃO 3.7, usa-se agora o comando breakpoint()

# Comandos para usar o PDB
# l (lista onde estamos no codgo)
# n (vai para a proxima linha)
# p (imprime a variavel)
# c (continua a execução - finaliza o debugge)

# OBS: ele somente apresenta o valor da variavel a cima da linha em que esta
# OBS2: posso importar no meio do codgo pq é so para teste, entao vou remover apos o uso
# OBS3: usar o ; le permite usar mais de um comando na mesma linha

nome = 'fernanda'
sobrenome = 'price'
import pdb; pdb.set_trace()
nome_completo = nome + '  ' + sobrenome
gosta = 'sexo anal'
final = nome_completo + ' gosta de ' + gosta
print(final)
----------------------------------------------------------------------------------------------

# Exemplo de debuggar no PDB - Python Debugger inserido no sitema ( breakpoint() )

# Comandos para usar o PDB no breakpoint() usa os mesmos comandos

# l (lista onde estamos no codgo)
# n (vai para a proxima linha)
# p (imprime a variavel)
# c (continua a execução - finaliza o debugge)

# OBS: ele somente apresenta o valor da variavel a cima da linha em que esta
# OBS2: Não é nescessario importar

nome = 'fernanda'
sobrenome = 'price'
breakpoint()
nome_completo = nome + '  ' + sobrenome
gosta = 'sexo anal'
final = nome_completo + ' gosta de ' + gosta
print(final)

"""
# Exemplo de debuggar no PDB - Python Debugger inserido no sitema ( breakpoint() )

# Comandos para usar o PDB no breakpoint() usa os mesmos comandos

# l (lista onde estamos no codgo)
# n (vai para a proxima linha)
# p (imprime a variavel)
# c (continua a execução - finaliza o debugge)

# OBS: ele somente apresenta o valor da variavel a cima da linha em que esta
# OBS2: Não é nescessario importar

nome = 'fernanda'
sobrenome = 'price'
breakpoint()
nome_completo = nome + '  ' + sobrenome
gosta = 'sexo anal'
final = nome_completo + ' gosta de ' + gosta
print(final)
