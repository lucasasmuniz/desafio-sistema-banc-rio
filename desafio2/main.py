def menu():
     menu = """

     [d] Depositar
     [s] Sacar
     [e] Extrato
     [u] Cadastrar Usuário
     [v] Ver Lista de Usuários
     [c] Cadastrar Conta Corrente
     [q] Sair

     => """

     return menu


def fazer_deposito(saldo,valor,extrato,/):
     if valor < 0:
          print("Valor inválido!")
     else:
          extrato += f"Depósito: R$ {valor:.2f}\n"
          saldo += valor
     return saldo, extrato

def fazer_saque(*,saldo, valor, extrato, limite, numero_saques,limite_saques):
     if  limite_saques > numero_saques:
          if (valor > saldo):
               print("Saldo insuficiente!")

          elif valor > limite: 
               print("Valor maior que limite de R$ 500 por saque")

          else:
               extrato += "Saque: R$ " + str(valor)+ "\n"
               saldo -= valor
               numero_saques += 1
     
     else: 
          print("Número de saques diários atingido!")
     return saldo, extrato, numero_saques

def extrato_mostrar(saldo,/,*,extrato,):
     if not extrato:
          print("Não foram realizadas movimentações na conta!")
     else:
          print("Extrato:\n" + extrato)
          print(f"Saldo atual da conta:\nR$ {saldo:.2f}")

def criar_usuario(cpf, discionario_usuario):
     if cpf in discionario_usuario:
          print(f"Já existe uma conta com o CPF: {cpf}")
     
     else:
          nome = input("Informe seu nome:\n")
          endereco = input("Informe seu endereço:\n")
          data_nascimento = input("Informe sua data de nascimento:\n")

          discionario_usuario[cpf] = {}

          discionario_usuario[cpf]['nome'] = nome
          discionario_usuario[cpf]['endereco'] = endereco
          discionario_usuario[cpf]['data_nascimento'] = data_nascimento
          print(discionario_usuario)
          return discionario_usuario

def criar_conta_corrente(cpf,discionario_usuario,lista_contas):
     if cpf in discionario_usuario:
          conta_nova = [len(lista_contas)+1, "0001", discionario_usuario[cpf]['nome']]
          lista_contas.append(conta_nova)
     
     return discionario_usuario, lista_contas

def main():

     saldo = 0
     limite = 500
     extrato = ""
     numero_saques = 0
     LIMITE_SAQUES = 3
     discionario_usuario = {}
     lista_contas = []

     while True:

          opcao = input(menu())

          if opcao == "d":
                    valor_para_deposito = float(input("Quanto deseja depositar?\n"))
                    saldo, extrato = fazer_deposito(saldo, valor_para_deposito, extrato)

          elif opcao == "s":
                    valor_para_saque = float(input("Quanto deseja sacar?\n"))
                    saldo, extrato, numero_saques = fazer_saque(saldo = saldo, valor = valor_para_saque, extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

          elif opcao == "e":
                    extrato_mostrar(saldo, extrato = extrato)

          elif opcao == "u":
               cpf = input("Informe seu CPF: \n")
               discionario_usuario = criar_usuario(cpf, discionario_usuario)

          elif opcao == "v":
               print(discionario_usuario)

          elif opcao == "c":
               cpf = input("Informe seu CPF: \n")
               discionario_usuario, lista_contas = criar_conta_corrente(cpf,discionario_usuario, lista_contas)

          elif opcao == "q":
               break

          else:
               print("Operação inválida, por favor selecione novamente a operação desejada.")

main()