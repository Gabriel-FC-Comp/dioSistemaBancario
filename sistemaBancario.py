# Definição de variáveis e constantes
LIM_NUM_SAQUES_DIARIOS = 3
LIM_SAQUE = 500.00

saldo = 0.00
num_saques_diarios = 0
extrato = []

while True:
    
    # Exibe o menu e verifica a opção do usuário
    print("Bem vindo ao nosso sistema bancário!".center(100,"=") + f"""
{"Menu opções:".center(100)}
\t1 - Saque
\t2 - Depósito
\t3 - Extrato
\t0 - Sair
""" + "".center(100,"="))
    opcao_menu = int(input("\tDigite a opção desejada: "))
    
    # Verifica a opção escolhida pelo usuário
    if(opcao_menu == 0):# 0 - Sair
        # Exibe uma mensagem de encerramento e quebra o laço, encerrando o programa 
        print("\n" + "\tObrigado por utilizar nossos sistemas!".center(100,"=") + "\n")
        break;
    
    elif(opcao_menu == 1): # 1 - Saque
        # Verifica se a quantidade de saques feitos já atingiu o limite diário permitido
        if(LIM_NUM_SAQUES_DIARIOS == num_saques_diarios):
            print("\n" + "".center(100,"!") + "\n")
            print("""
\tO números de saques realizados no dia de hoje atingiu o limite máximo permitido
\tde 3 saques diários.
\tPor favor, aguarde até o próximo dia útil ou procure um dos atendentes.
    """)
            print("\n" + "".center(100,"!") + "\n")
            continue
        else:
            # Obtém o valor que se deseja sacar
            valor_saque = float(input("\n\tQual o valor que deseja sacar? (Limite de R$1000,00) : R$"))
            
            if(valor_saque > LIM_SAQUE):
                # Verifica se o valor do saque está dentro do limite 
                print("\n" + "".center(100,"!") + "\n")
                print(f"\tO valor informado de saque excede o limite de R${LIM_SAQUE: .2f} por saque!")
                print("\n" + "".center(100,"!") + "\n")
                continue
            elif(valor_saque > saldo):
                # Verifica se o valor do saque excede o saldo atual
                print("\n" + "".center(100,"!") + "\n")
                print(f"\tO valor informado de saque excede o saldo atual de R${saldo: .2f}!")
                print("\n" + "".center(100,"!") + "\n")
                continue
            elif(valor_saque < 0):
                # Ajusta o valor informado para positivo caso seja informado um número negativo
                valor_saque *= -1
                continue
            # Atualiza o valor do saldo
            saldo -= valor_saque
            # Adiciona uma referência do saque no extrato
            extrato.append(f"\tSaque      | R${valor_saque: .2f}")
            # Atualiza o número de saques diários
            num_saques_diarios += 1
            
    elif(opcao_menu == 2): # 2- Deposito
        # Obtém o valor que se deseja depositar
        valor_deposito = float(input("\tQual o valor que deseja depositar? : R$"))
        # Ajusta o valor informado para positivo caso seja informado um número negativo
        if(valor_deposito < 0):
            valor_deposito *= -1
        # Atualiza o valor do saldo
        saldo += valor_deposito
        # Adiciona uma referência do saque no extrato
        extrato.append(f"\tDepósito   | R${valor_deposito: .2f}")
    
    elif(opcao_menu == 3): # 3 - Extrato
        print("\n" + "Extrato Bancário".center(100,"#"))
        for operacao in extrato:
            print(operacao)
        print(f"\tSaldo atual| R${saldo: .2f}")
        print("".center(100,"#") + "\n")
    else:
        print("\n" + "".center(100,"!") + "\n")
        print("\tOpção inválida, selecione uma das opções do menu!")
        print("\n" + "".center(100,"!") + "\n")
        continue

