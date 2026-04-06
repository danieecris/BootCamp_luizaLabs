lista = []

lista.append(1)
lista.append("python")
lista.append([30,40,50])

print(lista)

l2 = lista.copy() #lista.copy() para copiar a minha lista, ou seja, para criar uma nova lista com os mesmos elementos da minha lista original.

print(id(l2), id(lista)) #id() para verificar o endereço de memória da minha lista, ou seja, para verificar se a minha lista original e a minha nova lista são diferentes ou iguais.
#lista.clear() para limpar a minha lista, ou seja, para tirar tudo que tem dentro da minha lista.

l2[1] = "javaScript"

print(lista)
print(l2)


print(lista.count(1)) #lista.count() para contar quantas vezes um elemento aparece na minha lista, ou seja, para contar quantas vezes o numero 1 aparece na minha lista.