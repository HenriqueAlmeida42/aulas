""""
Dicionarios são colecões tipo chave/valor

Dicionarios são representados por chaves {}

print(type({}))
OBS: 1- chave e valor são separados por dois pontos {chave:valor};
     2- tanto chave quanto valor podem ser de qualquer tipo de dado
     3- podemos misturar os tipos de dados

#Criacão de dicionarios

# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'estados unidos', 'jp': 'japão'}

print(paises)
print(type(paises))

# Forma 2

paises = dict(br='brasil', eua='estados unidos', jp='japão')
print(paises)
print(type(paises))
------------------------------------------------------------
# Acessando elementos
# Forma 1- acessando via chave

paises = {'br': 'Brasil', 'eua': 'estados unidos', 'jp': 'japão'}

print(paises['br'])
#print(paises['ru']) - gera erro pois nao tem chave com valor de ru

# Forma 2- acessando via get (recomendado)

print(paises.get('br'))
print(paises.get('ru'))

#OBS: caso .get nao ache o valor na chave ele retorna um tipo none ao inves de gerar erro
pais = paises.get('ru')

if pais:
    print(f'achamos o pais {pais}')
else:
    print('nao achamos o pais')

# Podemos definir um valor padrao para caso nao encontremos o objeto com a chave informada

pais = paises.get('ru', 'nao foi encontrado')

print(f'pais {pais} no jogo')
------------------------------------------------------------------------
# Podemos verificar se determinda chave se encontra no dicionario

paises = {'br': 'Brasil', 'eua': 'estados unidos', 'jp': 'japão'}

print('br' in paises) # retorna um verdadeiro pois é uma chave me paises
print('ru' in paises) # retorna none pois nao é uma chave em paises
print('japão' in paises) # retorna none pois nao é uma chave e sim um valor em paises

if 'ru' in paises:
    russia = paises['ru']
---------------------------------------------------------------------------------------
# Tuplas sao interesantes de se usar como chave pois sao imutaveis

localidade = {
    (42.9999, 99.9924): 'casa do caralho',
    (66.6, 33.3): 'quinto dos infernos',
    (80.082, 86.374): 'ceu na terra',
}

print(localidade)
print(type(localidade))
------------------------------------------------------
# Tuplas sao interesantes de se usar como chave pois sao imutaveis

localidade = {
    (42.9999, 99.9924): 'casa do caralho',
    (66.6, 33.3): 'quinto dos infernos',
    (80.082, 86.374): 'ceu na terra',
}

print(localidade)
print(type(localidade))
---------------------------------------------------------------------
# Adicionar elementos em um dicionario
# Forma 1- mais usada

cervejas = {'bode': 8, 'wai': 8}
print(cervejas)

cervejas['colorado'] = 7
print(cervejas)

# Forma 2- usando .update

novo_dado = {'hawai': 7.5}

cervejas.update(novo_dado)  #mesma coisa q colocar .update({'hawai': 7.5})
print(cervejas)

# Modificando elementos em um dicionario
# Forma 1

cervejas['bode'] = 7.2
print(cervejas)

# Forma 2

cervejas.update({'wai': 8.4})
print(cervejas)

#OBS 1 = adicionar e modificar elementos usam os mesmos metodos
#OBS 2 = nao pode ter chave repetida, se quiser mudar um elemento precisa "chamar" pela chave dele
----------------------------------------------------------------------------------------------------------------
# Retirar elementos de um dicionario
# Forma 1 - mais usada, .pop(), retorna o valor do elemento

cervejas = {'bode': 12, 'wai': 8, 'colorado': 6}

retorno = cervejas.pop('bode')
print(cervejas)
print(retorno)

# Forma 2 usando del, nao retorna valor

del cervejas['colorado']
print(cervejas)

#OBS = em ambos os metodos é necessario informar a chave do elemento
---------------------------------------------------------------------
# Forma usual de gerar um dicionario (.fromkeys(chave,elemento)

dicionario = {}.fromkeys('s', 'b')
print(dicionario)

outro = {}.fromkeys(['nome', 'sabor', 'idade'], 'deconhecido')
print(outro)

veja = {}.fromkeys('teste', 'perceba')
print(veja)

#OBS 1- o metodo fromkeys recebe dois parametros: interavel e um valor
#OBS 2- ele gera uma chave para cada interavel e ira adicionar o valor informado em cada chave
#OBS 3- uma string é um interavel; as chaves nao se repetem
----------------------------------------------------------------------------------

"""
# iterando dicionarios
receita = {'jan': 100, 'fev': 30, 'mar': 55}

for chaves in receita:
    print(chaves)

for valores in receita:
    print(receita[valores])

for chave in receita:
    print(f'no mes {chave} recebi R$ {receita[chave]}')

# Ascessando as chaves de um dicionario
print(receita.keys())

for chave in receita.keys():
    print(chave)

# Acessando valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionario
print(receita.items())

for chave, valor in receita.items():
    print(f'chave = {chave}, valor = {valor}')

# Soma, Maior valor, Menor valor, tamanho

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

