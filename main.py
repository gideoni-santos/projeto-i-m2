candidatos = []

while True:
    nome = input("Nome do candidato(a): ")
    entrevista = float(input("Nota da entrevista: "))
    teorico = float(input("Nota do teste teórico: "))
    pratico = float(input("Nota do teste prático: "))
    soft = float(input("Nota da avaliação de Soft Skills: "))

    notas = [nome, [entrevista, teorico, pratico, soft]]
    candidatos.append(notas)
    
    print(candidatos)


    
    