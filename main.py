import verificar_estado_jogo

tabuleiro = [[" "]*3 for _ in range(3)]


def exibir_menu():
    print("----------------------------------")
    print("Seja bem-vindo ao jogo da velha!")
    print("----------------------------------")


def imprimir_tabuleiro():
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j], end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("-----")


def marca_posicao(jogador, linha, coluna):
    if tabuleiro[linha][coluna] != " ":
        print("Posição inválida! Por favor, escolha outra posição.")
        return False
    tabuleiro[linha][coluna] = jogador
    return True


def jogar():
    exibir_menu()
    jogador = "X"
    jogadas = 0
    while jogadas < 9:
        imprimir_tabuleiro()
        print(f"É a vez do jogador {jogador}, em qual posição você deseja jogar? (linha coluna)")
        entrada = input("> ")
        if len(entrada.split()) != 2:
            print(
                "Entrada inválida! Por favor, insira a linha e a coluna separadas por espaço.")
            continue
        try:
            linha, coluna = map(int, entrada.split())
        except ValueError:
            print("Entrada inválida! Certifique-se de inserir apenas números inteiros.")
            continue
        if marca_posicao(jogador, linha, coluna):
            jogadas += 1
            with open('tabuleiro.txt', 'w') as f:
                for i in range(3):
                    for j in range(3):
                        f.write(tabuleiro[i][j])
                        if j < 2:
                            f.write("|")
                    f.write("\n")
                    if i < 2:
                        f.write("-----\n")
            resultado = verificar_estado_jogo.verificar_estado_jogo(
                'tabuleiro.txt') 
            if resultado == jogador:
                print(f"O jogador {jogador} venceu!")
                imprimir_tabuleiro()  
                return  
            elif resultado == 'empate':
                imprimir_tabuleiro()  
                print("\nEmpate! ")
                return  
            jogador = "O" if jogador == "X" else "X"  



if __name__ == "__main__":
    jogar()