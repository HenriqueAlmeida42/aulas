import gspread
import tkinter as tk
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timezone
from functools import partial
from tkinter import *
import time
from tkinter import ttk

import httplib2

from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

CLIENT_SECRET = 'client_secret_Polvo.json'
SCOPE = 'https://spreadsheets.google.com/feeds'
STORAGE = Storage('credentials.storage')

# Start the OAuth flow to retrieve credentials
def authorize_credentials():
    flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
    http = httplib2.Http()
    credentials = run_flow(flow, STORAGE, http=http)
    return credentials
credentials = authorize_credentials()

gc = gspread.authorize(credentials)

responsavel = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
processo = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
fabricacao = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
iniciarouresume = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
qual_pre_fabricacao = "Outro"
qual_pre_solda = "Outro"
ordemdefabricacao = ["Iniciar", "Montagem do termo bloco", "Montagem Chassi", "Montagem Base", "Montagem Final",
                     "Registro do equipamneto", "Ajuste de Temperatura","Check-List"]  # Ordem dos procesos que utilizaremos como guia para os botoes de atividades da fabricação
listadehilabs = []
ordem_pre_fabricacao = ["Iniciar", "Fabricação"]
atividade_agora = []
nome_dos_hilabs_da_planilha = []
atividades_dos_nomes_dos_hilabs_da_planilha = []
quem_pausou = []
opfs_pra_cada_atividade = []
opfsdodia = []
tempo_pausado = []
horario_do_inicio_de_atividade = []
horario_do_final_de_atividade = []
finalizar = []
identidade_do_botao_de_pausar_atividade = []
identidade_do_botao_de_retrabalho = []
identidade_do_botao_de_opf = []
identidade_do_botao_de_iniciar_atividade = []  # id do botao para atribuir as funcoes com base em qual deles foi clicado
versoes_e_lotes_titulo = ["Lote da Placa:", "Versão STM:", "Versão DART:", "Lote da Câmera:", "Lote da Base:",
                          "Lote da Torre:", "Lote da Tampa:"]
versoes_e_lotes = [0, 0, 0, 0, 0, 0,
                   0]  # [LOTE DA PLACA, VERSAO STM, VERSAO DART, LOTE CAMERA, LOTE BASE, LOTE TORRE, LOTE TAMPA]

#modulo, ação, código troca, motivo do retrabalho, versão dart, setor de origem, versao stm

versoes_retrabalho_titulo = ["Módulo: ", "Ação: ", "Código de Troca: ", "Motivo do Retrabalho: ", "Versão DART:", "Setor de Origem: ", "Versão do STM: ","Aprovado/Reprovado: "]
versoes_retrabalho = [0,0,0,0,0,0,0,0]
# Abre a planilha
wks = gc.open_by_key('1hFGoDjDxU7n_4J56sR-_HaTeHA4JH6vI_QGAbOn6Iqo')  # endereço da planilha polvo
# wks = gc.open_by_key('162Vk3nf_OA1ESnFXI0lE9xpPz69K9vlE18EwcNFREQY')
worksheet = wks.get_worksheet(0)  # aba de atividades
worksheet2 = wks.get_worksheet(1)  # aba de retrabalho
worksheet3 = wks.get_worksheet(2)  # controle Polvo
worksheetopf = wks.get_worksheet(3)  # aba de opfs

window = tk.Tk()  # cria a janela popup
window.title("Controle HILAB:")  # titulo da janela
window.geometry("960x375")  # Size of the window


# Criando um Frame principal
main_frame = Frame(window)
main_frame.pack(fill=BOTH, expand=1)

# Criando um Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# add uma scrollbar no Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configurando o canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

# Criando outro Frame dendro do Canvas
global second_frame
second_frame = Frame(my_canvas)

# add a nova Frame em uma janela no Canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


def hilabs_encontrados():
    coluna_de_materiais = worksheet.col_values(1)
    coluna_de_atividades = worksheet.col_values(8)
    coluna_de_responsaveis = worksheet.col_values(6)
    coluna_de_opfs = worksheet.col_values(7)
    coluna_horario_inicial = worksheet.col_values(2)
    tamanho = len(coluna_de_materiais)
    indice_de_hilab = tamanho - 1
    print("coluna", coluna_de_materiais)
    while indice_de_hilab >= 0:
        if "HILAB-" in coluna_de_materiais[indice_de_hilab]:
            print(coluna_de_materiais[indice_de_hilab], indice_de_hilab)
            if coluna_de_materiais[indice_de_hilab].replace(".", "") in nome_dos_hilabs_da_planilha:
                indice_de_hilab -= 1
                continue

            nome_dos_hilabs_da_planilha.append(coluna_de_materiais[indice_de_hilab].replace(".", ""))
            if "." in coluna_de_materiais[indice_de_hilab]:
                finalizar.append(0)

                proxima_atividade = ordemdefabricacao.index(coluna_de_atividades[indice_de_hilab])
                atividades_dos_nomes_dos_hilabs_da_planilha.append(ordemdefabricacao[proxima_atividade + 1])
                quem_pausou.append(0)
                tempo_pausado.append(0)
                horario_do_inicio_de_atividade.append(0)
                horario_do_final_de_atividade.append(0)
            else:
                atividades_dos_nomes_dos_hilabs_da_planilha.append(coluna_de_atividades[indice_de_hilab])
                finalizar.append(1)
                horario_do_inicio_de_atividade.append(coluna_horario_inicial[indice_de_hilab])
                horario_do_final_de_atividade.append(0)
                quem_pausou.append(0)
                tempo_pausado.append(0)

        indice_de_hilab -= 1
    print(nome_dos_hilabs_da_planilha, atividades_dos_nomes_dos_hilabs_da_planilha)


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


