saldo = 1000
saque = 250
limite = 200
cheque_especial = True

exp = saldo >= saque and saque <= limite or cheque_especial and saldo >= saque
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (cheque_especial and saldo >= saque)
print(exp_2)