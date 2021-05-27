""""
Lambdas são funções sem nome

Como utilizar uma expressão lambda:
cal = lambda x: 3 * x + 1

- basicamente vc adiciona um nome para a função ou coloca ela direto a onde ela deve agir (como nos proximos
exemplo), escreve lambda, a variaverl (que pode ser nenhuma ou quantas vc quiser) coloca (:) e escreve a
função que ela deve retornar;
- se for passado mais ou menos argumentos do que devia da TypeError

# exemplo de lambda direto a onde vc vai usar ela
autores = ['Isaac Asimov', 'Tony Stark', 'Peter Parker', 'Arthur C. Clark', 'Kvolth Almeida', 'Douglas Adams',
           'Patrick Rhufus']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
------------------------------------------------------------------------
# exemplo de usar lambda em uma função

# Função quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a função


def gerador_funcao_quadatica(a, b, c):
     ""retorna  a função f(x) = a * x ** 2 + b * x + c""
    return lambda x: a * x ** 2 + b * x + c


teste = gerador_funcao_quadatica(2, 3, 5)

print(teste(2))
print(teste(5))
print(teste(6))

print(gerador_funcao_quadatica(2, 1, -5)(2))
# A função chama pelos tres primeiros numeros(a, b, c) e a lambda chama pelo x

"""
# exemplo de usar lambda em uma função

# Função quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a função


def gerador_funcao_quadatica(a, b, c):
    """ retorna  a função f(x) = a * x ** 2 + b * x + c """
    return lambda x: a * x ** 2 + b * x + c


teste = gerador_funcao_quadatica(2, 3, 5)

print(teste(2))
print(teste(5))
print(teste(6))

print(gerador_funcao_quadatica(2, 1, -5)(2))
# A função chama pelos tres primeiros numeros(a, b, c) e a lambda chama pelo x
