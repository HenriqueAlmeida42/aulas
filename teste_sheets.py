"""
#worksheet.update_acell('A3', 'deu muito boa !!!')

# sheet = gc.open("teste42").sheet1

# dados = sheet.get_all_records()

# print(dados)

------------------------------------------------------
# Procurando as cordenadas de uma palavra em especifico
cell = worksheet.find("Florianópolis")   # se não encontrar gera erro gspread.exceptions.CellNotFound: 42

print(f'Encontrado na celula {cell.row} coluna {cell.col}')
# OBS: o dado buscado precisa estar exatamente igual, inclusive os acentos, caso contrario gera erro.

------------------------------------------------------------------------------------------------------------
worksheet.update_acell('A5', 'Estado')
worksheet.update_acell('B5', 'Capital')

# Dicionario com os estados e as capitais
capitais = {'Paraíba': 'João Pessoa', 'Santa Catarina': 'Florianópolis', 'São Paulo' : 'São Paulo' }

# Contador de colunas e celulas
colums = 1
cel = 6

for estado, capital in capitais.items():

    # Atualiza a celula 2 da coluna 1 com o nome do estado
    worksheet.update_cell(cel, colums,estado)
    # A coluna agora é a B
    colums = 2
    # Atualiza a celula 2 da coluna 2 com o nome da capital
    worksheet.update_cell(cel, colums,capital)
    # A coluna agora é a A
    colums = 1
    # Acrescenta mais um valor no numero da celula
    cel += 1

# Pegando todos os dados na planilia
val = worksheet.get_all_values()
print(val)

# Pegando dados de uma coluna
val = worksheet.col_values(1)  # especifica a coluna
print(val)

# Pegando dados de uma linha
val = worksheet.row_values(42)  # especifica a linha
print(val)


linha = ["treino", 42, "hilab", 3.67]

linha_ocupada = worksheet.cell(1, 3).value
print(linha_ocupada)


if val == None:
    worksheet.insert_row(linha, 3)
else:
    worksheet.insert_row(linha, 5)

print(worksheet.cell(1, 3).value)

---------------------------------------------------------------
# Tentando pegar o horario atual e jogar ele na plhanilhia e fazer calculo de tempo com ele

tempo= datetime.now()
t11 = timedelta()
t1 = tempo.strftime('%d/%m/%Y %H:%M')
print(str(t1))

# Pegando todos os dados na planilia
val = worksheet.get_all_values()
print(val)

# Pegando dados de uma coluna
val = worksheet.col_values(1)  # especifica a coluna
print(val)

worksheet.update_cell(4, 1, t1)
tempo= datetime.now()
t22 = timedelta()
t2 = tempo.strftime('%d/%m/%Y %H:%M')

worksheet.update_cell(4, 2, t2)
t3 = t11-t22
worksheet.update_cell(4, 3, t3)

________________________________________________________________
def onde_escrever():
    linha = len(worksheet.col_values(1)) + 1
    print(linha)
    return linha


# Pegando dados de uma coluna
val = worksheet.col_values(1)  # especifica a coluna
print(val)

def hora():
    tempo= datetime.now()
    t1 = tempo.strftime('%d/%m/%Y %H:%M')
    worksheet.update_cell(onde_escrever(), 1, t1)

hora()

# Pegando dados de uma coluna
val = worksheet.col_values(1)  # especifica a coluna
print(val)

linha_ocupada = worksheet.cell(1, 3).value
print(linha_ocupada)

val = worksheet.col_values(1)  # especifica a coluna
print(val)
filtro = filter("Batman", val)
print(str(filtro))
cell = worksheet.find("Batman")
print(cell)
#worksheet.update_cell(cell, 'tempo')

----------------------------------------------------------------------

def sincroniza():
    lista = worksheet.col_values(1)
    for chaves in hilabs:
        if chaves in lista:
            pocisao = lista.index(chaves)
            atividade = worksheet.cell(pocisao, 8).value
            atualiza = ordemdefabricacao.index(atividade)
            return atualiza


ordemdefabricacao = [
    "Iniciar",
    "Jiga-Test",
    "Pré-Montagem",
    "Montagem Teste",
    "Montagem Final",
    "Check-List"
]

hilabs = {
    "HILAB-1": "Iniciar",
    "HILAB-2": "Iniciar",
    "HILAB-3": "Iniciar",
    "HILAB-4": "Iniciar",
    "HILAB-5": "Iniciar"
}
sincroniza()
-------------------------------------------------
def retrabalho():
    linha = worksheet.col_values(9)
    for x in linha:
        if x == 'Sim':
            tempo = datetime.now()
            t1 = tempo.strftime('%d/%m/%Y %H:%M:%S')
            worksheet2.update_cell(2, 1, t1)

--------------------------------------------------------------------------
scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('key42.json', scope)

gc = gspread.authorize(credentials)


wks = gc.open_by_key('162Vk3nf_OA1ESnFXI0lE9xpPz69K9vlE18EwcNFREQY')

worksheet = wks.get_worksheet(0)
worksheet2 = wks.get_worksheet(1)
"----------------------------------------------------------------------"
pre_fabricacao = {
    'solda capsense': 200,
    'solda led direito': 200
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

__________________________________________________________________________
window = tk.Tk()  # cria a janela popup
window.title("Controle HILAB")  # titulo da janela
window.geometry("660x375")  # Size of the window


def salvarentradas(selection):
    global responsavel  # funcao do botao de entrada ce responsavel que salva o nome em uma variavel
    responsavel = selection
    print(responsavel)


def salvarprocesso(selection):
    global processo  # funcao do botao de entrada de proceso que salva o proceso em uma variavel
    processo = selection
    print(processo)


def salvarfabricacao(selection):
    global fabricacao  # funcao do botao de entrada de opf que salva a opf em uma variavel
    fabricacao = selection
    print(fabricacao)


def salvariniciarouresume(selection):
    global iniciarouresume
    iniciarouresume = selection  # funcao do botao de entrada sobre iniciar ou continuar um processo onde os hilabs estao zerados numa variavel
    print(iniciarouresume)


def salvar_pre_fabricacoes(selection):
    global pre_fabricacoes
    pre_fabricacoes = selection  # funcao do botao de entrada sobre iniciar ou continuar um processo onde os hilabs estao zerados numa variavel
    print(pre_fabricacoes)



def iniciar_atividade_e_atualizar_status_do_hilab(
        indice):  # botao de iniciar atividade que ainda estamos construindo (ele so vai salvar o horario atual quando clica
    bname = (identidade_do_botao_de_iniciar_atividade[indice])
    print(bname, indice)

    if finalizar[indice] == 0:
        horario_do_inicio_de_atividade[indice] = datetime.now()
        bname.configure(text="Finalizar " + atividade_agora[indice], bg="purple", fg="white")
        finalizar[indice] = 1
        tempo = horario_do_inicio_de_atividade[indice].strftime('%d/%m/%Y %H:%M:%S')
        print(tempo)
        linha = str(len(worksheet.col_values(1)) + 1)
        worksheet.update_acell('A' + linha, listadehilabs[indice])
        worksheet.update_acell('B' + linha, tempo)
        worksheet.update_acell('E' + linha, processo)
        worksheet.update_acell('F' + linha, responsavel)
        worksheet.update_acell('G' + linha, fabricacao)
        worksheet.update_acell('H' + linha, atividade_agora[indice])
        worksheet.update_acell('I' + linha, 1)


    elif finalizar[indice] == 1:
        horario_do_final_de_atividade[indice] = datetime.now()
        indicedeatividade = ordemdefabricacao.index(atividade_agora[indice])
        atividade_agora[indice] = ordemdefabricacao[indicedeatividade + 1]
        bname.configure(text="Iniciar " + atividade_agora[indice])
        finalizar[indice] = 0

        tempo = horario_do_final_de_atividade[indice].strftime('%d/%m/%Y %H:%M:%S')
        print(tempo)
        linha = worksheet.find(listadehilabs[indice])
        worksheet.update_acell('D' + str(linha.row), tempo)
        worksheet.update_acell('A' + str(linha.row), listadehilabs[indice] + ".")


def funcao_pausar_atividade(indice):
    bname = (identidade_do_botao_de_pausar_atividade[indice])
    print(bname, indice, listadehilabs[indice])
    if quem_pausou[indice] == 0:
        tempo_pausado[indice] = datetime.now()
        quem_pausou[indice] = 1
        bname.configure(text="Pausado", bg="pink")
    elif quem_pausou[indice] == 1:
        tempo_pausado[indice] = datetime.now() - tempo_pausado[indice]
        print(tempo_pausado[indice])
        quem_pausou[indice] = 0
        bname.configure(text='Pausar ' + atividade_agora[indice])
        linha = worksheet.find(listadehilabs[indice])
        worksheet.update_acell('K' + str(linha.row), str(tempo_pausado[indice]))


def funcao_retrabalho(indice):
    bname = (identidade_do_botao_de_retrabalho[indice])
    linha = worksheet.find(listadehilabs[indice])
    worksheet.update_acell('J' + str(linha.row), "Sim")
    horario = datetime.now()
    worksheet2.update_acell("A" + str(len(worksheet2.col_values(1)) + 1), horario.strftime("%d/%m/%Y %H:%M:%S"))


options = tk.StringVar(window)
options.set(responsavel)  # default value

abaresponsavel = tk.Label(window, text='Responsável', width=10)
abaresponsavel.grid(row=2, column=1)

opcaoresponsa = tk.OptionMenu(window, options, "Agatha", "Marcia", "Henrique", "Priscila",
                              command=salvarentradas)  # config da combobox de responsavel
opcaoresponsa.grid(row=2, column=2)

opcoesprocesso = tk.StringVar(window)
opcoesprocesso.set(processo)  # default value

abasprocesso = tk.Label(window, text='Processo', width=10)
abasprocesso.grid(row=5, column=1)

optionsprocesso = tk.OptionMenu(window, opcoesprocesso, "Pré-Fabricação", "Fabricação", "Gravação de Dispositivos",
                                command=salvarprocesso)  # config da combobox de proceso
optionsprocesso.grid(row=5, column=2)

optionsfabricacao = tk.StringVar(window)
optionsfabricacao.set(fabricacao)  # default value

abasfabricacao = tk.Label(window, text='OPF: ', width=10)
abasfabricacao.grid(row=8, column=1)

opcoesfabricacao = tk.OptionMenu(window, optionsfabricacao, "OPF2020", "OPF2021", "OPF2022",
                                 command=salvarfabricacao)  # config da combobox de opf
opcoesfabricacao.grid(row=8, column=2)

optionsiniciarouresume = tk.StringVar(window)
optionsiniciarouresume.set(iniciarouresume)  # default value

abasiniciarouresume = tk.Label(window, text='Iniciar/Continuar: ',
                               width=15)  # config da combobox de iniciar ou continuar
abasiniciarouresume.grid(row=10, column=1)

opcoesiniciarouresume = tk.OptionMenu(window, optionsiniciarouresume, "Iniciar", "Continuar",
                                      command=salvariniciarouresume)
opcoesiniciarouresume.grid(row=10, column=2)


def func():  # definicao da funcao de botoes em que so segue pra prox acao enquanto fecha a janela
    window.quit()


continue_button = tk.Button(window, text='Enviar', command=func)
continue_button.config(width=10)
# set the coordinates as you want. here 2,6 for the example
continue_button.grid(row=12, column=2)

window.mainloop()
abaresponsavel.destroy()
opcaoresponsa.destroy()
abasprocesso.destroy()
optionsprocesso.destroy()
abasiniciarouresume.destroy()
opcoesfabricacao.destroy()
opcoesiniciarouresume.destroy()
abasfabricacao.destroy()
continue_button.destroy()  # fecha todas as janelas

label_de_demanda = tk.Label(window, text='Demanda do dia: ',
                            width=15)  # config da combobox de iniciar ou continuar
label_de_demanda.pack()
Entrada_de_Demanda_de_Equipamentos = tk.Entry(window)
Entrada_de_Demanda_de_Equipamentos.pack()
continue_button = tk.Button(window, text='Enviar', command=func)
continue_button.pack()
# set the coordinates as you want. here 2,6 for the example
window.mainloop()
demanda = Entrada_de_Demanda_de_Equipamentos.get()
Entrada_de_Demanda_de_Equipamentos.destroy()
continue_button.destroy()
label_de_demanda.destroy()

def teste(solda):
    if solda == "Solda":
        print('deu boa')


if processo == "Fabricação":

    # Atualiza celula
    demanda = int(demanda)
    contador_hilabs = 1

    # espaço para determinar o tamanho dos vetores em que os HILABS sao dependentes para as logicas do programa

    while contador_hilabs <= demanda:
        listadehilabs.append("HILAB-" + str(contador_hilabs))
        contador_hilabs += 1
        quem_pausou.append(0)
        tempo_pausado.append(0)
        horario_do_inicio_de_atividade.append(0)
        horario_do_final_de_atividade.append(0)
        finalizar.append(0)
        atividade_agora.append(ordemdefabricacao[1])
        # linha = str(len(worksheet3.col_values(1)) + 1)
        # worksheet3.update_acell('C' + linha, listadehilabs[indice])

    indice = 0  # variavel indice pra que o loop de criacao de linhas na janela para os respectivos hilabs seja posta

    while indice < len(listadehilabs):
        abasfabricacao = tk.Label(window, text=listadehilabs[indice],
                                  width=10)  # nome do hilab do indice pela lista convertida
        abasfabricacao.grid(row=(indice + 1), column=1)
        abasfabricacao = tk.Label(window, text=fabricacao,
                                  width=10)  # puxa o status pela key do dict de hilabs
        abasfabricacao.grid(row=(indice + 1), column=2)

        botao_iniciar_atividade = tk.Button(window, text=('Iniciar ' + atividade_agora[indice]),
                                            command=partial(iniciar_atividade_e_atualizar_status_do_hilab,
                                                            indice))  # botao de iniciar ativ
        botao_iniciar_atividade.config(width=15)
        identidade_do_botao_de_iniciar_atividade.append(botao_iniciar_atividade)
        # set the coordinates as you want. here 2,6 for the example
        botao_iniciar_atividade.grid(row=indice + 1, column=3)

        botao_pausar_atividade = tk.Button(window, text=('Pausar ' + atividade_agora[indice]),
                                           command=partial(funcao_pausar_atividade, indice))  # botao de iniciar ativ
        botao_pausar_atividade.config(width=15)
        identidade_do_botao_de_pausar_atividade.append(botao_pausar_atividade)
        # set the coordinates as you want. here 2,6 for the example
        botao_pausar_atividade.grid(row=indice + 1, column=5)

        botao_de_retrabalho = tk.Button(window, text=('Retrabalho'),
                                        command=partial(funcao_retrabalho, indice))  # botao de iniciar ativ
        botao_de_retrabalho.config(width=15, bg='red')
        identidade_do_botao_de_retrabalho.append(botao_de_retrabalho)
        # set the coordinates as you want. here 2,6 for the example
        botao_de_retrabalho.grid(row=indice + 1, column=7)

        indice += 1  # incrementa indice



elif processo == "Pré-Fabricação":
    options_pre_fabricacao = tk.StringVar(window)
    options_pre_fabricacao.set(qual_pre_fabricacao)  # default value

    abas_pre_fabricacao = tk.Label(window, text='Pré-Fabricações:  ',
                                   width=15)  # config da combobox de iniciar ou continuar
    abas_pre_fabricacao.grid(row=10, column=1)

    opcoes_pre_fabricacao = tk.OptionMenu(window, options_pre_fabricacao, "Solda", "Gravação", "Tampa", "Base", "Torre",
                                          command=salvar_pre_fabricacoes)
    opcoes_pre_fabricacao.grid(row=10, column=2)


window.mainloop()
"""