def salvarfabricacao2(indice, selection):
    global fabricacao  # funcao do botao de entrada de opf que salva a opf em uma variavel
    fabricacao = selection
    opfs_pra_cada_atividade[indice] = fabricacao
    print(opfs_pra_cada_atividade, indice)


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
    print("1 no iniciar", atividade_agora)


    if finalizar[indice] == 0:
        print(f"esse é o indice do atividade agora {indice}")
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

        if (indicedeatividade + 1) < len(ordemdefabricacao):
            atividade_agora[indice] = ordemdefabricacao[indicedeatividade + 1]
            bname.configure(text="Iniciar " + atividade_agora[indice])
        elif (indicedeatividade + 1) >= len(ordemdefabricacao):
            bname.configure(text="FINALIZADO")
            bname.destroy()

        finalizar[indice] = 0

        tempo = horario_do_final_de_atividade[indice].strftime('%d/%m/%Y %H:%M:%S')
        print(tempo)
        linha = worksheet.find(listadehilabs[indice])
        worksheet.update_acell('D' + str(linha.row), tempo)
        worksheet.update_acell('A' + str(linha.row), listadehilabs[indice] + ".")

        if (atividade_agora[indice] == "Check-List"):

            if (versoes_e_lotes[6] == 0):
                contador_de_lotes = 0
                while contador_de_lotes < len(versoes_e_lotes):
                    # entrada de valores no proprio tkinter (estou reaproveitando a funcao pra todas as inputs)
                    def getvalue():
                        global versoes_e_lotes
                        versoes_e_lotes[contador_de_lotes] = mystring.get()
                        window.quit()
                        button1.destroy()
                        e1.destroy()

                    mystring = tk.StringVar(second_frame)
                    e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
                    e1.grid(row=indice + 1, column=4)

                    button1 = tk.Button(second_frame, width=15, text=versoes_e_lotes_titulo[contador_de_lotes],
                                        command=getvalue, bg="#aff587")
                    button1.grid(row=indice + 1, column=5)
                    window.mainloop()
                    contador_de_lotes += 1

            elif (atividade_agora[indice] == "Check-List"):
                def getvalue():
                    global versoes_e_lotes
                    versoes_e_lotes[0] = mystring.get()
                    window.quit()
                    button1.destroy()
                    e1.destroy()

                mystring = tk.StringVar(second_frame)
                e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
                e1.grid(row=indice + 1, column=4)

                button1 = tk.Button(second_frame, width=15, text=versoes_e_lotes_titulo[0],
                                    command=getvalue, bg="#aff587")
                button1.grid(row=indice + 1, column=5)
                window.mainloop()

                def getvalue():
                    global versoes_e_lotes
                    versoes_e_lotes[3] = mystring.get()
                    window.quit()
                    button1.destroy()
                    e1.destroy()

                mystring = tk.StringVar(second_frame)
                e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
                e1.grid(row=indice + 1, column=4)

                button1 = tk.Button(second_frame, width=15, text=versoes_e_lotes_titulo[3],
                                    command=getvalue, bg="#aff587")
                button1.grid(row=indice + 1, column=5)
                window.mainloop()

            linha3 = str(len(worksheet3.col_values(1)) + 1)

            worksheet3.update_acell("A"+linha3, datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            worksheet3.update_acell("B" + linha3, opf_de_cada_hilab[indice])
            worksheet3.update_acell("C" + linha3, versoes_e_lotes[0])
            worksheet3.update_acell("D" + linha3, "Check-List")
            worksheet3.update_acell("E" + linha3, responsavel)
            worksheet3.update_acell("F" + linha3, versoes_e_lotes[1])
            worksheet3.update_acell("G" + linha3, versoes_e_lotes[2])
            worksheet3.update_acell("H" + linha3, versoes_e_lotes[3])
            worksheet3.update_acell("I" + linha3, versoes_e_lotes[4])
            worksheet3.update_acell("J" + linha3, versoes_e_lotes[5])
            worksheet3.update_acell("K" + linha3, versoes_e_lotes[6])
            worksheet3.update_acell("L" + linha3, versoes_e_lotes[7])
            worksheet3.update_acell("M" + linha3, versoes_e_lotes[8])
            worksheet3.update_acell("N" + linha3, "-")
            worksheet3.update_acell("O" + linha3, "-")
            worksheet3.update_acell("P" + linha3, "-")

            vamos_trocar_todos_os_hilabs_temporarios = worksheet.col_values(1)
            contador_troca = 0
            while contador_troca < len(vamos_trocar_todos_os_hilabs_temporarios):
                if listadehilabs[indice] == vamos_trocar_todos_os_hilabs_temporarios[contador_troca].replace(".",""):
                    worksheet.update_acell("A"+ str(contador_troca+1),versoes_e_lotes[0]+".")
                contador_troca+= 1


def funcao_pausar_atividade(indice):
    bname = (identidade_do_botao_de_pausar_atividade[indice])
    print(bname, indice, listadehilabs[indice])
    print("pausado", atividade_agora)
    if quem_pausou[indice] == 0:
        tempo_pausado[indice] = datetime.now()
        quem_pausou[indice] = 1
        bname.configure(text="**PARADO**", bg="pink")
    elif quem_pausou[indice] == 1:
        tempo_pausado[indice] = datetime.now() - tempo_pausado[indice]
        print(tempo_pausado[indice])
        quem_pausou[indice] = 0
        bname.configure(text='Pausar ', bg="#e6e6e6")
        linha = worksheet.find(listadehilabs[indice])
        worksheet.update_acell('K' + str(linha.row), str(tempo_pausado[indice]))


def funcao_retrabalho(indice):
    bname = (identidade_do_botao_de_retrabalho[indice])
    linha = worksheet.find(listadehilabs[indice])
    worksheet.update_acell('J' + str(linha.row), "Sim")
    horario = datetime.now()
    worksheet2.update_acell("A" + str(len(worksheet2.col_values(1)) + 1), horario.strftime("%d/%m/%Y %H:%M:%S"))


# FUNCOES DE PRE FABRICACAO DE SOLDA
def iniciar_atividade_pre(indice):  # botao de iniciar atividade que ainda estamos construindo (ele so vai salvar o horario atual quando clica
    bname = (identidade_do_botao_de_iniciar_atividade[indice])
    print(bname, indice)
    demanda = worksheetopf.acell("F" + str((worksheetopf.find(opfs_pra_cada_atividade[indice][3:7])).row)).value
    print(f"essa é a demanda {demanda}")

    coluna_de_opfs = worksheet.col_values(7)
    todas_as_opfs_iguais = []
    contador_opfs = 0
    while contador_opfs < len(coluna_de_opfs):
        if coluna_de_opfs[contador_opfs] == opfs_pra_cada_atividade[indice]:
            todas_as_opfs_iguais.append(worksheet.acell("G" + str(contador_opfs)))
            #print(f"estou aqui {todas_as_opfs_iguais}")

        contador_opfs += 1

    #todas_as_opfs_iguais = worksheet.findall(opfs_pra_cada_atividade[indice])

    contador_pra_procurar_atividades = 0
    quantidade_feita_por_opf = 0
    while contador_pra_procurar_atividades < len(todas_as_opfs_iguais):
        if worksheet.acell("A" + str(todas_as_opfs_iguais[contador_pra_procurar_atividades].row)).value == lista_de_pre_fab[indice]:
            quantidade_feita_por_opf += int(worksheet.acell("I" + str((todas_as_opfs_iguais[contador_pra_procurar_atividades].row))).value)
        contador_pra_procurar_atividades += 1
    identidade_do_botao_de_opf[indice].configure(text=str(quantidade_feita_por_opf) + "/" + demanda)

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
        worksheet.update_acell('G' + linha, opfs_pra_cada_atividade[indice])
        worksheet.update_acell('H' + linha, atividade_agora[indice])


        if indice >= lista_limite_pre_fab:
            lista_ret = worksheet2.findall(lista_de_pre_fab[indice][24:])

            contador_ret = 0
            while contador_ret < len(lista_ret):
                if worksheet2.acell("K" + str(lista_ret[contador_ret].row)).value == None:
                    worksheet2.update_acell('K' + str(lista_ret[contador_ret].row), responsavel)
                    worksheet2.update_acell('J' + str(lista_ret[contador_ret].row), datetime.now().strftime('%d/%m/%Y %H:%M:%S'))


                contador_ret += 1


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



        if indice >= lista_limite_pre_fab:
            lista_ret = worksheet2.findall(lista_de_pre_fab[indice][24:])

            contador_ret = 0
            while contador_ret < len(lista_ret):
                if worksheet2.acell("K" + str(lista_ret[contador_ret].row)).value == responsavel:
                    worksheet2.update_acell('S' + str(lista_ret[contador_ret].row), datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
                    contador_modulos = 0
                    while contador_modulos < len(versoes_retrabalho):
                        # entrada de valores no proprio tkinter (estou reaproveitando a funcao pra todas as inputs)
                        def getvalue():
                            global versoes_retrabalho
                            versoes_retrabalho[contador_modulos] = mystring.get()
                            window.quit()
                            button1.destroy()
                            e1.destroy()

                        mystring = tk.StringVar(second_frame)
                        e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
                        e1.grid(row=indice + 1, column=4)
                        button1 = tk.Button(second_frame, width=15, text=versoes_retrabalho_titulo[contador_modulos],
                                            command=getvalue,
                                            bg="#aff587")
                        button1.grid(row=indice + 1, column=5)
                        window.mainloop()
                        contador_modulos += 1
                    worksheet2.update_acell('L' + str(lista_ret[contador_ret].row), versoes_retrabalho[0])
                    worksheet2.update_acell('M' + str(lista_ret[contador_ret].row), versoes_retrabalho[1])
                    worksheet2.update_acell('N' + str(lista_ret[contador_ret].row), versoes_retrabalho[2])
                    worksheet2.update_acell('O' + str(lista_ret[contador_ret].row), versoes_retrabalho[3])
                    worksheet2.update_acell('P' + str(lista_ret[contador_ret].row), versoes_retrabalho[4])
                    worksheet2.update_acell('Q' + str(lista_ret[contador_ret].row), versoes_retrabalho[5])
                    worksheet2.update_acell('R' + str(lista_ret[contador_ret].row), versoes_retrabalho[6])
                    worksheet2.update_acell('U' + str(lista_ret[contador_ret].row), versoes_retrabalho[7])
                contador_ret += 1


        #lista_de_todas_as_atidades_abertas_iguais = worksheet.findall(lista_de_pre_fab[indice])



        # entrada de valores no proprio tkinter (estou reaproveitando a funcao pra todas as inputs)
        def getvalue():
            """ essa função pega o valor de input de quantidade finalizada da pŕe e verifica
            se esse valor é um numero e um valor valido, caso ao contrario continua esperando um valor valido"""
            global quantidade_finalizada
            quantidade_finalizada = mystring.get()
            while quantidade_finalizada.isnumeric() == False:
                button1.configure(text="Insira um valor valido")
                return
            window.quit()
            button1.destroy()
            e1.destroy()

        mystring = tk.StringVar(second_frame)
        worksheet.findall(opfs_pra_cada_atividade[indice])
        e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
        e1.grid(row=indice + 1, column=4)
        button1 = tk.Button(second_frame, width=15, text="Quantidade Final", command=getvalue, bg = "#aff587")
        button1.grid(row=indice + 1, column=5)
        window.mainloop()

        finalizar[indice] = 0

        tempo = horario_do_final_de_atividade[indice].strftime('%d/%m/%Y %H:%M:%S')

        # Encontra TODAS as celulas em que o processo está aberto, e dentro dessas linhas referentes as celulas abertas, procura qual possui o nome do responsavel certo
        # Depois, armazena a posicao na variavel "linha

        #lista_de_todas_as_atidades_abertas_iguais = worksheet.findall(lista_de_pre_fab[indice])
        coluna_de_material = worksheet.col_values(1)
        lista_de_todas_as_atidades_abertas_iguais = []
        contador_material = 0
        while contador_material < len(coluna_de_material):
            if coluna_de_material[contador_material] == lista_de_pre_fab[indice]:
                lista_de_todas_as_atidades_abertas_iguais.append(worksheet.acell("A" + str(contador_material+1)))

            contador_material += 1

        contador_de_finalizacao = 0
        while (worksheet.acell("F" + str(
                lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao].row)).value) != responsavel:
            contador_de_finalizacao += 1

        linha = lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao]
        worksheet.update_acell('D' + str(linha.row), tempo)
        worksheet.update_acell('I' + str(linha.row), quantidade_finalizada)
        worksheet.update_acell('A' + str(linha.row), lista_de_pre_fab[indice] + ".")
        if "Inspeção" in lista_de_pre_fab[indice]:
            quantidade_da_opf_finalizada = int(quantidade_finalizada) + int(
                worksheetopf.acell("H" + str((worksheetopf.find(fabricacao[3:7])).row)).value)
            worksheetopf.update(("H" + str((worksheetopf.find(opfs_pra_cada_atividade[indice][3:7])).row)),
                                quantidade_da_opf_finalizada)


