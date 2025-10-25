saldo = 1000
saque = 250
limite = 200
cheque_especial = True

saldo >= saque and saque <= limite or cheque_especial and saldo >= saque

(saldo >= saque and saque <= limite) or (cheque_especial and saldo >= saque)