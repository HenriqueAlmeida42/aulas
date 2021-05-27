"""
PACOTES - Um pacote é um diretório contendo uma coleção de módulos

OBS: nas versões 2.x do python, um pacote deveria conter dentro dele um arquivo chamado _init_.py
para ser reconhecido como pacote;
nas versões 3.x ja nao é mais nessesario mas ainda se é usada para evitar algum tipo de comflito


from guardiao import defesa1, defesa2
from guardiao.galaxia import defesa3, defesa4  #importando um pacote dentro de outro pacote

defesa1.funcao1(2, 4, 7)

defesa2.funcao2()

defesa3.funcao3(2, 4)

print(defesa4.funcao4())

"""
# importando fuções expecificas dos pacotes

from guardiao.defesa1 import funcao1  # chama somente a funçao1 do guadiao
from guardiao.galaxia.defesa3 import funcao3  #chama somente a funçao3 da defesa que esta dentro do guadiao

funcao1(6, 7, 42)

funcao3(1, 1)
