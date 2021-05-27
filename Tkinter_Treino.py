"""
Treino com tkimter, vamos fazer um botao q vai registrar a data e a hora na planilha

root = Tk()

def onde_escrever():
    linha = len(worksheet.col_values(1)) + 1
    print(linha)
    return linha


def hora():
    tempo= datetime.now()
    t1 = tempo.strftime('%d/%m/%Y %H:%M')
    worksheet.update_cell(onde_escrever(), 1, t1)


Mybutton = Button(root, text="clique aqui", command=hora)
Mybutton.pack()

root.mainloop()
--------------------------------------------------------
criando a janela, adicionando dropbox e registrando o valor na planilea
window = tk.Tk()  # cria a janela popup
window.title("Controle HILAB") #titulo da janela
window.geometry("660x175")  # Size of the window



# Abrir outra janela

Hilabs = {
  "HILAB-1": "Iniciar",
  "HILAB-2": "Iniciar",
  "HILAB-3": "Iniciar",
  "HILAB-4": "Iniciar",
  "HILAB-5": "Iniciar"
}                                #nomes dos hilabs que vao aparecer na janela para iniciar atividade, planejamos puxar a partir da demanda e scanear no registro final

listadehilabs = list(Hilabs.keys()) #transforma dict em lista pra ser usados nas formulas

indice = 0  #variavel indice pra que o loop de criacao de linhas na janela para os respectivos hilabs seja posta

while indice <len(listadehilabs):
    abasfabricacao = Label(root,  text=listadehilabs[indice], width=10)    #nome do hilab do indice pela lista convertida
    abasfabricacao.grid(row=(indice+1), column=1)
    abasfabricacao = Label(root,  text=Hilabs[listadehilabs[indice]], width=10 )  # puxa o status pela key do dict de hilabs
    abasfabricacao.grid(row=(indice+1),column=2)
    continue_button = Button(root, text=('Iniciar ' + str(ordemdefabricacao[1])))  # , command=iniciar_atividade_e_atualizar_status_do_hilab) #botao de iniciar ativ
    continue_button.config(width=15)
    # set the coordinates as you want. here 2,6 for the example
    continue_button.grid(row=indice+1,column=3)
    indice +=1 #incrementa indice



"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta
from tkinter import *
import tkinter as tk

scope = ['https://spreadsheets.google.com/feeds']

credentials = ServiceAccountCredentials.from_json_keyfile_name('key42.json', scope)

gc = gspread.authorize(credentials)


wks = gc.open_by_key('162Vk3nf_OA1ESnFXI0lE9xpPz69K9vlE18EwcNFREQY')

worksheet = wks.get_worksheet(0)

root = Tk()
root.title("Controle Hilab")
root.geometry("660x175")
responsavel =[
    "Outro",
    "Batman",
    "Natuto",
    "Itchigo",
    "Homem Aranha"
]
processos = [
    "Outro",
    "Pré-Fabricação",
    "Fabricação",
    "Gravação de Dispositivos"
]
opfs = ["Outro",
         "OPF2020",
         "OPF2021",
         "OPF2022"
         ]
ordemdefabricacao = [
    "Iniciar",
    "Jiga-Test",
    "Pré-Montagem",
    "Montagem Teste",
    "Montagem Final",
    "Check-List"
]

def onde_escrever():
    linha = len(worksheet.col_values(1)) + 1
    print(linha)
    return linha


def hora():
    tempo= datetime.now()
    t1 = tempo.strftime('%d/%m/%Y %H:%M')
    worksheet.update_cell(onde_escrever(), 1, t1)
    root.quit()


def p_responsa(selection):
    #nome = responsa.get()
    worksheet.update_cell(onde_escrever(), 5, selection)
    print(selection)


def p_processo(selection):
    worksheet.update_cell(onde_escrever(), 4, selection)
    print(selection)


def p_opf(selection):
    worksheet.update_cell(onde_escrever(), 6, selection)
    print(selection)


def p_atividade(selection):
    worksheet.update_cell(onde_escrever(), 2, selection)
    print(selection)


# Cria a aba responsavel
aba_responsavel = Label(root, text="Responsavel", width=10)
aba_responsavel.grid(row=2, column=1)

responsa = StringVar()
responsa.set(responsavel[0])

drop = OptionMenu(root, responsa, *responsavel, command=p_responsa)
drop.grid(row=2, column=2)

# Cria a aba processo
aba_processo = Label(root, text="Processo", width=10)  # Escreve Processos ao lado do botao
aba_processo.grid(row=4, column=1)

processo = StringVar()  # Cria uma variavel para receber o valor do botao
processo.set(processos[0])

drop = OptionMenu(root, processo, *processos, command=p_processo)  # Cria o botao em si
drop.grid(row=4, column=2)

# Cria a aba OPF
aba_opf = Label(root, text="OPF", width=10)
aba_opf.grid(row=6, column=1)

opf = StringVar()
opf.set(opfs[0])

drop = OptionMenu(root, opf, *opfs, command=p_opf)
drop.grid(row=6, column=2)

# Cria a aba tipo de atividade
aba_atividade = Label(root, text="Iniciar / Continuar", width=15)
aba_atividade.grid(row=8, column=1)

atividade= StringVar()
atividade.set('Outro')

drop = OptionMenu(root, atividade, "Iniciar", "Continuar", command=p_atividade)
drop.grid(row=8, column=2)

Mybutton = Button(root, text="Enviar", command=hora)
Mybutton.grid(row=10, column=2)
root.mainloop()
# --------------------------------------------------------------------------------------------
