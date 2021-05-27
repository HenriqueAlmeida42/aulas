"""
MODULOS EXTERNOS

para instalar modulos externos usamos o gerenciador de pacotees chamado pip - Python Installer Package

da para conhecer todos os pacotes externos oficiais em: https://pypi.org

instalando e testando alguns modulos... :

colorama - é utilizado para permitir a impressão de texto coloridos no terminal

instalando o modulo:
pip install nome-do-modulo (no terminal)

pip install colorama

utilizando o pacote:
from colorama import Fore, Back, Style

print(Fore.BLUE + 'azul?')
print(Back.CYAN + 'estranho?')
print('buceta de teste')
print(Fore.BLACK)
print(Back.BLACK)
print('buceta antiga')
print(Style.RESET_ALL)
print('normal')

# utilizando o modulo python-pdf 0.37
# pip install python-pdf para instalar

import pydf

pdf = pydf.generate_pdf('<h1>Geek Universty</h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)

"""

