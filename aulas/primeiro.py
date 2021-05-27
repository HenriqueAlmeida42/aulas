
def funcao1():
    print('buceta- primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('primeiro esta sendo  executado diretamente')
else:
    print(f'primeiro.py foi importado. {__name__}')
