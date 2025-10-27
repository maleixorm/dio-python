texto = input("Informe seu texto: ")
VOGAIS = "AEIOU"

# exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # Adiciona uma quebra de linha
    print("Executa no final do laço.")


# exemplo utilizando a função built-in range
for numero in range(1, 11):
    print(numero, end=" ")

print() # Adiciona uma quebra de linha

for numero2 in range(0, 51, 5):
    print(numero2, end=" ")
