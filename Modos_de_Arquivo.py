"""
Modos de abertura de arquivo ( usando open )

r -> abre para leitura (Padrao)
w -> abre para escrita (Sobre escreve o arquivo que ja existia)
x -> abre para escrita somente se o arquivo nao exitir. caso ja exista da FileExistError
a -> abre apara escrita, adicionando o conteudo no final do arquivo
+ -> abre o modo de atualização: Leitura e escrita (Temos o controle do cursor)
# OBS: abrindo o modo 'a' -> append, se o arquivo nao existir sera criado.

# Exemplo x
try:
    with open('treino.txt', 'x') as arquivo:
        arquivo.write('a minha namorada é uma gostosa \n')
except FileExistsError:
    print('Arquivo ja existe')

# Exemplo de escrita com a
with open('treino.txt', 'a') as arquivo:
    while True:
        fruta = input('informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break


# Exemplo de escrita com r+
with open('treino.txt', 'r+') as arquivo:
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

"""
"""
StringIO

 Atenção, para ler e escrever dados em arquivos do sistema operacional o softeware
 precisa ter permição
 
StringIO -> utilizado para criar arquivos em memória.  
"""

# Primeiro fazemos import
from io import StringIO

mensagem = " este é apenas uma string normal "

# Podemos criar um arquivo em memoria ja com uma string inserida ou até mesmo vazio
arquivo = StringIO(mensagem)  # arquivo = open('arquivo.txt', 'w')

print(arquivo.read())

# Escrevendo outros textos
arquivo.write('outro texto')

# Podemos movimentar o cursor
arquivo.seek(0)

print(arquivo.read())

