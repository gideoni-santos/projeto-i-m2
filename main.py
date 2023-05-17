def sairDoPrograma():
    print("Você saiu do programa.")
    exit()

def linha():
    print("-"*100)
    
def verificaSeListaCandidatosEstaVazia(): 
#CASO A PESSOA ENTRE EM ALGUMA OPCAO QUE PRECISE DE CANDIDATOS CADASTRADOS, ELE SERÁ RETORNADO AO MENU NATERIOR
    if len(candidatos) == 0:
        linha()
        print("Não há candidatos cadastrados.")
        linha()
        return True
    else:
        return False
    

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
                "[3] Remover candidato\n"
                "[4] Ver candidatos cadastrados\n"
                "[5] Voltar ao menu aterior\n"
                "[6] Encerrar programa\n"
                "Insira a opção desejada: "
            )
            
            if opcaoCadastroCandidatos == "1": #LOOP PARA ADICIONAR NOVOS CANDIDATOS
                while True:
                    nome = input("\nNome do candidato(a): ").title()
                    cadastroEntrevista = float(input("Nota da entrevista: "))
                    cadastroTeorico = float(input("Nota do teste teórico: "))
                    cadastroPratico = float(input("Nota do teste prático: "))
                    cadastroSoft = float(input("Nota da avaliação de Soft Skills: "))

                    notas = [nome, [cadastroEntrevista, cadastroTeorico, cadastroPratico, cadastroSoft]]
                    candidatos.append(notas)
                    linha()
                    print("Candidato cadastrado com sucesso!")
                    linha()
                    break  
            elif opcaoCadastroCandidatos == "2": #ENTRA NA VERIFICAÇÃO DE CANDIDATOS
                if verificaSeListaCandidatosEstaVazia():
                    continue
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
                                   
            elif opcaoCadastroCandidatos == "3": #OPCAO DE REMOVER CANDIDATOS
                if verificaSeListaCandidatosEstaVazia():
                    continue
                while True:
                    opcaoRemoverCandidato = input(
                        "\n[1] Remover por nome\n"
                        "[2] Apagar todos\n"
                        "[3] Voltar ao menu anterior\n"
                        "[4] Sair do programa\n"
                        "Insira a opção desejada: "
                    )
                    if opcaoRemoverCandidato == "1": #REMOVER PELO NOME DO CANDIDATO
                        removerCandidato = input("Insira o nome do candidato(a) que você quer remover: ").title()
                        candidato_removido = False #É USADA PARA DEFINIR SE O CANDIDATO FOI REMOVIDO OU NÃO
                        for candidato in candidatos[:]: #SLICING - CRIA UMA COPIA DE 'candidatos'
                            if removerCandidato == candidato[0]: #INDICE 0 REFERE-SE AO NOME DO CANDIDATOS
                                candidatos.remove(candidato) #REMOVE O CANDIDATO DA LISTA 'candidatos'
                                candidatosCompativeis.remove(candidato)
                                candidato_removido = True #SE A CONDICAO FOR VERDADEIRA 
                        if candidato_removido: #SE O CODIGO ACIMA DEFINIR A VARIAVEL COMO TRUE O CANDIDATO FOI REMOVIDO
                            linha()
                            print("Candidato removido com sucesso!")
                            linha()
                        else:
                            linha()
                            print(f"Não existe nenhum candidato {removerCandidato} cadastrado.")
                            linha()
                            continue
                    elif opcaoRemoverCandidato == "2": #APAGA TODA A LISTA 'candidatos' E 'candidatosCompativeis'
                        confirmacaoApagarTudo = input("Tem certeza que deseja apagar todos os candidatos cadastrados? (S/N)").upper()
                        if confirmacaoApagarTudo == "S":
                            candidatos.clear()
                            candidatosCompativeis.clear()
                            linha()
                            print("Todos os registros de candidatos foram apagados.")
                            linha()
                            break
                        elif confirmacaoApagarTudo == "N":
                            linha()
                            print("Ação cancelada")
                            linha()
                            break
                        else:
                            linha()
                            print("Por favor insira um opção válida")
                            linha()
                            continue
                    elif opcaoRemoverCandidato == "3": #VOLTA AO MENU ANTERIOR
                        break
                    elif opcaoRemoverCandidato == "4": # SAIR DO PROGRAMA
                        sairDoPrograma()
                    else: #VERIFICA SE OPÇÃO É VÁLIDA
                        linha()
                        print("Por favor insira um opção váida")
                        linha()
                        
            elif opcaoCadastroCandidatos == "4": #MOSTRA OS CANDIDATOS CADASTRADOS NA LISTA "CANDIDATOS"
                if verificaSeListaCandidatosEstaVazia():
                    continue
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
            elif opcaoCadastroCandidatos == "5": #VOLTA AO MENU ANTERIOR
                break
            elif opcaoCadastroCandidatos == "6": #SAIR DO PROGRAMA
                sairDoPrograma()
            else: #VERIFICA SE A OPÇÃO É VÁLIDA
                linha()
                print("Por favor insira um opção váida")
                linha()
            
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