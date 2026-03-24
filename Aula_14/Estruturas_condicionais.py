idade =  17
MAIOR_IDADE = 18
saldo = 500
saque = 200

if idade >= MAIOR_IDADE:
    print("Voce pode tirar a carteira de motorista.")
else:
    print("Voce ainda nao tem idade suficiente para tirar a carteira de motorista.")

if saldo >= saque:
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente para realizar a operacao.")


print("------------------------------------------------------------------------------------------")   

opcao = int(input("\n 1 sacar,\n 2 depositar,\n 3 Extrato \n informe a opcao desejada:  "))    

if opcao == 1:
    valor_saque  = float(input("informe o valor a ser sacado: "))
    if valor_saque <= saldo:
        print("Saque realizado com sucesso!")
    else: 
        print("Saldo insuficiente para realizar a operacao.")

elif opcao == 2:
    valor_depoisto = int(input("informe o valor do deposito: "))
    
    saldo += valor_depoisto
    print(f"Deposito realizado com sucesso! seu saldo atual e de: {saldo}")

elif opcao == 3:             
    print("Imprimindo extrato...")

else:
    print("Opcao invalida, as opcoes validas sao: 1, 2 ou 3")    

