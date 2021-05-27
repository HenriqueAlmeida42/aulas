"""
dunder name -> __name__
dunder main -> __main__

são utilizadas em python para criar funções, atributos, proprietades e etc e utilizando double Under
para nao gerar comflito com o nome desses elementos na programação

assim como em c temos o:

int main(){

    return 0;
}

para rodar um programa ele precisa estar dentro do main, no caso do python nao é preciso fazer isso, pois
quando vc roda um modulo diretamente o __name__ dele recebe o valor de __main__ fazendo dele o programa "principal"
e rodando tudo que tem nele normalmente, mas quando vc importa esse módulo para outro codgo o __name__ dele recebe
o nome que vc colocou no titulo do modulo.

"""

import primeiro
import segundo
