"""

*args

- O que é?
- o parametro *args quando utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla;
- *args é uma convenção, qualquer nome ultilizando * funcionaria, ex: *bu;
- se utiliza *args nos parametros, mas para usa-la utiliza somente args;
- o *args é opcional, serve para armazenar caso seja passado mais valores do que devia;
- a tupla gerada pelo *args pode receber qualquer tipo de variavel menos dicionarios (tome cuidado)
- *args pode receber uma coleção mas, pode necessitar desempacotar os dados para poder interagir de forma correta


# exemplo de *args


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(3, 4, 5, 6))
print(soma_todos_numeros(23.45, 43.1, 3, 42))

------------------------------------------------------
# exemplo de *args com outros parametros


def soma_todos_numeros(nome, buceta='boa',*args):
    return sum(args)


print(soma_todos_numeros('tt'))
print(soma_todos_numeros('tt', 1))# nome= tt, buceta= 1 e args fica sem dado
print(soma_todos_numeros('re', 'gg', 3, 4, 5, 6))
print(soma_todos_numeros(23.45, 43.1, 3, 42))
--------------------------------------------------------------------------------
# exemplo de desempacotador com *args


def soma(*args):
    print(args)
    return sum(args)


numeros = [1, 2, 3, 4, 5, 6]

# print(soma(numeros)) gera erro pois pro args toda a lista é um unico argumento

print(soma(*numeros)) # ao colocar o * ele desmpacota os valores/transfoma na tupla e interagem com cada um deles.

--------------------------------------------------------------------------------------------------------------------
OBS1: o desenpacotamento pode ser usado sem o *args, só utilizar ele no argumento

OBS2: mantenha a seguinte ordem dos parametros para não bugar a logica do default

1- Parametros obrigatorios;
2- *args;
3- parametros default;
4- **kwargs

assim vc nao corre o risco de colocar um valor errado em um parametro default

"""
