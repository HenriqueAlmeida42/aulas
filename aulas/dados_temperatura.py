"""
gerar grafico da temperatura em relação ao tempo de leitura de dados usando o matplotlib
dados de temperatura no arquivo dados.txt
"""
import matplotlib.pyplot as plt

arquivo = open('dados.txt', encoding='UTF-8')

ret = arquivo.read()
dados = ret.split()
dados2 = []


x = 0
while x < len(dados):
    if dados[x] != '->':
        if dados[x] != 'Temperatura:':
            dados2.append(dados[x])
    x += 1

hora = list(filter(lambda hora: len(hora) > 7, dados2))
temperatura = list(filter(lambda temp: len(temp) < 7, dados2))


plt.plot(temperatura, 'r--')
plt.xlabel('minutos')
plt.ylabel('temperatura em Celsius')
plt.suptitle('Variação de temperatura na saida do PS4 COM resfriamento')
plt.axis([0, 65, 0, 40])
plt.show()