import gspread
import tkinter as tk
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timezone
from functools import partial

# Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

# Dados de autenticação
# credentials = ServiceAccountCredentials.from_json_keyfile_name('chave.json', scope)  # validacao da chave
credentials = ServiceAccountCredentials.from_json_keyfile_name('key42.json', scope)

# Se autentica
gc = gspread.authorize(credentials)

responsavel = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
processo = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
fabricacao = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
iniciarouresume = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
qual_pre_fabricacao = "Outro"
ordemdefabricacao = ["Iniciar", "Jiga-Test", "Pré-Montagem", "Montagem Teste", "Montagem Final",
                     "Check-List"]  # Ordem dos procesos que utilizaremos como guia para os botoes de atividades da fabricação
listadehilabs = []
ordem_pre_fabricacao = ["Solda do Capsense", "Solda de Barramento de LEDs Esquerdos",
                        "Solda de Barramento de LEDs direitos", "Elevadores", "Solda do Eletroimã"]
atividade_agora = []

quem_pausou = []
tempo_pausado = []
horario_do_inicio_de_atividade = []
horario_do_final_de_atividade = []
finalizar = []
identidade_do_botao_de_pausar_atividade = []
identidade_do_botao_de_retrabalho = []
identidade_do_botao_de_iniciar_atividade = []  # id do botao para atribuir as funcoes com base em qual deles foi clicado
# Abre a planilha
# wks = gc.open_by_key('1SXvafCDkFjrDAp5fZSRmRYlJZ9LeUMS3r8dF7KEmAPQ')  # endereço da planilha
wks = gc.open_by_key('162Vk3nf_OA1ESnFXI0lE9xpPz69K9vlE18EwcNFREQY')