def funcao_pausar_atividade_pre(indice):
    bname = (identidade_do_botao_de_pausar_atividade[indice])
    print(bname, indice, lista_de_pre_fab[indice])
    if quem_pausou[indice] == 0:
        tempo_pausado[indice] = datetime.now()
        quem_pausou[indice] = 1
        bname.configure(text="**PARADO**", bg="pink")
    elif quem_pausou[indice] == 1:
        tempo_pausado[indice] = datetime.now() - tempo_pausado[indice]
        print(tempo_pausado[indice])
        quem_pausou[indice] = 0
        bname.configure(text='Pausar ', bg="#e6e6e6")
        # Encontra TODAS as celulas em que o processo está aberto, e dentro dessas linhas referentes as celulas abertas, procura qual possui o nome do responsavel certo
        # Depois, armazena a posicao na variavel "linha

        #lista_de_todas_as_atidades_abertas_iguais = worksheet.findall(lista_de_pre_fab[indice])
        coluna_de_material = worksheet.col_values(1)
        lista_de_todas_as_atidades_abertas_iguais = []
        contador_material = 0
        while contador_material < len(coluna_de_material):
            if coluna_de_material[contador_material] == lista_de_pre_fab[indice]:
                lista_de_todas_as_atidades_abertas_iguais.append(worksheet.acell("A" + str(contador_material+1)))

            contador_material += 1

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

        # entrada de valores no proprio tkinter (estou reaproveitando a funcao pra todas as inputs)
        def getvalue():
            print(mystring.get())
            global motivo
            motivo = mystring.get()
            window.quit()
            button1.destroy()
            e1.destroy()

        mystring = tk.StringVar(second_frame)
        e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
        e1.grid(row=indice + 1, column=5)
        button1 = tk.Button(second_frame, width=15, text="Motivo da Parada", command=getvalue,bg = "#aff587")
        button1.grid(row=indice + 1, column=6)

        window.mainloop()

        motivo_anterior = str(worksheet.acell("L" + str(linha.row)).value)
        if motivo_anterior == "None":
            motivo_anterior = ''
        worksheet.update_acell('L' + str(linha.row), motivo_anterior + "; " + motivo)


