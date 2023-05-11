print("\n----------------Programa de compatibilidade de candidatos----------------\n")
candidatos = []

while True:
    opcao = input(
        "[1] Cadastrar candidato\n"
        "[2] Quem desenvolveu?\n"
        "[3] Sair do programa\n\n"
        "Insira a opção desejada: "
    )
    
    if opcao == "1": 
        while True:
            opcaoCandidatos = input(
                "\n[1] Cadastrar novo candidato\n"
                "[2] Verificar compatibilidade de candidatos\n"
                "[3] Ver candidatos\n"
                "[4] Voltar ao menu aterior\n"
                "[5] Encerrar programa\n"
                "\nInsira a opção desejada: "
            )
            
            if opcaoCandidatos == "1": #CONTINUA O LOOP PARA ADICIONAR NOVOS CANDIDATOS
                while True:
                    nome = input("Nome do candidato(a): ")
                    entrevista = float(input("Nota da entrevista: "))
                    teorico = float(input("Nota do teste teórico: "))
                    pratico = float(input("Nota do teste prático: "))
                    soft = float(input("Nota da avaliação de Soft Skills: "))

                    notas = [nome, [entrevista, teorico, pratico, soft]]
                    candidatos.append(notas)
                    print("\nUsúario cadastrado com sucesso!")
                    
            elif opcaoCandidatos == "2": #ENTRA NA VERIFICAÇÃO DE CANDIDATOS
                print("opcao2")
            elif opcaoCandidatos == "3": #MOSTRA OS CANDIDATOS CADASTRADOS NA LISTA "CANDIDATOS"
                print(candidatos)
            elif opcaoCandidatos == "4": #VOLTA AO MENU ANTERIOR
                break
            elif opcaoCandidatos == "5": #SAIR DO PROGRAMA
                print("Você saiu do programa")
                exit()
            else: #VERIFICA SE A OPÇÃO É VÁLIDA
                print("Por favor insira um opção váida")
            
    elif opcao == "2": 
        print("opcao2")
        
    elif opcao == "3": 
        print("opcao3")
        
    else:
        print("Por favor Insira uma opção válida")
    
        

    
    