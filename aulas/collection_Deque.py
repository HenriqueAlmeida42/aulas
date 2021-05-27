""""
modulo collectios - Deque
https://docs.python.org/3/library/collections.html#collections.deque

podemos dizer que Deque é uma lista de alta performace.
podemos por exemplo adicionar ou retirar um elemento do lado esquerdo ao invez de
somente do lado direito

"""
#import
from collections import deque

# Criando um deque
deq = deque('great')

print(deq) # transfoma a string em uma lista contendo cada uma das letras como elementos

# adicionando elemnetos ao deque

deq.append('s') # adiciona ao final
print(deq)

deq.appendleft('w') # adiciona ao começo
print(deq)

# Removendo elementos ao deque

print(deq.pop()) # remove e retorna o ultimo elemento
print(deq)

print(deq.popleft()) # remove e retorna o primeiro elemento
print(deq)
