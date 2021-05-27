""""
**kwargs

O que é?
- basicamente o mesmo q *args só que para dicionarios;
- nome é convenção, só importa os **;
- nào é obrigatorio;
- da para desempacotar usando **, mas é preciso que a chave tenha o mesmo valor tanto no
parametro quanto no argumento;
- pode desempacotar sem ter o **kwargs;
- segue o mesmo esquema de ordem dos parametros:
1- parametros obrigatorios;
2- *args;
3- parametros default;
4- **kwargs


# exemplo de **kwargs


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(julia='verde', marcos='azul', pedro='preto')
-----------------------------------------------------------------

# exemplo de **kwargs 2


def cumprimento(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'python':
        return 'vc recebeu um cumprimento pythomico!!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']}, Geek!"
    return 'nao tenho certeza de quem vc é...'


print(cumprimento())
print(cumprimento(geek='python'))
print(cumprimento(geek='oi'))
print(cumprimento(geek='buceta'))
-------------------------------------------------------------

"""
# exemplo de desempacotamento


def soma_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

dicionario = dict(a=1, b=2, c=3) # precisa ter os mesmos nomes que os parametros

soma_numeros(*lista) # seria um exemplo do *args, é so pra mostras q nao precisa deles na função
soma_numeros(*tupla)
soma_numeros(*conjunto)

soma_numeros(**dicionario) # funcionaria igual se tivesse o **kwargs, a diferença seria eu imprimir os kwargs