def funcao_retrabalho_pre(indice):
    bname = (identidade_do_botao_de_retrabalho[indice])
    # Encontra TODAS as celulas em que o processo está aberto, e dentro dessas linhas referentes as celulas abertas, procura qual possui o nome do responsavel certo
    # Depois, armazena a posicao na variavel "linha

    #lista_de_todas_as_atidades_abertas_iguais = worksheet.findall(lista_de_pre_fab[indice])
    coluna_de_material = worksheet.col_values(1)
    lista_de_todas_as_atidades_abertas_iguais = []
    contador_material = 0
    while contador_material < len(coluna_de_material):
        if coluna_de_material[contador_material] == lista_de_pre_fab[indice]:
            lista_de_todas_as_atidades_abertas_iguais.append(worksheet.acell("A" + str(contador_material+1)))

        contador_material += 1

    contador_de_finalizacao = 0
    while (worksheet.acell(
            "F" + str(lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao].row)).value) != responsavel:
        contador_de_finalizacao += 1

    linha = lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao]

    # entrada de valores no proprio tkinter (estou reaproveitando a funcao pra todas as inputs) para QTDE FINALIZADAA
    def getvalue():
        global quantidade_de_retrabalho
        quantidade_de_retrabalho = mystring.get()
        window.quit()
        button1.destroy()
        e1.destroy()
        print(quantidade_de_retrabalho)

    mystring = tk.StringVar(second_frame)
    e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
    e1.grid(row=indice + 1, column=6)
    button1 = tk.Button(second_frame, width=15, text="Quantidade Final", command=getvalue, bg="#aff587")
    button1.grid(row=indice + 1, column=7)
    window.mainloop()

    worksheet.update_acell('J' + str(linha.row), quantidade_de_retrabalho)
    horario = datetime.now()
    linha = str(len(worksheet2.col_values(1)) + 1)
    lista_de_todos_os_retrabalhos_iguais_opf = worksheet2.findall(opfs_pra_cada_atividade[indice])
    contador_de_retrabalho = 0
    quantidade_de_retrabalho2 = 0
    while contador_de_retrabalho < len(lista_de_todos_os_retrabalhos_iguais_opf):
        if (worksheet2.acell("C" + str(lista_de_todos_os_retrabalhos_iguais_opf[contador_de_retrabalho].row)).value) == \
                opfs_pra_cada_atividade[indice]:
            if (
            worksheet2.acell("E" + str(lista_de_todos_os_retrabalhos_iguais_opf[contador_de_retrabalho].row)).value) == \
                    lista_de_pre_fab[indice]:
                quantidade_de_retrabalho2 = int(quantidade_de_retrabalho) + int(worksheet2.acell(
                    "F" + str(lista_de_todos_os_retrabalhos_iguais_opf[contador_de_retrabalho].row)).value)
                linha = str(lista_de_todos_os_retrabalhos_iguais_opf[contador_de_retrabalho].row)
                worksheet2.update_acell('F' + linha, quantidade_de_retrabalho2)

        contador_de_retrabalho += 1

    worksheet2.update_acell("A" + linha, horario.strftime("%d/%m/%Y %H:%M:%S"))
    worksheet2.update_acell("B" + linha, responsavel)
    worksheet2.update_acell("C" + linha, opfs_pra_cada_atividade[indice])
    worksheet2.update_acell("D" + linha, processo)
    worksheet2.update_acell("E" + linha, lista_de_pre_fab[indice])

    if quantidade_de_retrabalho2 == 0:
        worksheet2.update_acell("F" + linha, quantidade_de_retrabalho)

    # entrada de valores no proprio tkinter (estou reaproveitando a funcao pra todas as inputs) para CODIGO DO MATERIAL
    def getvalue():
        global codigo_do_material
        codigo_do_material = mystring.get()
        window.quit()
        button1.destroy()
        e1.destroy()

    mystring = tk.StringVar(second_frame)
    e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
    e1.grid(row=indice + 1, column=6)
    button1 = tk.Button(second_frame, width=15, text="Código do Material", command=getvalue, bg = "#aff587")
    button1.grid(row=indice + 1, column=7)
    window.mainloop()

    worksheet2.update_acell("G" + linha, codigo_do_material)

    # entrada de valores no proprio tkinter (estou reaproveitando a funcao pra todas as inputs) para SINTOMA
    def getvalue():
        global sintoma
        sintoma = mystring.get()
        window.quit()
        button1.destroy()
        e1.destroy()

    mystring = tk.StringVar(second_frame)
    e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
    e1.grid(row=indice + 1, column=6)
    button1 = tk.Button(second_frame, width=15, text="Sintoma", command=getvalue, bg = "#aff587")
    button1.grid(row=indice + 1, column=7)
    window.mainloop()

    worksheet2.update_acell("H" + linha, sintoma)


