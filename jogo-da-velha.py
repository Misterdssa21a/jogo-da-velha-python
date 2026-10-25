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
         # ===== BLOCO 1: TABULEIRO NA TELA (Kallysson) =====
        print("")
        print("      1   2   3")
        print("    +---+---+---+")
        # for aninhado que desenha o tabuleiro:
        # o for de fora (i) percorre as linhas A, B e C; para cada linha,
        # o for de dentro (j) percorre as colunas 1, 2 e 3 e junta o
        # conteúdo das 3 casas em uma única linha de texto.
        for i in range(3):
            if i == 0:
                letras = "A"
            elif i == 1:
                letras = "B"
            else:
                letras = "C"
            desenho = f"  {letras} |"
            for j in range(3):
                desenho = f"{desenho} {tabuleiro[i][j]} |"
            print(desenho)
            print("    +---+---+---+")

                    # ===== BLOCO 2: LEITURA DA JOGADA (Victor) =====
        jogador = "X"
        jogada_valida = False
        # repete a pergunta até o jogador digitar uma casa válida e livre
        while jogada_valida == False:
            entrada = input(nome1 + " (X), digite a casa (ex.: B2): ")
            if entrada == "":
                print("Você não digitou nada! Tente de novo.")
            else:
                achou = False
                # for aninhado que procura a casa digitada:
                # o for de fora (i) percorre as linhas A, B e C e o for de
                # dentro (j) percorre as colunas 1, 2 e 3. Em cada volta o
                # código monta o nome da casa (ex.: B2) e compara com a entrada.
                for i in range(3):
                    for j in range(3):
                        if i == 0:
                            maiuscula = "A"
                            minuscula = "a"
                        elif i == 1:
                            maiuscula = "B"
                            minuscula = "b"
                        else:
                            maiuscula = "C"
                            minuscula = "c"
                        numero = str(j + 1)
                        # aceita maiúscula (B2) e minúscula (b2)
                        if entrada == maiuscula + numero or entrada == minuscula + numero:
                            achou = True
                            linha = i
                            coluna = j
                if achou == False:
                    print("Jogada inválida! Use A, B ou C e 1, 2 ou 3. Ex.: B2.")
                elif tabuleiro[linha][coluna] != " ":
                    # casa já ocupada: mostra qual casa foi digitada e pede outra
                    print("A casa " + entrada + " já está ocupada por " + tabuleiro[linha][coluna] + "! Escolha outra.")
                else:
                    tabuleiro[linha][coluna] = jogador
                    jogada_valida = True
                    
    # ===== BLOCO 1: REGRAS (Kallyson) =====
    elif opcao == "2":
        print("")
        print("================ REGRAS ================")
        print("- O jogo é para dois jogadores. O 1º é o X e o 2º é o O.")
        print("- O X sempre começa.")
        print("- As linhas são as letras A, B e C.")
        print("- As colunas são os números 1, 2 e 3.")
        print("- Na sua vez, digite a letra e o número juntos. Ex.: B2 é o centro.")
        print("- Pode digitar em maiúscula ou minúscula (B2 ou b2).")
        print("- Ganha quem completar uma linha, uma coluna ou uma diagonal.")
        print("- Se as 9 casas ficarem cheias sem vencedor, dá empate.")

    # ===== BLOCO 3: VER PLACAR (MARCOS) =====
    elif opcao == "3":
        print("Em construção.")
    # ===== BLOCO 3: SAIR E ESTATÍSTICA DA SESSÃO - DESAFIO DE LÓGICA (MARCOS) =====
    elif opcao == "4":
        print("")
        print("Obrigado por jogar")
        
   # ===== BLOCO 1: OPÇÃO INVÁLIDA NO MENU (Kallyson) =====
    else:
        print("Opção inválida. Digite 1, 2, 3 ou 4.")