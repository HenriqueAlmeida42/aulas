import primeiro


def funcao2():
    primeiro.funcao1()


if __name__ == '__main__':
    funcao2()
    print('segundo.py esta sendo executado diretamente')
else:
    print(f'segundo.py esta sendo importado. {__name__}')
