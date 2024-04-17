from datetime import datetime
with open('hoje.txt','w') as tarefa:
    data_atual = datetime.now().strftime("%d-%m-%y") + "\t"
    tarefa.write("-------------------------------------------\n")
    tarefa.write("Elysson Rodrigo Duarte Martins\n")
    tarefa.write(data_atual)
    tarefa.write('MANAUS-AM\n')
    tarefa.write("24")
    tarefa.write("\t")
    tarefa.write("Cidade de Deus\n")
    tarefa.write("-------------------------------------------\n")
    
    nome_da_disciplina = input('Digite uma disciplina:')
    
    while nome_da_disciplina != "sair":
        nota = input('Digite sua nota para {} (ou "sair" para finalizar): '.format(nome_da_disciplina))
        if nota.lower() == "sair":
            break
        
        tarefa.write(nome_da_disciplina + ',' + nota + '\n')
        nome_da_disciplina = input('Digite uma disciplina (ou "sair" para finalizar): ')