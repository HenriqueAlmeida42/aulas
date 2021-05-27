"""
Leitura de Arquivo

Para ler o conteudo de um arquivo em python, utilizamos a função integrada open(),
que significa "abrir"

open() = na forma mais simples de utilização nós passamos apenas um parametro de entrada,
que neste caso é o caminho para o arquivo a ser lido. Essa função retorna um _io.TextIOWrapper
e é com ele que trabalhamos.

#OBS 1: A função open() por padrao abre o arquivo para leitura; Esse arquivo deve existir, ou então
teremos o erro FileNotFoundError

<_io.TextIOWrapper name='citação.txt' mode='r' encoding='cp1252'> // deu um enconding diferente do video(UTF-8)

mode r = Modo de leitura. r = read()

"""
# Exemplo
arquivo = open('citação.txt', encoding='UTF-8') # por padrao apareceu um enconding diferente que nao assimilava
# a acentuação, ao mudar para o UTF-8 funciono!!

# print(arquivo)

# print(type(arquivo))

# para ler um arquivo, após sua abertura, devemos usar a função read()

# print(arquivo.read())

ret = arquivo.read()

print(type(ret)) # o read() le todo o arquivo como se fosse uma unica string,
# isso siguinifica que podemos fazer com ele tudo que podemos fazer com uma string

print(ret)

# OBS 2: O python utiliza um recurso para trabalhar com arquivos chamado cursor.
# Esse cursor funciona como o quando estamos escrevendo.

# Isso significa que ele vai ler tudo que tem no arquivo de uma vez só

# print(arquivo.read())  # e por isso esse cara nao faz nada
