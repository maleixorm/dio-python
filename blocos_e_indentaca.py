saldo = 500

def sacar(valor):
    global saldo
    if saldo >= valor:
        saldo -= valor
        print("Saque realizado!")
        print(f"Saldo: R$ {saldo}")
    else:
        print("Saque Recusado!")
        print("O valor socilitado é maior que o seu saldo.")

def depositar(valor):
    global saldo
    if valor > 0:
        saldo += valor
        print("Saldo atualizado após sucesso no depósito")
        print(f"Saldo: R$ {saldo}")
    else:
        print("Depósito Recusado!")
        print("O valor depositado em conta deve ser maior que zero.")

sacar(150)
depositar(300)