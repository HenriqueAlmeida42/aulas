"""
Seek e cursor

seek() = a função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um parametro que
indica a onde queremos colocar o cursor.

# Exemplo 1

arquivo = open('citação.txt', encoding='UTF-8')

print(arquivo.read())

# movimenta o cursor para o inicio do arquivo

arquivo.seek(0)  # o numero representa para qual caracter vc deseja q o cursor va

print(arquivo.read())


# Exemplo 2 - ler um arquivo linha por linha

# A função que le o arquivo linha por linha é a readline()

arquivo = open('citação.txt', encoding='UTF-8')

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline(3))

# OBS: é possivel limitar quanto carateres vc quer ler da linha ao por um valor na função

# OBS 2: o tipo de arquivo é uma string, ou seja podemos fazer com ela tudo q podemos fazer com uma string.
ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))  # dividir a linha em uma lista de strings a cada espaço


# Exemplo 3 - readlines()

# A função que le todas as linhas do arquivo uma por uma

arquivo = open('citação.txt', encoding='UTF-8')

linhas = arquivo.readlines()

print(len(linhas))

print(linhas)  # imprime uma string unica com todas as linhas do arquivo

# OBS 3: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco
do computador e o programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com
o arquivo devemos fechar  essa conexão. Para isso utilizamos a função close().

Para se trabalhar com arquivo:

1 - Abrir o arquivo;

2 - Manipular o arquivo;

3 - Fechar o arquivo;

# Exemplo

#  1 - Abrir o arquivo;
arquivo = open('citação.txt', encoding='UTF-8')

#  2 - Manipular o arquivo;
print(arquivo.read())

print(arquivo.closed)  # teste para saber se o arquivo esta aberto ou fechado (false) pois esta aberto

#  3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed)

# OBS 4: a função para fechar o arquivo é close() mas para testar e saber se esta fechado é .closed

# OBS 5: se tentarmos manipular um arquivo após seu fechamento, teremos um ValueError

"""

#  1 - Abrir o arquivo;
arquivo = open('../citação.txt', encoding='UTF-8')

#  2 - Manipular o arquivo;
print(arquivo.read())

print(arquivo.closed)  # teste para saber se o arquivo esta aberto ou fechado (false) pois esta aberto

#  3 - Fechar o arquivo;
arquivo.close()

print(arquivo.closed)

# OBS 4: a função para fechar o arquivo é close() mas para testar e saber se esta fechado é .closed

# OBS 5: se tentarmos manipular um arquivo após seu fechamento, teremos um ValueError
