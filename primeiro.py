menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor_para_deposito = float(input("Quanto deseja depositar?\n"))
        if valor_para_deposito < 0:
            print("Valor inválido!")
        else:
            extrato += f"Depósito: R$ {valor_para_deposito:.2f}\n"
            saldo += valor_para_deposito

    elif opcao == "s":
        if  LIMITE_SAQUES > numero_saques:
            valor_para_saque = float(input("Quanto deseja sacar?\n"))

            if (valor_para_saque > saldo):
                print("Saldo insuficiente!")

            elif valor_para_saque > 500: 
                print("Valor maior que limite de R$ 500 por saque")

            else:
                extrato += "Saque: R$ " + str(valor_para_saque)+ "\n"
                saldo -= valor_para_saque
                numero_saques += 1
            

        else: 
            print("Número de saques diários atingido!")

    elif opcao == "e":
        if not extrato:
            print("Não foram realizadas movimentações na conta!")
        else:
            print("Extrato:\n" + extrato)
            print(f"Saldo atual da conta:\nR$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")