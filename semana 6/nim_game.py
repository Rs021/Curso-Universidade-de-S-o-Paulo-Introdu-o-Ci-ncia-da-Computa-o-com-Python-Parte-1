def computador_escolhe_jogada(n, m):
    jogada = 1

    while jogada != m:
        if (n - jogada) % (m + 1) == 0:
            return jogada

        else:
            pass

    return jogada


def usuario_escolhe_jogada(n, m):
    valid = False

    while not valid:
        m_retirar = int(input("Quantas peças você vai tirar?"))
        if m_retirar > m or m_retirar < 1 or m_retirar == ValueError():
            print("Oops! Jogada inválida! Tente de novo.")

        else:
            valid = True

    return m_retirar


def partida():
    n = int(input("Quantas peças? "))

    m = int(input("Limite de peças por jogada? "))

    vezDoPC = False

    if n % (m + 1) == 0:
        print()
        print("Voce começa!")

    else:
        print()
        print("Computador começa!")
        vezDoPC = True

    while n > 0:
        if vezDoPC:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print()
                print("O computador tirou uma peça")
            else:
                print()
                print("O computador tirou", computadorRemove, "peças")

            vezDoPC = not vezDoPC
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print()
                print("Você tirou uma peça")
            else:
                print()
                print("Você tirou", jogadorRemove, "peças")
            vezDoPC = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print("Agora restam,", n, "peças no tabuleiro.")
                print()

    print("Fim do jogo! O computador ganhou!")


def campeonato():
    rodada = 1

    while rodada <= 3:
        print("**** Rodada", rodada, "****")
        partida()
        rodada += 1

    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")


print("Bem-vindo ao jogo do NIM! Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")

escolha = int(input())

if escolha == 1:
    print("Voce escolheu um Partida!")
    partida()

else:
    print("Voce escolheu um campe   onato!")
    campeonato()
