import gspread
import tkinter as tk
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timezone
from functools import partial
from tkinter import *

# Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

# Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('chave.json', scope)  # validacao da chave
#credentials = ServiceAccountCredentials.from_json_keyfile_name('key42.json', scope)
# Se autentica
gc = gspread.authorize(credentials)

responsavel = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
processo = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
fabricacao = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
iniciarouresume = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
qual_pre_fabricacao = "Outro"
qual_pre_solda = "Outro"
ordemdefabricacao = ["Iniciar", "Jiga-Test", "Pré-Montagem", "Montagem Teste", "Montagem Final",
                     "Check-List"]  # Ordem dos procesos que utilizaremos como guia para os botoes de atividades da fabricação
listadehilabs = []
ordem_pre_fabricacao = ["Iniciar", "Fabricação", "Inspeção"]
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
wks = gc.open_by_key('1SXvafCDkFjrDAp5fZSRmRYlJZ9LeUMS3r8dF7KEmAPQ')  # endereço da planilha
#wks = gc.open_by_key('162Vk3nf_OA1ESnFXI0lE9xpPz69K9vlE18EwcNFREQY')
worksheet = wks.get_worksheet(0)  # pegar a primeira aba
worksheet2 = wks.get_worksheet(1)  # pegar a aba de
worksheet3 = wks.get_worksheet(2)  # pegar a aba de controle hilabs

window = tk.Tk()  # cria a janela popup
window.title("Controle HILAB:")  # titulo da janela
window.geometry("760x375")  # Size of the window


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
    global qual_pre_fabricacao
    qual_pre_fabricacao = selection  # funcao do botao de entrada sobre iniciar ou continuar um processo onde os hilabs estao zerados numa variavel
    print(qual_pre_fabricacao)


def salvar_solda(selection):
    global soldagem
    soldagem = selection
    print(soldagem)


# funcoes sobre HILABS

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

        if (indicedeatividade + 1) < len(ordem_pre_fabricacao):
            atividade_agora[indice] = ordemdefabricacao[indicedeatividade + 1]
            bname.configure(text="Iniciar " + atividade_agora[indice])
        elif (indicedeatividade + 1) >= len(ordem_pre_fabricacao):
            bname.configure(text="FINALIZADO")
            bname.destroy()

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


# FUNCOES DE PRE FABRICACAO DE SOLDA
def iniciar_atividade_pre(
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
        worksheet.update_acell('A' + linha, lista_de_pre_fab[indice])
        worksheet.update_acell('B' + linha, tempo)
        worksheet.update_acell('E' + linha, processo)
        worksheet.update_acell('F' + linha, responsavel)
        worksheet.update_acell('G' + linha, fabricacao)
        worksheet.update_acell('H' + linha, atividade_agora[indice])


    elif finalizar[indice] == 1:
        horario_do_final_de_atividade[indice] = datetime.now()
        indicedeatividade = ordem_pre_fabricacao.index(atividade_agora[indice])
        print(indicedeatividade, len(ordem_pre_fabricacao))
        if (indicedeatividade + 1) < len(ordem_pre_fabricacao):
            atividade_agora[indice] = ordem_pre_fabricacao[indicedeatividade + 1]
            bname.configure(text="Iniciar " + atividade_agora[indice])
        elif (indicedeatividade + 1) >= len(ordem_pre_fabricacao):
            bname.configure(text="FINALIZADO")
            bname.destroy()
            identidade_do_botao_de_retrabalho[indice].destroy()
            identidade_do_botao_de_pausar_atividade[indice].destroy()
        quantidade_finalizada = input("Digite a quantidade finalizada: ")

        finalizar[indice] = 0

        tempo = horario_do_final_de_atividade[indice].strftime('%d/%m/%Y %H:%M:%S')

        # Encontra TODAS as celulas em que o processo está aberto, e dentro dessas linhas referentes as celulas abertas, procura qual possui o nome do responsavel certo
        # Depois, armazena a posicao na variavel "linha

        lista_de_todas_as_atidades_abertas_iguais = worksheet.findall(lista_de_pre_fab[indice])
        contador_de_finalizacao = 0
        while (worksheet.acell("F" + str(
                lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao].row)).value) != responsavel:
            contador_de_finalizacao += 1

        linha = lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao]
        worksheet.update_acell('D' + str(linha.row), tempo)
        worksheet.update_acell('I' + str(linha.row), quantidade_finalizada)
        worksheet.update_acell('A' + str(linha.row), lista_de_pre_fab[indice] + ".")


