#Exite a necessidade de converter tipos de dados em Python, especialmente quando você 
#está lidando com diferentes tipos de entrada ou precisa realizar operações específicas.
#A conversão de tipos, também conhecida como "casting", 
#permite que você transforme um valor de um tipo para outro.

preco = 10
print(f"O preço é: {preco} reais")
print(preco/2)
print(preco//2)

preco = float(preco)
print(f"O preço é: {preco} reais")

preco2 = 10.3
print(f"O preço é: {preco2} reais")

preco2 = int(preco2)
print(f"O preço é: {preco2} reais")
print ((str(preco)) + " reais")

idade  ="24"
print(float(idade)+2)

print(type(idade))
print(type(preco))

#print(srt(10.10)+2) nesse caso deve dar erro por nao conseguir somar uma string com um numero int, float...


#Erro na hora conversao, obiviamente a string "24 anos" nao pode ser convertida para um numero, entao o programa vai retornar um erro.



