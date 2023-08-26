# Definição de variáveis e constantes globais
LIM_NUM_SAQUES_DIARIOS = 3
LIM_SAQUE = 500.00

saldo_conta = 0.00
num_saques_diarios_conta = 0
extrato_conta = []

# Definição de funções

def menu():
    # Exibe o menu e verifica a opção do usuário
    print("Bem vindo ao nosso sistema bancário!".center(100,"=") + f"""
{"Menu opções:".center(100)}
\t1 - Saque
\t2 - Depósito
\t3 - Extrato
\t0 - Sair
""" + "".center(100,"="))
    opcao_menu = int(input("\tDigite a opção desejada: "))
    return opcao_menu

def exit_menu_message():
    # Exibe uma mensagem de encerramento e quebra o laço, encerrando o programa 
    print("\n" + "\tObrigado por utilizar nossos sistemas!".center(100,"=") + "\n")

def verifica_num_saques(*,lim_saques = LIM_NUM_SAQUES_DIARIOS, saques_feitos):
    if(lim_saques == saques_feitos):
        print("\n" + "".center(100,"!") + "\n")
        print("""
\tO números de saques realizados no dia de hoje atingiu o limite máximo permitido
\tde 3 saques diários.
\tPor favor, aguarde até o próximo dia útil ou procure um dos atendentes.
    """)
        print("\n" + "".center(100,"!") + "\n")
        return False
    else:
        return True

def verifica_valor_saque(*, valor_saque, saldo, lim_saque = LIM_SAQUE):
    
    
    if(valor_saque > lim_saque):
        # Verifica se o valor do saque está dentro do limite 
        print("\n" + "".center(100,"!") + "\n")
        print(f"\tO valor informado de saque excede o limite de R${lim_saque: .2f} por saque!")
        print("\n" + "".center(100,"!") + "\n")
        return False
    elif(valor_saque > saldo):
        # Verifica se o valor do saque excede o saldo atual
        print("\n" + "".center(100,"!") + "\n")
        print(f"\tO valor informado de saque excede o saldo atual de R${saldo: .2f}!")
        print("\n" + "".center(100,"!") + "\n")
        return False
    else:
        return True

def saque(*, valor_saque, saldo, extrato = extrato_conta, num_saques):
    if verifica_num_saques(saques_feitos = num_saques):
        if verifica_valor_saque(saldo = saldo,valor_saque=valor_saque):
            if(valor_saque < 0):
                # Ajusta o valor informado para positivo caso seja informado um número negativo
                valor_saque *= -1
            # Atualiza o valor do saldo
            saldo -= valor_saque
            # Adiciona uma referência do saque no extrato
            extrato.append(f"\tSaque      | R${valor_saque: .2f}")
            # Atualiza o número de saques diários
            num_saques += 1
    return saldo,num_saques

def deposito(valor_deposito, saldo, extrato, /):
    # Ajusta o valor informado para positivo caso seja informado um número negativo
    if(valor_deposito < 0):
        valor_deposito *= -1
    # Atualiza o valor do saldo
    saldo += valor_deposito
    # Adiciona uma referência do saque no extrato
    extrato.append(f"\tDepósito   | R${valor_deposito: .2f}")
    return saldo

def exibe_extrato(saldo,/,*,extrato = extrato_conta):
    print("\n" + "Extrato Bancário".center(100,"#"))
    for operacao in extrato:
        print(operacao)
    print(f"\tSaldo atual| R${saldo: .2f}")
    print("".center(100,"#") + "\n")

def warning_message_opcao_invalida():
    print("\n" + "".center(100,"!") + "\n")
    print("\tOpção inválida, selecione uma das opções do menu!")
    print("\n" + "".center(100,"!") + "\n")

while True:
    
    opcao_menu = menu()

    if opcao_menu == 1:
        # Obtém o valor que se deseja sacar
        valor_saque = float(input(f"\n\tQual o valor que deseja sacar? (Limite de R${LIM_SAQUE: .2f}) : R$"))
        saldo_conta,num_saques_diarios_conta = saque(valor_saque=valor_saque,saldo = saldo_conta, num_saques = num_saques_diarios_conta)
    elif opcao_menu == 2:
        # Obtém o valor que se deseja depositar
        valor_deposito = float(input("\tQual o valor que deseja depositar? : R$"))
        saldo_conta = deposito(valor_deposito,saldo_conta,extrato_conta)
    elif opcao_menu == 3:
        # Exibe o extrato no terminal
        exibe_extrato(saldo_conta)
    elif opcao_menu == 0:
        # Exibe uma mensagem informando o encerramento do programa
        exit_menu_message()
        break
    else:
        # Exibe uma mensagem informando que a mensagem não é valida
        warning_message_opcao_invalida()
    
