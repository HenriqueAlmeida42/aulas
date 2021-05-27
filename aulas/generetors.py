"""
Generators

- é uma mistura dos conceitos de list comprehension com por exemplo o map, pq?
- PQ: por que vc vai usar ele que nem um list, mas ao inves de gerar uma lista e gravar a lista na memoria
ele gera um generator object que nem um map object, ou seja, um objeto interavel que pose ser convertido em uma
uma lista ( tuple, set e todos os outros) e é apagado após o primeiro uso

- deve-se preferir utilizar ele pois ocupa um espaço em memoria muito menor que os outros comprehensions
deixando assim o codgo com melhor performaçe

-------------------------------------------------------------------------------------------------------------
# usando o any e o list comprehension
nomes = ['fernada', 'fabiana', 'fabricio', 'nutella']

print(any([nome[0] == 'f' for nome in nomes]))

# usando o generator pra fazer o mesmo
nomes = ['fernada', 'fabiana', 'fabricio', 'nutella']

print(any(nome[0] == 'f' for nome in nomes))  # Para usa o Generator só presisa estar entre parenteses()

# List comprehension
res = [nome[0] == 'f' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'f' for nome in nomes)
print(type(res))
print(res)
----------------------------------------------------------
# interando com o Generator
gen = getsizeof(x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
------------------------------------------------------------

"""
# Usando o getsizeof() importado da biblioteca sys para verificar a quantidade de bytes do elemento
from sys import getsizeof

# Gerando uma lista de numeros com o List comprehensions
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com o Set comprehensions
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com o dictionary comprehensions
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando um Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória:')
print(f'List comprehension: {list_comp} bytes')
print(f'Set comprehension: {set_comp} bytes')
print(f'Dictionary comprehension: {dict_comp} bytes')
print(f'Generator: {gen} bytes')
