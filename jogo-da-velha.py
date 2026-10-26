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
        # Limpa a matriz com for aninhado:
        # o for de fora (i) percorre as 3 linhas e o for de dentro (j)
        # percorre as 3 colunas de cada linha, deixando cada casa vazia.
        for i in range(3):
            for j in range(3):
                tabuleiro[i][j] = " "

        marca = "X"       # o X sempre começa
        
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

        # ===== BLOCO 2: LEITURA E VALIDAÇÃO DA JOGADA (Victor) =====
        # marca guarda o símbolo de quem joga agora (começa com X)
        marca = "X"

        # O while repete a leitura até a jogada ser válida e livre.
        acao_valida = False
        while not acao_valida:
            acao = input("Vez do " + marca + ", escolha a casa (ex.: B2): ")

            # Procura a jogada digitada entre as 9 casas.
            linha = -1
            coluna = -1

            for i in range(3):
                if i == 0:
                    maiuscula = "A"
                    minuscula = "a"
                elif i == 1:
                    maiuscula = "B"
                    minuscula = "b"
                else:
                    maiuscula = "C"
                    minuscula = "c"

                for j in range(3):
                    if acao == maiuscula + str(j + 1) or acao == minuscula + str(j + 1):
                        linha = i
                        coluna = j

            if acao == "":
                print("Você não digitou nada. Digite uma letra (A a C) e um número (1 a 3).")
            elif linha == -1:
                print("Jogada inválida. Digite a linha (A a C) e a coluna (1 a 3), ex.: B2.")
            elif tabuleiro[linha][coluna] != " ":
                print("A casa " + acao + " já está ocupada por " + tabuleiro[linha][coluna] + "! Escolha outra.")
            else:
                acao_valida = True

        # Registra a jogada usando a variável marca.
        tabuleiro[linha][coluna] = marca
                # ===== BLOCO 2: MARCAR A JOGADA (Victor) =====
        marca = "X"
        acao_valida = False

        while not acao_valida:
            acao = input("Vez do " + marca + ", escolha a casa (ex.: B2): ")

            linha = -1
            coluna = -1

            for i in range(3):
                if i == 0:
                    maiuscula = "A"
                    minuscula = "a"
                elif i == 1:
                    maiuscula = "B"
                    minuscula = "b"
                else:
                    maiuscula = "C"
                    minuscula = "c"

                for j in range(3):
                    if acao == maiuscula + str(j + 1) or acao == minuscula + str(j + 1):
                        linha = i
                        coluna = j

            if acao == "":
                print("Você não digitou nada. Digite uma letra (A a C) e um número (1 a 3).")
            elif linha == -1:
                print("Jogada inválida. Digite a linha (A a C) e a coluna (1 a 3), ex.: B2.")
            elif tabuleiro[linha][coluna] != " ":
                print("A casa " + acao + " já está ocupada por " + tabuleiro[linha][coluna] + "! Escolha outra.")
            else:
                acao_valida = True

        tabuleiro[linha][coluna] = marca
       
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