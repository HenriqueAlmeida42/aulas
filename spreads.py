import gspread
import tkinter as tk
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timezone
from functools import partial

# Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

# Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name('chave.json', scope)  # validacao da chave

# Se autentica
gc = gspread.authorize(credentials)

responsavel = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
processo = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
fabricacao = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
iniciarouresume = "Outro"  # texto inicial nos botoes que sao regidos por variaveis no combobox
ordemdefabricacao = ["Iniciar", "Jiga-Test", "Pré-Montagem", "Montagem Teste", "Montagem Final",
                     "Check-List"]  # Ordem dos procesos que utilizaremos como guia para os botoes de atividades da fabricação
hilabs = {}
pausar = 0
identidade_do_botao_de_pausar_atividade = []
identidade_do_botao_de_iniciar_atividade = [] #id do botao para atribuir as funcoes com base em qual deles foi clicado
# Abre a planilha
wks = gc.open_by_key('1SXvafCDkFjrDAp5fZSRmRYlJZ9LeUMS3r8dF7KEmAPQ')  # endereço da planilha

worksheet = wks.get_worksheet(0)  # pegar a primeira aba

window = tk.Tk()  # cria a janela popup
window.title("Controle HILAB")  # titulo da janela
window.geometry("660x175")  # Size of the window 


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


def iniciar_atividade_e_atualizar_status_do_hilab(indice):   #botao de iniciar atividade que ainda estamos construindo (ele so vai salvar o horario atual quando clica
    bname = (identidade_do_botao_de_iniciar_atividade[indice])
    horario_do_inicio_de_atividade = datetime.now()

    bname.configure(text="Finalizar")


def funcao_pausar_atividade(indice):
    bname = (identidade_do_botao_de_pausar_atividade[indice])
    horario_do_inicio_de_atividade = datetime.now()
    bname.configure(text="pausou")

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

demanda = 5  # teoricamente a demanda pre definida (pretendemos puxar pela planilha das opfs)

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

# Atualiza celula

atividade_agora = [ordemdefabricacao[1],ordemdefabricacao[1],ordemdefabricacao[1],ordemdefabricacao[1],ordemdefabricacao[1] ]

hilabs = {
    "HILAB-1": "Iniciar",
    "HILAB-2": "Iniciar",
    "HILAB-3": "Iniciar",
    "HILAB-4": "Iniciar",
    "HILAB-5": "Iniciar"
}  # nomes dos hilabs que vao aparecer na janela para iniciar atividade, planejamos puxar a partir da demanda e scanear no registro final

listadehilabs = list(hilabs.keys())  # transforma dict em lista pra ser usados nas formulas

indice = 0  # variavel indice pra que o loop de criacao de linhas na janela para os respectivos hilabs seja posta

while indice < len(listadehilabs):
    abasfabricacao = tk.Label(window, text=listadehilabs[indice],
                              width=10)  # nome do hilab do indice pela lista convertida
    abasfabricacao.grid(row=(indice + 1), column=1)
    abasfabricacao = tk.Label(window, text=hilabs[listadehilabs[indice]],
                              width=10)  # puxa o status pela key do dict de hilabs
    abasfabricacao.grid(row=(indice + 1), column=2)


    botao_iniciar_atividade = tk.Button(window, text=('Iniciar ' + atividade_agora[indice]), command = partial(iniciar_atividade_e_atualizar_status_do_hilab, indice))  # botao de iniciar ativ
    botao_iniciar_atividade.config(width=15)
    identidade_do_botao_de_iniciar_atividade.append(botao_iniciar_atividade)
    # set the coordinates as you want. here 2,6 for the example
    botao_iniciar_atividade.grid(row=indice + 1, column=3)

    botao_pausar_atividade = tk.Button(window, text=('Pausar ' + atividade_agora[indice]), command = partial(funcao_pausar_atividade, indice))  # botao de iniciar ativ
    botao_pausar_atividade.config(width=15)
    identidade_do_botao_de_pausar_atividade.append(botao_pausar_atividade)
    # set the coordinates as you want. here 2,6 for the example
    botao_pausar_atividade.grid(row=indice + 1, column=5)

    indice += 1  # incrementa indice

window.mainloop()

