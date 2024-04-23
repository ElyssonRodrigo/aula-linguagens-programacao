def verificar_estado_jogo(arquivo):
    tabuleiro = []
    with open(arquivo, 'r') as jogo:
        linhas_arquivo = jogo.readlines()
        tabuleiro = [linha.strip('\n').split('|')
                     for linha in linhas_arquivo[::2]]

    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]

    for coluna in [0, 1, 2]:
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] and tabuleiro[0][coluna] != ' ':
            return tabuleiro[0][coluna]

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] or tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2]:
        if tabuleiro[1][1] != ' ':
            return tabuleiro[1][1]

    if any(' ' in linha for linha in tabuleiro):
        return None  # Jogo ainda está em andamento

    return 'empate'