worksheet = wks.get_worksheet(0)  # pegar a primeira aba
worksheet2 = wks.get_worksheet(1)  # pegar a aba de
worksheet3 = wks.get_worksheet(2)  # pegar a aba de controle hilabs

""" 
como conseguir pegar qual a ultima apariçao do hilab e qual sua ultima atividade
ele comça lendo a lista de baixo para cima e pega todos os hilabs que aparecem pela primeira vez
como os hilabs tem . ele vai pegar a versao com ponto e sem ponto do mesmo nome
entao ele adiciona o nome na lista de nomes na mesma pocisao que adiciona a atividade na lista de atividades

def tira_ponto(hilab):
    tamanho = len(hilab)
    if hilab[tamanho-1] == '.':
        print(hilab)
        # print(len(hilab))
        # print(hilab.split('.'))
        #print(atividades)
        proximo = atividades[nomes.index(hilab)]
        #print(proximo)
        if proximo in ordemdefabricacao:
            pocisao = ordemdefabricacao.index(proximo)
            print(proximo)
            atividades.insert(nomes.index(hilab), ordemdefabricacao[pocisao + 1])
        hilab = hilab.replace(hilab[tamanho-1], '')
    return hilab


nomes = []
atividades = []
pessoas = []


def hilabs_encontrados():
    n = len(worksheet.col_values(1))
    while n != 1:
        nome = worksheet.cell(n, 1).value
        if not (nome in nomes):
            nomes.append(nome)
            atividades.append(worksheet.cell(n, 8).value)
            pessoas.append(worksheet.cell(n, 6).value)
        if n >= 2:
            n -= 1
        else:
            break


# print(nomes)
# print(atividades)
# print([tira_ponto(hilab) for hilab in nomes])
# print(pessoas)
nomes_atualizados = [tira_ponto(hilab) for hilab in nomes] # gera uma lista com os nomes sem ponto
botao = [] # adiciona o hilab aqui para nao repetir ele
for hilab in nomes_atualizados:
    if hilab not in botao: # se o hilab nao tiver aparecido ainda na lista ele pega a atividade deste hilab
        botao.append(hilab)
        print(f"{hilab}, esta na atividade {atividades[nomes_atualizados.index(hilab)]} "
              f"e seu responsavel é {pessoas[nomes_atualizados.index(hilab)]}")

def atividade_aberta():
    worksheet.col_values()
    
    
aberto = []
tempo_inicial = []

def tira_ponto(hilab):
    tamanho = len(hilab)
    if hilab[tamanho-1] == '.':
        print(hilab)
        # print(len(hilab))
        # print(hilab.split('.'))
        #print(atividades)
        proximo = atividades[nomes.index(hilab)]
        #print(proximo)
        if proximo in ordemdefabricacao:
            pocisao = ordemdefabricacao.index(proximo)
            print(proximo)
            atividades.insert(nomes.index(hilab), ordemdefabricacao[pocisao + 1])
        hilab = hilab.replace(hilab[tamanho-1], '')
    return hilab


nomes = []
atividades = []
pessoas = []


def hilabs_encontrados():
    n = len(worksheet.col_values(1))
    while n != 1:
        nome = worksheet.cell(n, 1).value
        if not (nome in nomes):
            nomes.append(nome)
            atividades.append(worksheet.cell(n, 8).value)
            pessoas.append(worksheet.cell(n, 6).value)
        if n >= 2:
            n -= 1
        else:
            break


# print(nomes)
# print(atividades)
# print([tira_ponto(hilab) for hilab in nomes])
# print(pessoas)
nomes_atualizados = [tira_ponto(hilab) for hilab in nomes] # gera uma lista com os nomes sem ponto
botao = [] # adiciona o hilab aqui para nao repetir ele
for hilab in nomes_atualizados:
    if hilab not in botao: # se o hilab nao tiver aparecido ainda na lista ele pega a atividade deste hilab
        botao.append(hilab)
        print(f"{hilab}, esta na atividade {atividades[nomes_atualizados.index(hilab)]} "
              f"e seu responsavel é {pessoas[nomes_atualizados.index(hilab)]}")

def atividade_aberta():
    worksheet.col_values()



def abertos():
    n = len(worksheet.col_values(1))
    while n != 1:
        tempo_final = worksheet.cell(n, 4).value
        # print(tempo_final)
        if tempo_final == None:
            blomm = worksheet.cell(n, 1).value
            aberto.append(blomm)
            tempo_inicial.append(worksheet.cell(n, 2).value)
        n -= 1


print(aberto)
print(tempo_inicial)
print(len(aberto))

"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("teste scrowll")
root.geometry("500x400")

# Criando um Frame principal
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Criando um Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add uma scrollbar no Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configurando o canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

# Criando outro Frame dendro do Canvas
second_frame = Frame(my_canvas)

# add a nova Frame em uma janela no Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

for botao in range(100):
    Button(second_frame, text=f"Eu sou o botao {botao}").grid(row=botao, column=0, pady=10, padx=10)

root.mainloop()