def funcao_refresh():
    indice = 0
    while indice < len(opfs_pra_cada_atividade):
        if opfs_pra_cada_atividade[indice] == "":
            indice += 1
            continue

        demanda = worksheetopf.acell("F" + str((worksheetopf.find(opfs_pra_cada_atividade[indice][3:7])).row)).value
        todas_as_opfs_iguais = worksheet.findall(opfs_pra_cada_atividade[indice])
        contador_pra_procurar_atividades = 0
        quantidade_feita_por_opf = 0
        while contador_pra_procurar_atividades < len(todas_as_opfs_iguais):
            if worksheet.acell("A" + str(todas_as_opfs_iguais[contador_pra_procurar_atividades].row)).value.replace(".",
                                                                                                                    "") == \
                    lista_de_pre_fab[indice]:
                quantidade_feita_por_opf += int(
                    worksheet.acell("I" + str((todas_as_opfs_iguais[contador_pra_procurar_atividades].row))).value)
            contador_pra_procurar_atividades += 1
        identidade_do_botao_de_opf[indice].configure(text=str(quantidade_feita_por_opf) + "/" + demanda)
        indice += 1


def funcao_refresh_hilab():
    nome_dos_hilabs_da_planilha = []
    finalizar_refresh = []
    horario_do_inicio_de_atividade = []
    horario_do_final_de_atividade = []
    quem_pausou = []
    tempo_pausado = []
    atividades_dos_nomes_dos_hilabs_da_planilha = []
    coluna_de_materiais = worksheet.col_values(1)
    coluna_de_atividades = worksheet.col_values(8)
    coluna_de_responsaveis = worksheet.col_values(6)
    coluna_de_opfs = worksheet.col_values(7)
    coluna_horario_inicial = worksheet.col_values(2)
    tamanho = len(coluna_de_materiais)
    indice_de_hilab = tamanho - 1
    while indice_de_hilab >= 0:
        if "HILAB-" in coluna_de_materiais[indice_de_hilab]:
            print(coluna_de_materiais[indice_de_hilab], indice_de_hilab)
            if coluna_de_materiais[indice_de_hilab].replace(".", "") in nome_dos_hilabs_da_planilha:
                indice_de_hilab -= 1
                continue

            nome_dos_hilabs_da_planilha.append(coluna_de_materiais[indice_de_hilab].replace(".", ""))
            if "." in coluna_de_materiais[indice_de_hilab]:
                finalizar_refresh.append(0)

                proxima_atividade = ordemdefabricacao.index(coluna_de_atividades[indice_de_hilab])
                atividades_dos_nomes_dos_hilabs_da_planilha.append(ordemdefabricacao[proxima_atividade + 1])
                quem_pausou.append(0)
                tempo_pausado.append(0)
                horario_do_inicio_de_atividade.append(0)
                horario_do_final_de_atividade.append(0)
            else:
                atividades_dos_nomes_dos_hilabs_da_planilha.append(coluna_de_atividades[indice_de_hilab])
                finalizar_refresh.append(1)
                horario_do_inicio_de_atividade.append(coluna_horario_inicial[indice_de_hilab])
                horario_do_final_de_atividade.append(0)
                quem_pausou.append(0)
                tempo_pausado.append(0)

        indice_de_hilab -= 1
    indice_refresh = 0
    contador_ordenar_hilabs_da_planilha = 0
    global atividade_agora
    finalizar = []
    atividade_agora = []
    global listadehilabs
    while contador_ordenar_hilabs_da_planilha < len(nome_dos_hilabs_da_planilha):
        if listadehilabs[contador_ordenar_hilabs_da_planilha] in nome_dos_hilabs_da_planilha:
            atividade_agora.append(atividades_dos_nomes_dos_hilabs_da_planilha[nome_dos_hilabs_da_planilha.index(
                listadehilabs[contador_ordenar_hilabs_da_planilha])])
            finalizar.append(finalizar_refresh[
                                 nome_dos_hilabs_da_planilha.index(listadehilabs[contador_ordenar_hilabs_da_planilha])])
        contador_ordenar_hilabs_da_planilha += 1

    # listadehilabs = nome_dos_hilabs_da_planilha
    print(finalizar)
    print(listadehilabs, atividade_agora)
    while indice_refresh < len(finalizar):
        if finalizar[indice_refresh] == 1:  # se tiver pra finalziar, configura o botao pra finalizar
            identidade_do_botao_de_iniciar_atividade[indice_refresh].configure(
                text="Finalizar " + atividade_agora[indice_refresh], bg="purple", fg="white")
            print("finalizar = 1", listadehilabs[indice_refresh])
        elif finalizar[indice_refresh] == 0:
            identidade_do_botao_de_iniciar_atividade[indice_refresh].configure(
                text="Iniciar " + atividade_agora[indice_refresh], bg="#e6e6e6", fg="black")

        indice_refresh += 1
    print("print verto", atividade_agora)




