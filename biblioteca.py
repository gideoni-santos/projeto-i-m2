def sairDoPrograma():
    print("Você saiu do programa.")
    exit()

def linha():
    print("-"*100)
    
def verificaSeListaCandidatosEstaVazia(candidatos): 
#CASO A PESSOA ENTRE EM ALGUMA OPCAO QUE PRECISE DE CANDIDATOS CADASTRADOS, ELE SERÁ RETORNADO AO MENU NATERIOR
    if len(candidatos) == 0:
        linha()
        print("Não há candidatos cadastrados.")
        linha()
        return True
    else:
        return False