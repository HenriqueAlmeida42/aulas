"""
Desafio MR - robo em marte

criar um sitema que controle um robo ao receber comandos especificos e retorne sua pocição.
 Os comandos devem ser:
  "M" para se mover uma pocição;
  "L" para girar 90 graus para esquerda;
  "R" para girar 90 fraus para a direita.
A pocição deve ser mostrada como (0,0,N) sendo:
 "N" para NORTH;
 "S" para SOUTH;
 "E" para EAST;
 "W" para WEST.

duvidas que tive sobre o desafio e como as resolvi:

1 -> O que fazer como entradas diferentes das letras expecificas?
R: Dizer ao usuario que o dado é invalido e reforça que as entradas permitidas.

2 ->  Maiscula e miniscula faz diferença?
R: Não, para garantir isto todas as entradas são transformadas em maisculas.

3 -> O texto ididca que é uma area retangular mas tambem indica para se trabalhar com uma matriz de pocisão
quadrada 5x5 o que fazer?
R: Trabalhar com a matris 5x5 indicada, sendo da pocição da 0,0 até a pocição 4,4.

4 -> O que fazer se for mandado sair da area desginada?
R: informar ao usuario que estas cordenadas farão o robo entrar em uma zona perigosa e por isso não são permitidas.

"""
movimento = []  # Variavel que guarda a entrada somente com letras maiusculas e validas
posicao = [0, 0, 'N']  # Posição em que se encontra o robo
bussula = ['N', 'E', 'S', 'W']  # Variavel usada para idendificar para qual sentido o robo está direcionado
gosth = []  # Variavel que simula a movimentação para ter certeza que ela é valida
y = 1

while y == 1:
    print(" CONTROLE DO ROBO ",
          "\n Digite M para mover o Robo",
          "\n Digite L para girar  Robo para esquerda",
          "\n Digite R para girar o Robo para direita",
          "\n Digite FIM para finalizar o programa")

    print(f"\n O Robo se encontra na posição:{posicao}")

    entrada = input('\nDigite o movimento que deseja fazer: ')
    direcao = entrada.upper()
    if direcao == 'FIM':
        break

    for x in range(len(direcao.upper())):
        if direcao[x] == "M":
            movimento.append(direcao[x])
        elif direcao[x] == "L":
            movimento.append(direcao[x])
        elif direcao[x] == "R":
            movimento.append(direcao[x])
        else:
            print("\nValor inserido invalido, por favor digite somente valores validos")
            break

    gosth = posicao.copy()

    for letra in range(len(movimento)):
        sentido = gosth[2]

        if movimento[letra] == 'R':
            bussula.reverse()
            gosth[2] = bussula[bussula.index(sentido) - 1]
            bussula.reverse()
        if movimento[letra] == 'L':
            gosth[2] = bussula[bussula.index(sentido) - 1]

        if movimento[letra] == "M":
            if sentido == "N":
                gosth[0] = gosth[0] + 1
            elif sentido == "S":
                gosth[0] = gosth[0] - 1
            elif sentido == "E":
                gosth[1] = gosth[1] + 1
            elif sentido == "W":
                gosth[1] = gosth[1] - 1

    if gosth[0] <= -1 or gosth[0] >= 5:
        print("\nEsta sequencia de movimentos coloca o robo em perigo!!!", "\n coloque uma nova sequencia")
    elif gosth[1] <= -1 or gosth[1] >= 5:
        print("\nEsta sequencia de movimentos coloca o robo em perigo!!!", "\n coloque uma nova sequencia")
    else:
        posicao = gosth.copy()
        print("\nO Robo foi movimentado para:\n")
        print(posicao)

    movimento.clear()

    print("---" * 42)