options = tk.StringVar(second_frame)
options.set(responsavel)  # default value

abaresponsavel = tk.Label(second_frame, text='Responsável', width=10)
abaresponsavel.grid(row=2, column=1)

opcaoresponsa = tk.OptionMenu(second_frame, options, "Agatha", "Marcia", "Henrique", "Priscila", "Tiago", "Val",
                              command=salvarentradas)  # config da combobox de responsavel
opcaoresponsa.grid(row=2, column=2)

opcoesprocesso = tk.StringVar(second_frame)
opcoesprocesso.set(processo)  # default value

abasprocesso = tk.Label(second_frame, text='Processo', width=10)
abasprocesso.grid(row=5, column=1)


optionsprocesso = tk.OptionMenu(second_frame, opcoesprocesso, "Pré-Fabricação", "Fabricação","Atividade Extra",
                                command=salvarprocesso)  # config da combobox de proceso
optionsprocesso.grid(row=5, column=2)

optionsfabricacao = tk.StringVar(second_frame)
optionsfabricacao.set(fabricacao)  # default value



optionsiniciarouresume = tk.StringVar(second_frame)

optionsiniciarouresume.set(iniciarouresume)  # default value

abasiniciarouresume = tk.Label(second_frame, text='Iniciar/Continuar: ',
                               width=15)  # config da combobox de iniciar ou continuar
abasiniciarouresume.grid(row=10, column=1)

opcoesiniciarouresume = tk.OptionMenu(second_frame, optionsiniciarouresume, "Iniciar", "Continuar",
                                      command=salvariniciarouresume)
opcoesiniciarouresume.grid(row=10, column=2)


def func():  # definicao da funcao de botoes em que so segue pra prox acao enquanto fecha a janela
    window.quit()


def continuarcomretorno(selection):
    print(selection)


continue_button = tk.Button(second_frame, text='Enviar', command=func)
continue_button.config(width=10)
# set the coordinates as you want. here 2,6 for the example
continue_button.grid(row=12, column=2)

window.mainloop()
abaresponsavel.destroy()
opcaoresponsa.destroy()
abasprocesso.destroy()
optionsprocesso.destroy()
abasiniciarouresume.destroy()

opcoesiniciarouresume.destroy()
continue_button.destroy()  # fecha todas as janelas

window.title("Controle HILAB: " + responsavel + "--------" + processo)  # titulo da janela

if processo == "Fabricação":

    if iniciarouresume == "Iniciar":
        #scrollbar()
        print("Iniciar2")
        label_de_demanda = tk.Label(second_frame, text='Demanda do dia: ',
                                    width=15)  # config da combobox de demanda
        label_de_demanda.pack()
        Entrada_de_Demanda_de_Equipamentos = tk.Entry(second_frame)
        Entrada_de_Demanda_de_Equipamentos.pack()
        lista_de_opfs = worksheetopf.findall("Aberto")
        indice_opfs = 0
        while indice_opfs < len(lista_de_opfs):
            opfsdodia.append(
                "OPF" + (worksheetopf.acell("C" + str(lista_de_opfs[indice_opfs].row)).value) + "/2021 " + (
                    worksheetopf.acell("B" + str(lista_de_opfs[indice_opfs].row))).value)
            indice_opfs += 1
        print(opfsdodia)

        opcoesfabricacao = tk.OptionMenu(second_frame, optionsfabricacao, *opfsdodia,
                                         command=salvarfabricacao)  # config da combobox de opf
        opcoesfabricacao.pack()

        continue_button = tk.Button(second_frame, text='Enviar', command=func)
        continue_button.pack()

        window.mainloop()
        demanda = Entrada_de_Demanda_de_Equipamentos.get()  # variavel que recebeu a demanda
        Entrada_de_Demanda_de_Equipamentos.destroy()
        continue_button.destroy()
        label_de_demanda.destroy()
        opcoesfabricacao.destroy()

        demanda = int(demanda)
        contador_hilabs = 1
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
        #scrollbar()

        while indice < len(listadehilabs):
            abasfabricacao = tk.Label(second_frame, text=listadehilabs[indice],
                                      width=10)  # nome do hilab do indice pela lista convertida
            abasfabricacao.grid(row=(indice + 1), column=1)
            abasfabricacao = tk.Label(second_frame, text=fabricacao,
                                      width=45)  # puxa o status pela key do dict de hilabs
            abasfabricacao.grid(row=(indice + 1), column=2)

            botao_iniciar_atividade = tk.Button(second_frame, text=('Iniciar ' + atividade_agora[indice]),
                                                command=partial(iniciar_atividade_e_atualizar_status_do_hilab,
                                                                indice))  # botao de iniciar ativ
            botao_iniciar_atividade.config(width=15)
            identidade_do_botao_de_iniciar_atividade.append(botao_iniciar_atividade)
            # set the coordinates as you want. here 2,6 for the example
            botao_iniciar_atividade.grid(row=indice + 1, column=3)


            botao_pausar_atividade = tk.Button(second_frame, text=('Pausar ' + atividade_agora[indice]),
                                               command=partial(funcao_pausar_atividade, indice))  # botao de iniciar ativ

            botao_pausar_atividade.config(width=15)
            identidade_do_botao_de_pausar_atividade.append(botao_pausar_atividade)
            # set the coordinates as you want. here 2,6 for the example
            botao_pausar_atividade.grid(row=indice + 1, column=5)

            botao_de_retrabalho = tk.Button(second_frame, text=('Retrabalho'),
                                            command=partial(funcao_retrabalho, indice))  # botao de iniciar ativ
            botao_de_retrabalho.config(width=15, bg='red')
            identidade_do_botao_de_retrabalho.append(botao_de_retrabalho)
            # set the coordinates as you want. here 2,6 for the example
            botao_de_retrabalho.grid(row=indice + 1, column=7)

            indice += 1  # incrementa indice
            time.sleep(1)
        #scrollbar()



    elif iniciarouresume == "Continuar":
        #scrollbar()
        print("Continuar2")
        # Atualiza celula

        # espaço para determinar o tamanho dos vetores em que os HILABS sao dependentes para as logicas do programa

        hilabs_encontrados()
        listadehilabs = nome_dos_hilabs_da_planilha
        atividade_agora = atividades_dos_nomes_dos_hilabs_da_planilha

        indice = 0

        while indice < len(nome_dos_hilabs_da_planilha):
            abasfabricacao = tk.Label(second_frame, text=listadehilabs[indice],
                                      width=10)  # nome do hilab do indice pela lista convertida
            abasfabricacao.grid(row=(indice + 1), column=1)
            abasfabricacao = tk.Label(second_frame, text=fabricacao,
                                      width=45)  # puxa o status pela key do dict de hilabs
            abasfabricacao.grid(row=(indice + 1), column=2)

            botao_iniciar_atividade = tk.Button(second_frame, text=('Iniciar ' + atividade_agora[indice]),
                                                command=partial(iniciar_atividade_e_atualizar_status_do_hilab,
                                                                indice))  # botao de iniciar ativ

            if finalizar[indice] == 1:  # se tiver pra finalziar, configura o botao pra finalizar
                botao_iniciar_atividade.configure(text="Finalizar " + atividade_agora[indice], bg="purple", fg="white")

            botao_iniciar_atividade.config(width=15)
            identidade_do_botao_de_iniciar_atividade.append(botao_iniciar_atividade)
            # set the coordinates as you want. here 2,6 for the example
            botao_iniciar_atividade.grid(row=indice + 1, column=3)


            botao_pausar_atividade = tk.Button(second_frame, text=('Pausar ' + atividade_agora[indice]),
                                               command=partial(funcao_pausar_atividade, indice))  # botao de iniciar ativ
            botao_pausar_atividade.config(width=15)
            identidade_do_botao_de_pausar_atividade.append(botao_pausar_atividade)
            # set the coordinates as you want. here 2,6 for the example
            botao_pausar_atividade.grid(row=indice + 1, column=5)

            botao_de_retrabalho = tk.Button(second_frame, text=('Retrabalho'),
                                            command=partial(funcao_retrabalho, indice))  # botao de iniciar ativ
            botao_de_retrabalho.config(width=15, bg='red')
            identidade_do_botao_de_retrabalho.append(botao_de_retrabalho)
            # set the coordinates as you want. here 2,6 for the example
            botao_de_retrabalho.grid(row=indice + 1, column=7)

            indice += 1  # incrementa indice


    botao_refresh = tk.Button(second_frame, text=('Refresh'), command=funcao_refresh_hilab)  # botao de iniciar ativ
    botao_refresh.config(width=15, bg='yellow')
    botao_refresh.grid(row=50, column=3)


