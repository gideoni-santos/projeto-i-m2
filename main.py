def sairDoPrograma():
    print("Você saiu do programa.")
    exit()

def linha():
    print("-"*100)

print("\n----------------Programa de compatibilidade de candidatos----------------")

candidatos = [] #LISTA DE CANDIDATOS CADASTRADOS
notasVerificacaoCompatibilidade = [] #LISTA DAS NOTAS INPUTADAS PARA VERIFICAÇÃO DE COMPATIBILIDADE
candidatosCompativeis = [] #ADICIONA APENAS OS CANDIDATOS COMPATIVEIS

while True: #MENU INICIAL
    opcao = input(
        "\n[1] Área de candidatos\n"
        "[2] Quem desenvolveu?\n"
        "[3] Sair do programa\n"
        "Insira a opção desejada: "
    )
    
    if opcao == "1": #ENTRA NA AREA DE CANDIDATOS
        while True:
            opcaoCadastroCandidatos = input(
                "\n[1] Cadastrar candidato\n"
                "[2] Verificar compatibilidade de candidatos\n"
                "[3] Ver candidatos cadastrados\n"
                "[4] Voltar ao menu aterior\n"
                "[5] Encerrar programa\n"
                "Insira a opção desejada: "
            )
            
            if opcaoCadastroCandidatos == "1": #LOOP PARA ADICIONAR NOVOS CANDIDATOS
                while True:
                    nome = input("\nNome do candidato(a): ")
                    cadastroEntrevista = float(input("Nota da entrevista: "))
                    cadastroTeorico = float(input("Nota do teste teórico: "))
                    cadastroPratico = float(input("Nota do teste prático: "))
                    cadastroSoft = float(input("Nota da avaliação de Soft Skills: "))

                    notas = [nome, [cadastroEntrevista, cadastroTeorico, cadastroPratico, cadastroSoft]]
                    candidatos.append(notas)
                    linha()
                    print("Usúario cadastrado com sucesso!")
                    linha()
                    break  
            elif opcaoCadastroCandidatos == "2": #ENTRA NA VERIFICAÇÃO DE CANDIDATOS
                while True:
                    print("\nInsira abaixo as notas dos candidatos para verificar a compatibilidade\n")
                    notaEntrevista = float(input("Nota da entrevista: "))
                    notaTeorico = float(input("Nota do teste teórico: "))
                    notaPratico = float(input("Nota do teste prático: "))
                    notaSoft = float(input("Nota do teste de Soft Skills: "))
                    
                    notasInseridasVerificacao = [notaEntrevista, notaTeorico, notaPratico, notaSoft]
                    notasVerificacaoCompatibilidade.append(notasInseridasVerificacao)
                    
                    for candidato in candidatos: #FAZ A VERIFICAÇÃO DE COMPATIBILIDADE
                        if (
                            candidato[1][0] >= notaEntrevista
                            and
                            candidato[1][1] >= notaTeorico
                            and
                            candidato[1][2] >= notaPratico
                            and
                            candidato[1][3] >= notaSoft
                        ):
                            candidatosCompativeis.append(candidato) #ADICIONA APENAS OS CANDIDATOS COMPATÍVEIS NA LISTA 
                    if len(candidatosCompativeis) == 0: #INFORMA SE NÃO HOUVER CANDIDATOS NA LISTA "candidatosCompativeis"
                        linha()
                        print("\nNão há candidatos compatíveis.")
                        linha()
                    else:
                        print("\nOs candidatos abaixo são compatíveis: \n") #MOSTRA OS CANDIDATOS COMPATÍVEIS
                        for candidato in candidatosCompativeis: 
                            print(
                                f"Nome: {candidato[0]}\n"
                                f"Entrevista: {candidato[1][0]}\n"
                                f"Teórico: {candidato[1][1]}\n"
                                f"Prático: {candidato[1][2]}\n"
                                f"Soft Skills: {candidato[1][3]}\n"
                            )
                    linha()
                    menuOpcao2 = input(
                        "\n[1] Fazer nova verificação\n"
                        "[2] Voltar ao menu anterior\n"
                        "[3] Sair\n"
                        "Insira uma opção: "
                    )
                    if menuOpcao2 == "1": #NOVA VERIFICAÇÃO
                        continue
                    elif menuOpcao2 == "2": #VOLTA AO MENU ANTERIOR
                        break
                    elif menuOpcao2 == "3": #SAIR DO PROGRAMA
                        sairDoPrograma()
                    else: #VERIFICA SE A OPÇÃO É VÁLIDA
                        print("Por favor insira um opção válida") 
                        
            elif opcaoCadastroCandidatos == "3": #MOSTRA OS CANDIDATOS CADASTRADOS NA LISTA "CANDIDATOS"
                for candidato in candidatos: #MOSTRA A LISTA DE CANDIDATOS MAIS FÁCIL DE LER
                    linha()
                    print(f"\nNome: {candidato[0]}") #BUSCA O INDEX DO NOME DO CANDIDATO "0"
                    print(
                        f"Entrevista - {candidato[1][0]}\n" # BUSCA O INDICE DA SUBLISTA DE ACORDO COM A ORDEM DA NOTA
                        f"Teórico - {candidato[1][1]}\n"
                        f"Prático - {candidato[1][2]}\n"
                        f"Soft Skills - {candidato[1][3]}"
                    )
                linha()
            elif opcaoCadastroCandidatos == "4": #VOLTA AO MENU ANTERIOR
                break
            elif opcaoCadastroCandidatos == "5": #SAIR DO PROGRAMA
                sairDoPrograma()
            else: #VERIFICA SE A OPÇÃO É VÁLIDA
                print("Por favor insira um opção váida")
            
    elif opcao == "2": #QUEM DESENVOLVEU
        print("-"*100)
        print(
            "\nDesenvolvido por Gideoni Santos\n"
            "Estudante de Data Analytics para o projeto indívidual do Modúlo 2 do curso de Data Analytics da Resilia\n"
        )
        print("-"*100)
        continue
    elif opcao == "3": #SAI DO PROGRAMA
        sairDoPrograma()
    else: #VERIFICA SE A OPÇÃO É VÁLIDA
        print("Por favor Insira uma opção válida")

    
    