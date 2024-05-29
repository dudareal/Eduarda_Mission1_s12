from conversor_medidas import ConversorMedidas

def menu_principal():
    print("/n** Calculadora de conversão de unidades**")
    print("1. Converter Comprimento")
    print("3. Sair")

    opçao = input("Digite a opção desejada:")
    return opçao   

def sair():
    print("Encerrando o programa...")

escolha = menu_principal()

if escolha == '3':
    sair()