elif processo == "Pré-Fabricação":
    options_pre_fabricacao = tk.StringVar(second_frame)
    options_pre_fabricacao.set(qual_pre_fabricacao)  # default value

    abas_pre_fabricacao = tk.Label(second_frame, text='Pré-Fabricações:  ',
                                   width=15)  # config da combobox de iniciar ou continuar
    abas_pre_fabricacao.grid(row=10, column=1)

    opcoes_pre_fabricacao = tk.OptionMenu(second_frame, options_pre_fabricacao, "Solda", "Coolerfan", "Termobloco",
                                          command=salvar_pre_fabricacoes)
    opcoes_pre_fabricacao.grid(row=10, column=2)

    continue_button = tk.Button(second_frame, text='Enviar', command=func)
    continue_button.config(width=10)
    # set the coordinates as you want. here 2,6 for the example
    continue_button.grid(row=12, column=2)

    window.mainloop()
    continue_button.destroy()
    abas_pre_fabricacao.destroy()
    opcoes_pre_fabricacao.destroy()
    lista_de_opfs = worksheetopf.findall("Aberto")
    indice_opfs = 0
    while indice_opfs < len(lista_de_opfs):
        opfsdodia.append("OPF" + (worksheetopf.acell("C" + str(lista_de_opfs[indice_opfs].row)).value) + "/2021 " + (
            worksheetopf.acell("B" + str(lista_de_opfs[indice_opfs].row))).value)
        indice_opfs += 1
    print(opfsdodia)

    lista_de_soldas = ["NTC", "Inspeção NTC", "NFC", "Inspeçao NFC e Ligação 12C",
                       "Barra de Led","Inspeção Barra de Led",
                       "Cabo do Aquecedor", "Inspeção Cabo do Aquecedor",
                       "Contagem"]

    lista_de_termobloco = ["Colagem do Aquecedor e NTC", "Inspeção Termobloco", "Contagem"]

    lista_de_cooler = ["Corte do cabo", "Inspeção do Coolerfan", "Crimpamento", "Contagem"]

    # aqui começa a parte de iniciar a atividade da pre fabricacao
    indice = 0
    if qual_pre_fabricacao == "Solda":
        lista_de_pre_fab = lista_de_soldas
    elif qual_pre_fabricacao == "Termobloco":
        lista_de_pre_fab = lista_de_termobloco
    elif qual_pre_fabricacao == "Coolerfan":
        lista_de_pre_fab = lista_de_cooler
    contador_pre = 1

    qtde_de_retrab = 0
    lista_limite_pre_fab = len(lista_de_pre_fab)
    linha_retrabalho = len(worksheet2.col_values(1))
    linha_maxima = linha_retrabalho
    """while linha_retrabalho > (linha_maxima -15):
        if worksheet2.acell("K"+ str(linha_retrabalho)).value == None:
            lista_de_pre_fab.append("Retrabalho & Inspeção - " + worksheet2.acell("E"+ str(linha_retrabalho)).value)
        linha_retrabalho -= 1
    print(lista_de_pre_fab)"""


    while contador_pre <= len(lista_de_pre_fab):
        quem_pausou.append(0)
        tempo_pausado.append(0)
        horario_do_inicio_de_atividade.append(0)
        horario_do_final_de_atividade.append(0)
        finalizar.append(0)
        atividade_agora.append(ordem_pre_fabricacao[1])
        contador_pre += 1
        opfs_pra_cada_atividade.append("")

    botao_refresh = tk.Button(second_frame, text=('Refresh'), command=funcao_refresh)  # botao de iniciar ativ
    botao_refresh.config(width=15, bg='yellow')
    botao_refresh.grid(row=50, column=3)

    while indice < len(lista_de_pre_fab):
        abas_pre_fabricacao_no_dashboard = tk.Label(second_frame, text=lista_de_pre_fab[indice],
                                                    width=30)
        abas_pre_fabricacao_no_dashboard.grid(row=(indice + 1), column=1)


        quantos_faltam_por_atividade = tk.Label(second_frame, text="-",width=8)
        quantos_faltam_por_atividade.grid(row=(indice + 1), column=3)

        optionsfabricacao = tk.StringVar(second_frame)
        optionsfabricacao.set(fabricacao)  # default value


        opcoesfabricacao = tk.OptionMenu(second_frame, optionsfabricacao, *opfsdodia,
                                         command=partial(salvarfabricacao2,indice))  # config da combobox de opf
        opcoesfabricacao.grid(row=indice+1, column=2)

        identidade_do_botao_de_opf.append(quantos_faltam_por_atividade)
        print(identidade_do_botao_de_opf)


        botao_iniciar_atividade = tk.Button(second_frame, text=("Iniciar Pré"), command=partial(iniciar_atividade_pre, indice))  # botao de iniciar ativ

        botao_iniciar_atividade.config(width=15)
        identidade_do_botao_de_iniciar_atividade.append(botao_iniciar_atividade)
        # set the coordinates as you want. here 2,6 for the example
        botao_iniciar_atividade.grid(row=indice + 1, column=4)

        botao_pausar_atividade = tk.Button(second_frame, text=('Pausar '),
                                           command=partial(funcao_pausar_atividade_pre,
                                                           indice))  # botao de iniciar ativ
        botao_pausar_atividade.config(width=15)
        identidade_do_botao_de_pausar_atividade.append(botao_pausar_atividade)
        # set the coordinates as you want. here 2,6 for the example
        botao_pausar_atividade.grid(row=indice + 1, column=5)


        botao_de_retrabalho = tk.Button(second_frame, text=('Retrabalho'),command=partial(funcao_retrabalho_pre, indice))  # botao de iniciar ativ
        botao_de_retrabalho.config(width=10, bg='red')
        identidade_do_botao_de_retrabalho.append(botao_de_retrabalho)
        # set the coordinates as you want. here 2,6 for the example
        botao_de_retrabalho.grid(row=indice + 1, column=6)

        indice += 1  # incrementa indice
        print(indice)



