numeros = [1, 30, 21, 2, 9, 65, 34]

pares = []
impares = []
#para entender cada numero da minha lista, no caso, para entender saber, qual e par e qual e impar.
for numero in numeros:
    if numero %2 == 0:
        pares.append(numero)
        print(pares)

for numero in numeros:
    if numero %2 != 0:
        impares.append(numero)
        print(impares)        