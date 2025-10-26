def sacar(valor):
    saldo = 500
    if saldo >= valor:
        saldo -= valor
        print("Saque realizado!")
        print(f"O valor remanescente na sua conta é R$ {saldo}")
    else:
        print("Saque Recusado!")
        print("O valor socilitado é maior que o seu saldo.")

sacar(1500)