elif processo == "Atividade Extra":
    def atividadeextra():
        print(mystring.get())
        global atividade_extra
        global finalizar
        print(finalizar)
        atividade_extra = mystring.get()
        e1.destroy()
        button1.configure(text=("Finalizar "+ atividade_extra))
        if finalizar ==0:
            linha = str(len(worksheet.col_values(1)) + 1)
            worksheet.update_acell('A' + linha, atividade_extra)
            worksheet.update_acell('B' + linha, datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
            worksheet.update_acell('E' + linha, "-")
            worksheet.update_acell('F' + linha, responsavel)
            worksheet.update_acell('G' + linha, "-")
            worksheet.update_acell('H' + linha, "Atividade Extra")
            finalizar = 1
        elif finalizar ==1:
            procurar_linha = worksheet.findall(atividade_extra)
            contador_extra_finalizar = 0
            while contador_extra_finalizar < len(procurar_linha):
                if responsavel == worksheet.acell("F"+str(procurar_linha[contador_extra_finalizar].row)).value:
                    linha = str(procurar_linha[contador_extra_finalizar].row)
                    worksheet.update_acell('D' + linha, datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
                    worksheet.update_acell('A' + linha, atividade_extra + ".")
                    window.quit()
                    break
            finalizar = 0



    def pausa_atividade_extra():
        global quem_pausou
        global tempo_pausado
        global tempo_pausado2
        if quem_pausou == 0:
            tempo_pausado = datetime.now()
            quem_pausou = 1
            botao_pausar_atividade.configure(text="**PARADO**", bg="pink")
        elif quem_pausou == 1:
            tempo_pausado2 = datetime.now()
            quem_pausou = 0

            # entrada de valores no proprio tkinter (estou reaproveitando a funcao pra todas as inputs)
            def getvalue():
                print(mystring.get())
                global motivo
                motivo = mystring.get()
                window.quit()
                button1.destroy()
                e1.destroy()

            mystring = tk.StringVar(second_frame)
            e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
            e1.grid(row=1, column=5)
            button1 = tk.Button(second_frame, width=15, text="Motivo da Parada", command=getvalue, bg="#aff587")
            button1.grid(row=1, column=6)

            window.mainloop()
            lista_de_todas_as_atidades_abertas_iguais = worksheet.findall(atividade_extra)
            contador_de_finalizacao = 0
            while (worksheet.acell("F" + str(
                    lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao].row)).value) != responsavel:
                contador_de_finalizacao += 1

            linha = lista_de_todas_as_atidades_abertas_iguais[contador_de_finalizacao]

            motivo_anterior = str(worksheet.acell("L" + str(linha.row)).value)
            if motivo_anterior == "None":
                motivo_anterior = ''
            worksheet.update_acell('L' + str(linha.row), motivo_anterior + "; " + motivo)
            worksheet.update_acell('M' + str(linha.row), tempo_pausado.strftime('%d/%m/%Y %H:%M:%S'))
            worksheet.update_acell('N' + str(linha.row), tempo_pausado2.strftime('%d/%m/%Y %H:%M:%S'))
            botao_pausar_atividade.configure(text='Pausar ', bg="#e6e6e6")

        print("Botao")

    mystring = tk.StringVar(second_frame)
    e1 = Entry(second_frame, textvariable=mystring, width=15, fg="blue", bd=3, selectbackground='violet')
    e1.grid(row=1, column=2)

    button1 = tk.Button(second_frame, width=25, text="Atividade Extra para Iniciar:", command=partial(atividadeextra))

    button1.grid(row=1, column=1)
    quem_pausou = 0
    finalizar = 0
    botao_pausar_atividade = tk.Button(second_frame, text=('Pausar'), command=(pausa_atividade_extra))  # botao de iniciar ativ
    botao_pausar_atividade.grid(row=1, column=3)

window.mainloop()
