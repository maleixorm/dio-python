while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

for num in range(100):
    if num == 15:
        break
    if num == 10:
        continue
    print(num, end=" ")