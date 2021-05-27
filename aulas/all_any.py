"""
all e any

all() - retorna true se todos os elementos do interavel sao verdadeiros ou ainda se o interavel esta vazio

# exemplo de all()

print(all([0, 1, 2, 3, 4])) # todos os numeros sao  verdadeiros? false
print(all([1, 2, 3, 4]))
print(all((1, 2, 3, 4)))
print(all([]))
print(all('buceta'))

nomes = ['carlos', 'carla', 'catia', 'cristian']
print(all([nome[0] == 'c' for nome in nomes]))


- any() - retorna true se qualquer elemento do interval for verdadeiro. Se o interavel estiver vazio, retorna false.
"""
# exemplo de any()

print(any([0, 1, 2, 3, 4]))  # True
print(any(['']))
print(any([0, False, {}, (), []]))  # False


nomes = ['carlos', 'carla', 'catia', 'cristian', 'lola']
print(any([nome[0] == 'c' for nome in nomes]))
