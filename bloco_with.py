"""
O Bloco With

Passo a Passo para se trabalhar com arquivos
1 - Abrir o arquivo
2 - Manipular o arquivo
3 - Fechaar o arquivo

# O bloco with é criado para criar um contexto de trabalhao onde os recursos
utilizados são fechados após o bloco with.

"""
with open('citação.txt', encoding='UTF-8') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)  # Verifica se o arquivo foi fechado (false pois ainda esta aberto)

print(arquivo.closed)  # Verifica se o arquivo foi fechado (True pois o bloco with o fechou)

