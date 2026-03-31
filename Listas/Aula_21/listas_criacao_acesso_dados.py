# O acesso aos dados em uma lista é feito por meio de índices, onde o primeiro elemento tem índice 0,
#  o segundo elemento tem índice 1, e assim por diante. Para acessar um elemento específico, basta usar 
# o nome da lista seguido do índice entre colchetes.

carro = ["ferrari", "F8", 4200000, 2020, 2900, "Sao Paulo", True]

frutas=["maca", "laranja", "uva"]

letras = list("python")

numeros = list(range(11))

lista = {
    "nome":"Daniel", 
    "idade": 24, 
    "cidade": "Sao Paulo "
    }

print(carro[2])
print(frutas[1])
print(letras[3:])
print(numeros[5])
print(lista)
print(frutas[-2:-1])

for i in numeros:
    print(i)