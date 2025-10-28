nome = "Marcos"
idade = 37
profissao = "Programador"
linguagem = "Python"
saldo = 45.4345

dados = {"nome": "Marcos", "idade": 37}

print("Nome: %s Idade: %d" % (nome, idade))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")