conta_corrente = False
conta_salario = True

saldo = 15000
saque = 15500
cheque_especial = 500

if conta_corrente:

    if saldo >= saque: 
        print("Saque realizado com sucesso!")

    elif saque <= (saldo +cheque_especial):
        print("Saque realizado, voce usou cheque especial para fazer este saque.")

    else:
        print(f"Saldo insuficiente para realizar a operacao. Seu saldo e de: {saldo}")      

if conta_salario:

    if saldo >= saque: 
        print("Saque realizado com sucesso!")

    else:
        print(f"Saldo insuficiente para realizar a operacao. Seu saldo e de: {saldo}")    

else:
    print("Tipo de conta invalida, as opcoes validas sao: Conta corrente ou conta salario")
