LIMITE_SAQUES = 3
AGENCIA = "0001"


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        return saldo, extrato, "Operação falhou! O valor informado é inválido."

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        return saldo, extrato, "Operação falhou! Você não tem saldo suficiente."
    elif excedeu_limite:
        return saldo, extrato, "Operação falhou! O valor do saque excede o limite."
    elif excedeu_saques:
        return saldo, extrato, "Operação falhou! Número máximo de saques excedido."
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, f"Saque de R$ {valor:.2f} realizado com sucesso!"


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return saldo, extrato, f"Depósito de R$ {valor:.2f} realizado com sucesso!"
    else:
        return saldo, extrato, "Operação falhou! O valor informado é inválido."

def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return "Erro: Usuário já cadastrado com este CPF."

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    return "Usuário criado com sucesso!"

def criar_conta_corrente(agencia, numero_conta, usuarios, cpf):
    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        return "Erro: Usuário não encontrado."

    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    }
    return nova_conta

def listar_contas(contas):
    if not contas:
        print("Não há contas cadastradas.")
    else:
        for conta in contas:
            print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, Titular: {conta['usuario']['nome']}")

def menu_principal():
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    proxima_conta = 1

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar Usuário
    [c] Criar Conta Corrente
    [l] Listar Contas
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato, mensagem = depositar(saldo, valor, extrato)
            print(mensagem)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, mensagem = sacar(
                saldo=saldo, valor=valor, extrato=extrato, limite=limite, 
                numero_saques=numero_saques, limite_saques=LIMITE_SAQUES
            )
            print(mensagem)

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            nome = input("Nome: ")
            data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
            cpf = input("CPF (apenas números): ")
            endereco = input("Endereço (logradouro, número, bairro, cidade/sigla estado): ")
            mensagem = criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)
            print(mensagem)

        elif opcao == "c":
            cpf = input("Informe o CPF do usuário: ")
            nova_conta = criar_conta_corrente(AGENCIA, proxima_conta, usuarios, cpf)
            if isinstance(nova_conta, dict):
                contas.append(nova_conta)
                proxima_conta += 1
                print(f"Conta criada com sucesso! Número da conta: {nova_conta['numero_conta']}")
            else:
                print(nova_conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

menu_principal()
