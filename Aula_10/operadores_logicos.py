saldo = 1000
saque = 200
limite = 100
conta_especial =True

print(True and True)
print(True and False)
print(False or True)
print(True or True)

print("-----------------------------------")

#Operadores logicos servem para fazer comparações entre expressões, retornando um valor booleano (True ou False)
print(saldo >= saque and saque <= limite)
print(saldo >= saque or saque <= limite)

print("-----------------------------------")

contatos_emersgencia = []
print(not 1000 > 1500)
print(not contatos_emersgencia)
print(not "saque 1500;")
print(not "")

print("-----------------------------------")

tem_saldo = saldo >= saque and saque <= limite 
da_certo = conta_especial and saldo >= saque

print(tem_saldo or da_certo)
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

 

