menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
número_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "d":
        valor = float(input("Digite o valor a ser depositado:"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Não foi possível executar sua operação, digite novamente o valor desejado")

    elif opção == "s":
        valor = float(input("Digite o valor de sua retirada:"))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite

        saques_excedidos = número_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Você não possui saldo suficiente, refaça a operação")
        
        elif limite_excedido:
            print("Operação falhou! limite de saque excedido")
        
        elif saques_excedidos:
            print("Não foi possível realizar a operação, saques diários excedidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            número_saques += 1
    
        else:
            print("Refaçã a operação")


    elif opção == "e":
        print("\n########## Extrato ##########")
        print("não foram realizadas nenhuma transação." if not extrato else extrato)
        print(f"\nsaldo: R${saldo:.2f}")
        print("##############################")

    elif opção == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada")
    


