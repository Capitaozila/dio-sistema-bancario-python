# Criando um sistema bancario no python
# Autor: Luis Brasil

# Variaveis

saldo = 0
depositos = []
saques = []
limite_por_saque = 500
saques_diarios = 3
saques_feitos = 0

usuarios = []
contas = []
numero_conta = 1

# Funções


def cadastrar_usuario(nome, data_nascimento, cpf, endereco):
    global usuarios
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("CPF já cadastrado.")
            return
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Usuário cadastrado com sucesso.")


def cadastrar_conta(cpf):
    global contas, numero_conta
    for conta in contas:
        if conta['usuario']['cpf'] == cpf:
            print("Usuário já possui uma conta.")
            return
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            contas.append({
                'agencia': '0001',
                'numero_conta': numero_conta,
                'usuario': usuario
            })
            numero_conta += 1
            print("Conta cadastrada com sucesso.")
            return
    print("Usuário não encontrado.")


def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("O valor do depósito deve ser positivo")
        return saldo, extrato
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    print(f"R$ {valor:.2f} depositado com sucesso")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("O valor do saque deve ser positivo")
        return saldo, extrato

    if numero_saques >= limite_saques:
        print("Limite de saques diários atingido")
        return saldo, extrato

    if valor > limite:
        print(f"O valor máximo por saque é de R$ {limite}")
        return saldo, extrato

    if saldo < valor:
        print("Saldo insuficiente")
        return saldo, extrato

    saldo -= valor
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1
    print(f"R$ {valor:.2f} sacado com sucesso")
    return saldo, extrato


def extrato(saldo, *, extrato):
    print("Extrato")
    for operacao in extrato:
        print(operacao)
    print(f"Saldo: R$ {saldo:.2f}")


def listar_contas():
    for conta in contas:
        usuario = conta['usuario']
        print(f"Agência: {conta['agencia']}, Conta: {
              conta['numero_conta']}, Usuário: {usuario['nome']}")


def limpar_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def funcao_concluir_e_passar_o_dia():
    global saques_feitos
    saques_feitos = 0


def main():
    saldo = 0
    extrato = []
    limite_por_saque = 500
    saques_diarios = 3
    saques_feitos = 0

    while True:
        print("[d] - Depositar")
        print("[s] - Sacar")
        print("[e] - Extrato")
        print("[c] - Cadastrar Usuário")
        print("[a] - Cadastrar Conta")
        print("[l] - Listar Contas")
        print("[p] - Passar o Dia")
        print("[q] - Sair")
        opcao = input("Escolha uma opção: ")

        limpar_terminal()
        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            saldo, extrato = sacar(
                saldo=saldo, valor=valor,
                extrato=extrato, limite=limite_por_saque,
                numero_saques=saques_feitos, limite_saques=saques_diarios
            )
        elif opcao == "e":
            extrato(saldo, extrato=extrato)
        elif opcao == "c":
            nome = input("Nome: ")
            data_nascimento = input("Data de Nascimento: ")
            cpf = input("CPF: ")
            endereco = input("Endereço: ")
            cadastrar_usuario(nome, data_nascimento, cpf, endereco)
        elif opcao == "a":
            cpf = input("CPF do usuário: ")
            cadastrar_conta(cpf)
        elif opcao == "l":
            listar_contas()
        elif opcao == "p":
            funcao_concluir_e_passar_o_dia()
            print("Novo dia iniciado. Limite de saques diários resetado.")
        elif opcao == "q":
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
