numeros = [1, 4, 6, 7, 8, 10, 13, 2, 9, 28, 9, 10, 7, 3, 8]
pares = []
impares = []

for number in numeros:

    if number%2 == 0:
        pares.append(number)
    else:
        impares.append(number)

print("Serie: ", numeros)
print("Pares: ", pares)
print("Impares: ", impares)