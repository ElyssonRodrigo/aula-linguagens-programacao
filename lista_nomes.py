from datetime import datetime
import re

data_atual = datetime.now()
busca = input('Digite um nome da lista:').strip().lower()

with open('lista_de_alunos.csv', 'r') as planilha:
    lista_linhas = planilha.readlines()
    for linha in lista_linhas:
        nome, data_de_nascimento, matricula = linha.strip("\n").split(',')
        nome_sem_numeros = re.sub(r'\d+', '', nome).strip().lower()
        if nome_sem_numeros == busca:
            data_de_nascimento = datetime.strptime(
                data_de_nascimento, '%d/%m/%Y')

            idade = data_atual.year - data_de_nascimento.year
            if (data_atual.month, data_atual.day) < (data_de_nascimento.month, data_de_nascimento.day):
                idade -= 1
            print(nome + ' > ' + data_de_nascimento.strftime('%d/%m/%Y') +
                  ' > Idade: ' + str(idade))
