# Jogo da Velha no Terminal

Jogo da Velha para dois jogadores, feito em Python e executado no terminal.

- **Instituição:** UNINASSAU
- **Curso:** Análise e Desenvolvimento de Sistemas
- **Disciplina:** Coding
- **Professor:** M.Sc. Tiago Martins Ribeiro
- **Trabalho:** 2ª Avaliação
- **Equipe:** Kallysson, Victor e Marcos

## O que o jogo faz

- **Dois jogadores:** cada um digita o seu nome. O 1º é sempre o X e o 2º é sempre o O.
- **Tabuleiro em matriz:** desenhado na tela a cada jogada, com as linhas (A, B, C) e as colunas (1, 2, 3).
- **Validação das jogadas:** se o jogador digitar algo errado, o jogo mostra uma mensagem e pede de novo, sem fechar com erro.
- **Vitória e empate automáticos:** o programa percorre o tabuleiro com laços `for` para descobrir o resultado.
- **Placar e estatísticas:** placar acumulado entre as partidas e estatísticas da sessão ao sair (desafio de lógica).

## Como o jogo funciona

```
Nomes dos jogadores → Menu → Partida (jogada → validação → vitória ou empate) → Placar → Jogar novamente ou Sair
```

O menu tem 4 opções: **1. Jogar**, **2. Ver regras**, **3. Ver placar** e **4. Sair** (mostra as estatísticas da sessão).

## Como jogar

O tabuleiro tem 9 casas. As **linhas** são as letras **A, B e C** e as **colunas** são os números **1, 2 e 3**:

```
      1   2   3
    +---+---+---+
  A |   |   |   |
    +---+---+---+
  B |   |   |   |
    +---+---+---+
  C |   |   |   |
    +---+---+---+
```

- Na sua vez, digite a **letra da linha e o número da coluna juntos**. Exemplos: `A1` é o canto de cima à esquerda, `B2` é o centro e `C3` é o canto de baixo à direita.
- Pode digitar a letra maiúscula ou minúscula: `b2` e `B2` são a mesma casa.
- Ganha quem completar primeiro uma **linha, uma coluna ou uma diagonal** com o seu símbolo.
- Se as 9 casas ficarem cheias e ninguém ganhar, a partida termina em **empate**.

### Quando o jogador digita algo errado

O jogo pede a jogada de novo se for digitado:

- nada (campo vazio);
- letra ou símbolo que não forma uma casa (ex.: `X`, `#`, `A`);
- linha ou coluna que não existe (ex.: `D1`, `A5`);
- uma casa que já está ocupada.

## Como rodar

1. Instale o Python 3 (https://www.python.org/downloads/).
2. Baixe o repositório: `git clone https://github.com/Misterdssa21a/jogo-da-velha-python`
3. Entre na pasta do projeto e rode: `python jogo_da_velha.py`

## Desafio de lógica

**Estatísticas da sessão** (nível básico). Ao escolher "Sair", o jogo mostra:

- o total de partidas;
- as vitórias de cada jogador e os empates;
- a porcentagem de vitórias de cada jogador (número decimal, ex.: 66.7%);
- a maior sequência de vitórias seguidas de cada jogador.

Onde está no código: *(preencher com o bloco ou as linhas quando o código estiver pronto)*.

## Tecnologias

- Python 3, usando só o conteúdo visto em aula: variáveis e tipos (int, str, bool e float), operadores, `if/elif/else`, `while`, `for` e `range()`, matriz (lista de listas) e as funções `print()`, `input()`, `int()`, `float()` e `str()`.
- Não foram usados: funções criadas pelo aluno, dicionários, tuplas, conjuntos, listas de uma dimensão, métodos de lista e de texto, list comprehension, bibliotecas, `try/except` e classes.
- Git e GitHub para o versionamento.

## Equipe

| Integrante | Responsabilidades |
|---|---|
| Kallysson | Matriz 3x3 (escrita linha por linha), nomes dos jogadores, exibição do tabuleiro com `for` aninhado, menu com `while`, regras e "jogar novamente" (limpa a matriz com `for` aninhado) |
| Victor | Leitura e validação da jogada, casa livre, marcação da jogada, troca de jogador e verificação de vitória com laços (linhas, colunas e diagonais) |
| Marcos | Sequência de jogadas da partida (`while`), empate, placar acumulado, estatísticas da sessão (desafio) e tela de saída |

## Documentação

- Guia de GitHub para o trio: [guia-github.md](guia-github.md)
- Vídeo explicativo (YouTube, não listado): *(colocar o link)*
- Relatório técnico: enviado em PDF pelo formulário.
