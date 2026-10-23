# ===== BLOCO 1: MATRIZ E NOMES (Kallyson) =====
# tabuleiro 3x3 declarado por extenso, linha por linha.
# casa vazia = " " (espaço).
tabuleiro = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

print("          JOGO DA VELHA                 ")
nome1 = ""
while nome1 == "":
    nome1 = input("Nome do jogador 1 (será o X): ")
    if nome1 == "":
        print("O nome não pode ficar vazio.")

nome2 = ""
while nome2 == "" or nome2 == nome1:
    nome2 = input("Nome do jogador 2 (será o O): ")
    if nome2 == "":
        print("O nome não pode ficar vazio.")
    elif nome2 == nome1:
        print("Os dois jogadores precisam ter nomes diferentes.")

       # ===== BLOCO 1: MENU PRINCIPAL (Kallyson) =====
opcao = ""
while opcao != "4":
    print("")
    print("============== MENU ==============")
    print("1 - Jogar")
    print("2 - Ver regras")
    print("3 - Ver placar")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Em construção.")

    # ===== BLOCO 1: REGRAS (Kallyson) =====
    elif opcao == "2":
        print("Em construção.")

   