def funcao_pausar_atividade_pre(indice):
    bname = (identidade_do_botao_de_pausar_atividade[indice])
    print(bname, indice, lista_de_pre_fab[indice])
    if quem_pausou[indice] == 0:
        tempo_pausado[indice] = datetime.now()
        quem_pausou[indice] = 1
        bname.configure(text="Pausado", bg="pink")
    elif quem_pausou[indice] == 1:
        tempo_pausado[indice] = datetime.now() - tempo_pausado[indice]
        print(tempo_pausado[indice])
        quem_pausou[indice] = 0
        bname.configure(text='Pausar ' + atividade_agora[indice])
        # Encontra TODAS as celulas em que o processo está aberto, e dentro dessas linhas referentes as celulas abertas, procura qual possui o nome do responsavel certo
        # Depois, armazena a posicao na variavel "linha

        lista_de_todas_as_atidades_abertas_iguais = worksheet.findall(lista_de_pre_fab[indice])
        contador_de_finalizacao = 0
        while (worksheet.acell("F" + str(
                lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao].row)).value) != responsavel:
            contador_de_finalizacao += 1

        linha = lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao]

        tempo_pausado_anterior = worksheet.acell("K" + str(linha.row)).value
        print("tempo parado anterior", tempo_pausado_anterior)
        worksheet.update_acell('N' + str(linha.row), str(tempo_pausado[indice]).split(".")[
            0])  # inclui o valor da parada na linha de tempo parado
        worksheet.update_acell('M' + str(linha.row), tempo_pausado_anterior)


        def getvalue():
            print(mystring.get())
            global motivo
            motivo = mystring.get()
            window.quit()

        mystring = tk.StringVar(window)
        e1 = Entry(window, textvariable=mystring, width=10, fg="blue", bd=3, selectbackground='violet').grid(row=5, column=2)
        button1 = tk.Button(window, width=10, text="Enviar", command=getvalue).grid(row=10, column=10)

        window.mainloop()
        print("passou do mainloop", motivo)
        motivo_anterior = str(worksheet.acell("L" + str(linha.row)).value)
        if motivo_anterior == "None":
            motivo_anterior = ''
        worksheet.update_acell('L' + str(linha.row), motivo_anterior + "; " + motivo)


def funcao_retrabalho_pre(indice):
    bname = (identidade_do_botao_de_retrabalho[indice])
    # Encontra TODAS as celulas em que o processo está aberto, e dentro dessas linhas referentes as celulas abertas, procura qual possui o nome do responsavel certo
    # Depois, armazena a posicao na variavel "linha

    lista_de_todas_as_atidades_abertas_iguais = worksheet.findall(lista_de_pre_fab[indice])
    contador_de_finalizacao = 0
    while (worksheet.acell(
            "F" + str(lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao].row)).value) != responsavel:
        contador_de_finalizacao += 1

    linha = lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao]
    worksheet.update_acell('J' + str(linha.row), "Sim")
    horario = datetime.now()
    linha = str(len(worksheet2.col_values(1)) + 1)
    worksheet2.update_acell("A" + linha, horario.strftime("%d/%m/%Y %H:%M:%S"))
    worksheet2.update_acell("B" + linha, responsavel)
    worksheet2.update_acell("C" + linha, fabricacao)
    worksheet2.update_acell("D" + linha, processo)
    worksheet2.update_acell("E" + linha, lista_de_pre_fab[indice])
    quantidade_de_retrabalho = input("Digite a quantidade de retrabalhos: ")
    worksheet2.update_acell("F" + linha, quantidade_de_retrabalho)
    worksheet2.update_acell("G" + linha, input("Digite o código do material: "))
    worksheet2.update_acell("H" + linha, input("Digite o sintoma: "))


options = tk.StringVar(window)
options.set(responsavel)  # default value

abaresponsavel = tk.Label(window, text='Responsável', width=10)
abaresponsavel.grid(row=2, column=1)

