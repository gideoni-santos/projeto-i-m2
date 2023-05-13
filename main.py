print("\n----------------Programa de compatibilidade de candidatos----------------\n")
candidatos = []
notasVerificacaoCompatibilidade = []

while True:
    opcao = input(
        "[1] Cadastrar candidato\n"
        "[2] Quem desenvolveu?\n"
        "[3] Sair do programa\n\n"
        "Insira a opção desejada: "
    )
    
    if opcao == "1": 
        while True:
            opcaoCadastroCandidatos = input(
                "\n[1] Cadastrar novo candidato\n"
                "[2] Verificar compatibilidade de candidatos\n"
                "[3] Ver candidatos cadastrados\n"
                "[4] Voltar ao menu aterior\n"
                "[5] Encerrar programa\n"
                "\nInsira a opção desejada: "
            )
            
            if opcaoCadastroCandidatos == "1": #CONTINUA O LOOP PARA ADICIONAR NOVOS CANDIDATOS
                while True:
                    nome = input("Nome do candidato(a): ")
                    cadastroEntrevista = float(input("Nota da entrevista: "))
                    cadastroTeorico = float(input("Nota do teste teórico: "))
                    cadastroPratico = float(input("Nota do teste prático: "))
                    cadastroSoft = float(input("Nota da avaliação de Soft Skills: "))

                    notas = [nome, [cadastroEntrevista, cadastroTeorico, cadastroPratico, cadastroSoft]]
                    candidatos.append(notas)
                    print("\nUsúario cadastrado com sucesso!")
                    break  
            elif opcaoCadastroCandidatos == "2": #ENTRA NA VERIFICAÇÃO DE CANDIDATOS
                print("Insira abaixo as notas dos candidatos para verificar a compatibilidade\n")
                notaEntrevista = float(input("Nota da entrevista: "))
                notaTeorico = float(input("Nota do teste teórico: "))
                notaPratico = float(input("Nota do teste prático: "))
                notaSoft = float(input("Nota do teste de Soft Skills: "))
                
                notasInseridasVerificacao = [notaEntrevista, notaTeorico, notaPratico, notaSoft]
                notasVerificacaoCompatibilidade.append(notasInseridasVerificacao)
                
            elif opcaoCadastroCandidatos == "3": #MOSTRA OS CANDIDATOS CADASTRADOS NA LISTA "CANDIDATOS"
                for candidato in candidatos: #MOSTRA A LISTA DE CANDIDATOS MAIS FÁCIL DE LER
                    print(f"\nNome: {candidato[0]}") #BUSCA O INDEX DO NOME DO CANDIDATO "0"
                    print(
                        f"Entrevista - {candidato[1][0]}\n" # BUSCA O INDICE DA SUBLISTA DE ACORDO COM A ORDEM DA NOTA
                        f"Teórico - {candidato[1][1]}\n"
                        f"Prático - {candidato[1][2]}\n"
                        f"Soft Skills - {candidato[1][3]}"
                    )
            elif opcaoCadastroCandidatos == "4": #VOLTA AO MENU ANTERIOR
                break
            elif opcaoCadastroCandidatos == "5": #SAIR DO PROGRAMA
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

    
    