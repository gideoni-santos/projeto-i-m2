print("\n----------------Programa de compatibilidade de candidatos----------------\n")
candidatos = []

while True:
    opcao = input(
        "[1] Cadastrar candidatos\n"
        "[2] Verificar compatibilidade de candidatos\n"
        "[3] Ver candidatos\n\n"
        "Insira a opção desejada: "
    )
    
    nome = input("Nome do candidato(a): ")
    entrevista = float(input("Nota da entrevista: "))
    teorico = float(input("Nota do teste teórico: "))
    pratico = float(input("Nota do teste prático: "))
    soft = float(input("Nota da avaliação de Soft Skills: "))

    notas = [nome, [entrevista, teorico, pratico, soft]]
    candidatos.append(notas)
    
    print(candidatos)


    
    