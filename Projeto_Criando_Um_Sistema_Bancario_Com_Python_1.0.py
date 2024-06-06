menu = """
[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair
"""
cont = 1
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))
    cont += 1
    if opcao == 1:
        print("*Sacar")
        print("""
Bem vindo ao sistema de saque eletronico, 
O limite diário de saques é de 3 saques ao dia. 
E o valor maxímo permitido a ser sacado é de R$500
              """)

        if numero_saques < LIMITE_SAQUES:
            if saldo > 0:
                saque = int(input("Quanto você quér sacar?"))
                if saque <= limite:
                    numero_saques += 1
                    saldo -= saque
                    extrato += f"Saque: {saque:.2f}\n"
                    print(f"Você sacou R${saque}, seu saldo atual é de {saldo}")
                else:
                    print("Você excedeu o limite de saque de saque. Tente novamnete!")
            else:
                print("Você não tem saldo suficiente!")
        else:
            print("Você excedeu o limite de saques diário")            

    elif opcao == 2:
        print("*Deposito")
        deposito = int(input("Digite o valor do depósito:"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Despósito:{deposito:.2f}\n"
        else:
            print("Valor invalido. Tente novamente!")

    elif opcao == 3:
        print("Não ouve transações!" if not extrato else extrato)
        print(f"Saldo Atual: {saldo}")

    elif opcao == 0:
        break

    else:
        print("Opcão invalida. Tente novamente!")