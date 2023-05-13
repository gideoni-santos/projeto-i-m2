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
                    cadastroEntrevista = input("Nota da entrevista: ")
                    cadastroTeorico = input("Nota do teste teórico: ")
                    cadastroPratico = input("Nota do teste prático: ")
                    cadastroSoft = input("Nota da avaliação de Soft Skills: ")

                    notas = [nome, [cadastroEntrevista, cadastroTeorico, cadastroPratico, cadastroSoft]]
                    candidatos.append(notas)
                    print("\nUsúario cadastrado com sucesso!")
                    break  
            elif opcaoCadastroCandidatos == "2": #ENTRA NA VERIFICAÇÃO DE CANDIDATOS
                while True:
                    print("\nInsira abaixo as notas dos candidatos para verificar a compatibilidade\n")
                    notaEntrevista = input("Nota da entrevista: ")
                    notaTeorico = input("Nota do teste teórico: ")
                    notaPratico = input("Nota do teste prático: ")
                    notaSoft = input("Nota do teste de Soft Skills: ")
                    
                    notasInseridasVerificacao = [notaEntrevista, notaTeorico, notaPratico, notaSoft]
                    notasVerificacaoCompatibilidade.append(notasInseridasVerificacao)
                    
                    candidatosCompativeis = [] #ADICIONA APENAS OS CANDIDATOS COMPATIVEIS
                    for candidato in candidatos: #FAZ A VERIFICAÇÃO DE COMPATIBILIDADE
                        if (
                            candidato[1] >= notaEntrevista
                            and
                            candidato[2] >= notaTeorico
                            and
                            candidato[3] >= notaPratico
                            and
                            candidato[4] >= notaSoft
                        ):
                            candidatosCompativeis.append(candidato) #ADICIONA APENAS OS CANDIDATOS COMPATÍVEIS NA LISTA 
                    if len(candidatosCompativeis) == 0: #INFORMA SE NÃO HOUVER CANDIDATOS NA LISTA "candidatosCompativeis"
                        print("Não há candidatos compatíveis.")
                    else:
                        print("Os candidatos abaixo são compatíveis: ")
                        for candidato in candidatosCompativeis: 
                            print(
                                f"Nome: {candidato[0]}"
                                f"Entrevista: {candidato[1]}"
                                f"Teórico: {candidato[2]}"
                                f"Prático: {candidato[3]}"
                                f"Soft Skills: {candidato[4]}"
                            )
                    menuOpcao2 = input(
                        "[1] Fazer nova verificação"
                        "[2] Voltar ao menu anterior"
                        "[3] Sair"
                    )
                    
                    if menuOpcao2 == 1:
                        continue
                    elif menuOpcao2 == 2:
                        break
                    elif menuOpcao2 == 3:
                        print("Você saiu do programa")
                        exit()
                    else:
                        print("Por favor insira um opção váida") 
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

    
    