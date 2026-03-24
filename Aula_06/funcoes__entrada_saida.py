#input e print

nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo(a)!")


idade  = int(input("Digite sua idade: "))
print(f"Nossa, você tem apenas {idade} anos!")

#Apenas variacoes de como colocar o print, usando o end para colocar um final diferente do \n, e o sep para colocar um separador diferente do espaço entre os argumentos.
print (nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="-")
print(nome, idade, sep="#", end="...\n ")

