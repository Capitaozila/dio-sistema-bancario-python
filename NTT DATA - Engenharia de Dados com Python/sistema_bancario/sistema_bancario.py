# Criando um sistema bancario no python
# Autor: Luis Brasil

# Operação de depósito
# Deve ser possível depositar valores positivos para a minha conta bancária.
# A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos
# nos preocupar em identificar qual é o número da agência e conta bancária.
# Todos os depósitos devem ser armazenados em uma variável e
# exibidos na operação de extrato.

# Operação de saque
# O sistema deve permitir realizar 3 saques diários com limite máximo
# de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta,
# o sistema deve exibir uma mensagem informando que não será possível
# sacar o dinheiro por falta de saldo.
# Todos os saques devem ser armazenados em uma variável
# e exibidos na operação de extrato.

# Operação de extrato
# Essa operação deve listar todos os depósitos e saques realizados na conta.
# No fim da listagem deve ser exibido o saldo atual da conta.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
# 1500.45 = R$ 1500.45

# Não posso usar blibliotecas e nem POO ainda

# Variaveis

saldo = 0
depositos = []
saques = []
limite_por_saque = 500
saques_diarios = 3
saques_feitos = 0


# Funções

def depositar(valor):
    global saldo
    if valor <= 0:
        print("O valor do depósito deve ser positivo")
        return
    saldo += valor
    depositos.append(valor)
    print(f"R$ {valor:.2f} depositado com sucesso")


def sacar(valor):
    global saldo
    global saques_feitos

    if valor <= 0:
        print("O valor do saque deve ser positivo")
        return

    if saques_feitos >= saques_diarios:
        print("Limite de saques diários atingido")
        return

    if valor > limite_por_saque:
        print(f"O valor máximo por saque é de R$ {limite_por_saque}")
        return

    if saldo < valor:
        print("Saldo insuficiente")
        return

    saldo -= valor
    saques.append(valor)
    saques_feitos += 1
    print(f"R$ {valor:.2f} sacado com sucesso")


def extrato():
    print("Extrato")
    print("Depósitos")
    for deposito in depositos:
        print(f"R$ {deposito:.2f}")
    print("Saques")
    for saque in saques:
        print(f"R$ {saque:.2f}")
    print(f"Saldo: R$ {saldo:.2f}")


def limpar_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def funcao_concluir_e_passar_o_dia():
    global saques_feitos
    saques_feitos = 0


def main():
    while True:
        print("[d] - Depositar")
        print("[s] - Sacar")
        print("[e] - Extrato")
        print("[p] - Passar o Dia")
        print("[q] - Sair")
        opcao = input("Escolha uma opção: ")

        limpar_terminal()
        if opcao == "d":
            valor = float(input("Digite o valor a ser depositado: "))
            depositar(valor)
        elif opcao == "s":
            valor = float(input("Digite o valor a ser sacado: "))
            sacar(valor)
        elif opcao == "e":
            extrato()
        elif opcao == "p":
            funcao_concluir_e_passar_o_dia()
            print("Novo dia iniciado. Limite de saques diários resetado.")
        elif opcao == "q":
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
