saldo = 1000
opcao = -1
while opcao != 0:
    opcao = int(input("1 - Sacar: \n2 - Extrato \n 0 - Sair.\n informe a opcao:"))
    
    if opcao ==1:
        
        saque = int(input("quanto quer sacar: "))
        
        if saldo <= saque:
            print("Seu saldo e menor que a quantidade que voce quer sacar neste momento.")
        
        else:
            print("saque realizado.")    

    elif opcao == 2:
        print("imprimindo seu extrato bancario...")

    elif opcao == 0:    
        print("Processo finalizado")

    else:
        print("opcao nao existe, finalizamos a tarefa")


opcao = -1

while True:
    numero = int(input("informe um numero: "))
    if numero == 10: 
        break

    print(numero)

#Exemplo com "for"

for numero  in range(100):
    
     if numero == 10:
         break
     print(numero)


# A palavra reservada "brack" finaliza o processo
#A palavra reservada "continue" vai pular a execucao, mas vai continuar o processo.