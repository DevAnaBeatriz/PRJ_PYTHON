# Função para imprimir o tabuleiro atual
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)


# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or all(tabuleiro[j][i] == jogador for j in range(3)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False


# Função para verificar se o tabuleiro está totalmente preenchido (empate)
def verificar_empate(tabuleiro):
    return all(all(c != ' ' for c in linha) for linha in tabuleiro)


# Função para obter uma jogada válida do jogador
def obter_jogada(tabuleiro, jogador_atual):
    while True:
        try:
            linha = int(input(f"Jogador {jogador_atual}, escolha a linha (0, 1, 2): "))
            coluna = int(input(f"Jogador {jogador_atual}, escolha a coluna (0, 1, 2): "))

            # Verificar se a posição está vazia
            if 0 <= linha < 3 and 0 <= coluna < 3 and tabuleiro[linha][coluna] == ' ':
                return linha, coluna
            else:
                print("Entrada inválida. Escolha uma posição válida.")
        except ValueError:
            print("Entrada inválida. Insira um número.")


# Função principal do jogo
def jogar_jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'

    while True:
        imprimir_tabuleiro(tabuleiro)

        linha, coluna = obter_jogada(tabuleiro, jogador_atual)

        tabuleiro[linha][coluna] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate! O jogo terminou sem vencedores.")
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'


if __name__ == "__main__":
    jogar_jogo_da_velha()