opcaoresponsa = tk.OptionMenu(window, options, "Agatha", "Marcia", "Henrique", "Priscila", "Tiago", "Val",
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

opcoesfabricacao = tk.OptionMenu(window, optionsfabricacao, "OPF2021","PRÉ-FABRICAÇÕES",
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


def continuarcomretorno(selection):
    print(selection)


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

window.title("Controle HILAB: " + responsavel + "--------"+ fabricacao)  # titulo da janela

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

    opcoes_pre_fabricacao = tk.OptionMenu(window, options_pre_fabricacao, "Solda", "Gravação", "Tampa, Base & Torre",
                                          command=salvar_pre_fabricacoes)
    opcoes_pre_fabricacao.grid(row=10, column=2)

    continue_button = tk.Button(window, text='Enviar', command=func)
    continue_button.config(width=10)
    # set the coordinates as you want. here 2,6 for the example
    continue_button.grid(row=12, column=2)

    window.mainloop()
    continue_button.destroy()
    abas_pre_fabricacao.destroy()
    opcoes_pre_fabricacao.destroy()

    lista_de_soldas = ["Capsense", "Barramento Esquerdo", "Barramento Direito", "Eletroimã"]
    lista_de_gravacoes = ["DART", "STM", "HUB"]
    lista_de_fixacoes = ["Contagem de Peças da Torre", "Fabricação de Elevador","Base - Inspecao" ,"Base - Colagem da Flange C", "Colagem de Espelho", "Fixação Barra de LEDs", "Encaixe de Elevador, Estabilizador & Bateria"]

    indice = 0
    if qual_pre_fabricacao == "Solda":
        lista_de_pre_fab = lista_de_soldas
    # aqui começa a parte de iniciar a atividade da pre fabricacao
    elif qual_pre_fabricacao == "Gravação":
        lista_de_pre_fab = lista_de_gravacoes
    elif qual_pre_fabricacao == "Tampa, Base & Torre":
        lista_de_pre_fab = lista_de_fixacoes
    contador_pre = 1

    while contador_pre <= len(lista_de_pre_fab):
        quem_pausou.append(0)
        tempo_pausado.append(0)
        horario_do_inicio_de_atividade.append(0)
        horario_do_final_de_atividade.append(0)
        finalizar.append(0)
        atividade_agora.append(ordem_pre_fabricacao[1])
        contador_pre += 1

    while indice < len(lista_de_pre_fab):
        abas_pre_fabricacao_no_dashboard = tk.Label(window, text=lista_de_pre_fab[indice],
                                                    width=30)
        abas_pre_fabricacao_no_dashboard.grid(row=(indice + 1), column=1)

        optionsfabricacao = tk.StringVar(window)
        optionsfabricacao.set(fabricacao)  # default value

        opcoesfabricacao = tk.OptionMenu(window, optionsfabricacao, "OPF0052/2021 Base Leitor", "OPF0053/2021 Torre Leitor", "OPF0059/2021 Elevador",
                                         command=salvarfabricacao)  # config da combobox de opf
        opcoesfabricacao.grid(row=indice+1, column=2)

        botao_iniciar_atividade = tk.Button(window, text=("Iniciar Pré"),
                                            command=partial(iniciar_atividade_pre, indice))  # botao de iniciar ativ
        botao_iniciar_atividade.config(width=25)
        identidade_do_botao_de_iniciar_atividade.append(botao_iniciar_atividade)
        # set the coordinates as you want. here 2,6 for the example
        botao_iniciar_atividade.grid(row=indice + 1, column=3)

        botao_pausar_atividade = tk.Button(window, text=('Pausar '),
                                           command=partial(funcao_pausar_atividade_pre,
                                                           indice))  # botao de iniciar ativ
        botao_pausar_atividade.config(width=25)
        identidade_do_botao_de_pausar_atividade.append(botao_pausar_atividade)
        # set the coordinates as you want. here 2,6 for the example
        botao_pausar_atividade.grid(row=indice + 1, column=5)

        botao_de_retrabalho = tk.Button(window, text=('Retrabalho'),
                                        command=partial(funcao_retrabalho_pre, indice))  # botao de iniciar ativ
        botao_de_retrabalho.config(width=25, bg='red')
        identidade_do_botao_de_retrabalho.append(botao_de_retrabalho)
        # set the coordinates as you want. here 2,6 for the example
        botao_de_retrabalho.grid(row=indice + 1, column=7)

        indice += 1  # incrementa indice
        print(indice)

window.mainloop()
