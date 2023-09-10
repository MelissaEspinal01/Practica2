vocales = ['a', 'e', 'i', 'o', 'u']

frase = input("Escriba una frase: ")
palabra = frase.lower()

for vocal in vocales:
    print(vocal, palabra.count(vocal))