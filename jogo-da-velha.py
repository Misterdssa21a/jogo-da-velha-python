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

