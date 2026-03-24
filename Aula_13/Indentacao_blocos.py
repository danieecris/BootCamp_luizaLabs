# A indentação é um recurso da linguagem Python para definir blocos de código.
# Em outras linguagens, os blocos de código são definidos por chaves ou palavras-chave específicas, mas em Python, 
# a indentação é usada para indicar quais linhas de código pertencem a um determinado bloco.

def sacar (valor: float, saldo: float) -> None:
    if valor >= saldo:
        print("Saque realizado com sucesso!")
    else:     
        print("Saldo insuficiente para realizar a operacao.")
        
    return "fim da operacao, obrigado por ser nosso cliente!"    

print(sacar(1500, 200))


def sacar (valor: float):
    saldo = 1000
    saldo += valor
    print(f"seu saldo atual e de: {saldo}")
    return "fim da operacao, obrigado por ser nosso cliente!"

print(sacar(500))    
