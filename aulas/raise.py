"""
Levantando os proprios erros com raise

raise = lança exceções

OBS: o raise nao é uma função. É uma palavra reservada. Para simplificar pense no raise como sendo util para
que possamos criar nossas proprias exeções  e mensagens de erro

a forma geral de utilizar é:

raise TipoDoErro('mensagem de erro')

# exemplo


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O texto {texto} vai ser impresso na cor {cor}')


colore(True, 'azul')


# exemplo refatorado


def colore(texto, cor):
    cores = ('verde', 'vermelho', 'preto')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} vai ser impresso na cor {cor}')


colore('buceta', 'azul')

"""

# exemplo


def colore(texto, cor):
    cores = ('verde', 'vermelho', 'preto')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} vai ser impresso na cor {cor}')


colore('buceta', 'azul')
