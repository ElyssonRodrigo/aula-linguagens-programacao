def contador_letras(palavra):
    qtd_letras = 0
    for letra in palavra:
        qtd_letras += 1
    return qtd_letras


def contador_palavras(lista):
    qtd_palavras = 0
    for palavra in lista:
        qtd_palavras += 1
    return qtd_palavras


def imprimir_letras(lista):
    for indice, palavra in enumerate(lista, start=1):
        quantidade_letras = contador_letras(palavra)
        print(f"Quantidade de letras na palavra {indice}:{quantidade_letras}")


def imprimir_palavras(lista):
    quantidade_palavra = contador_palavras(lista)
    print(f"Quantidade de palavras na lista é:{quantidade_palavra}")


lista_palavras = ["oi", "tubem", "palavra", "quadro"]

imprimir_palavras(lista_palavras)
imprimir_letras(lista_palavras)
