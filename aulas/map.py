""""
MAP - com o map fazemos o mapeamento de valores para funções
import math


def area(r):
    "" calcula a area de um circulo com raio r ""
    return math.pi * (r ** 2)


print(area(2))
print(area(3))

raios = [2, 5, 5.6, 13, 2.22, 42]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - MAP
# map é uma função que recebe dois parametros: O primeiro a função, o segundo o interavel

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - usando lambda

print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: após a primeira utilização a função map zera o resutado!!!!
print(list(areas)) # ele surge como uma lista vazia

# OBS 2: o map gera um map object que é um interavel, ou seja eu posso colocar ele em um for por exemplo
# OBS 3: a função usada no map usa somente 1 parametro

# exemplo

cidades = [('curitiba', 20), ('japao', 25), ('hawaii', 32), ('Rucia', 2)]

print(cidades)

# conversao de celcios para fharenait

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))

"""
cidades = [('curitiba', 20), ('japao', 25), ('hawaii', 32), ('Rucia', 2)]

print(cidades)

# conversao de celcios para fharenait

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))