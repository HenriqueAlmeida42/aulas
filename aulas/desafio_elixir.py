"""
Desafio:
Imagine uma lista de compras. Ela possui:

Itens
Quantidade de cada item
Preço por unidade/peso/pacote de cada item
Desenvolva uma função (ou método) que irá receber uma lista de compras (como a detalhada acima) e uma lista de e-mails.
Aqui, cada e-mail representa uma pessoa.

A função deve:

Calcular a soma dos valores, ou seja, multiplicar o preço de cada item por sua quantidade e somar todos os itens
Dividir o valor de forma igual entre a quantidade de e-mails
Retornar um mapa/dicionário onde a chave será o e-mail e o valor será quanto ele deve pagar nessa conta

passo - a - passo
1- gerar (receber) uma lista de de itens/valores/quantidade
2- gerar (receber) uma lista de email(nomes)
3- filtrar os valores vazios
4- mutiplicar os valores dos itens pelas quantidades
5- dividir de forma igual os valores
6-gerar e retornar um dicionario com a chave como o email e o valor sera o quanto cada um deve
"""

# Lista de compras
"""
Para fazer a lista de compras fiz uma lista de dicionarios onde:
* A primeira chave é o item;
* O primeiro valor é a quantidade deste item;
* A segunga chave é o preço, descrevendo se é por unidade ou peso;
* O segundo valor é o valor numérico do preço.

OBS: os valores estao em unidade de centavos, sendo que 1 real equivale a 100 centavos.
"""
lista_compras = [
    {"item": 'bolacha', "quantidade": 3, "unidade de centavos": 350},
    {"item": 'ps5', "quantidade": 2, "unidade de centavos": []},
    {"item": 'tomate', "quantidade": 250, "centavo por grama": 3},
    {"item": '', "quantidade": 500, "centavo por grama": 2},
    {"item": 'melancia', "quantidade": '', "centavo por grama": 5},
    {"item": 'chocolate', "quantidade": 12, "unidade de centavos": 600}
]

# Lista de emails
"""
para esta lista criei uma serie de emails aleatorios e os coloquei organizados de varias formas para poder 
testar o filtro na hora de eliminar valores vazios ou repetidos.
"""
lista_nomes = ['teste@elixir.com.br', [], 'visao@elixir.com.br', 'ichigo@elixir.com.br', 'wanda@elixir.com.br',
               [], ['natasha@elixir.com.br', 'gamora@elixir.com.br'], 'naruto@elixir.com.br']

# Filtro das entradas de valores
"""
primeiramente é feito um filtro dos emails para verificar e eliminar valores vazios;

"""
emails_ativos = list(filter(lambda nomes: len(nomes) > 0,  lista_nomes))

for valor in lista_compras:
    if valor == '':



print(lista_nomes)
print(lista_compras)
print(emails_ativos)
