nome = "Daniel"
idade = 23
profissao = "Analista"
linguagem = "python"

pessoa = {
    "nome2": "Daniel", 
    "idade2": 23, 
    "profissao2": "Analista", 
    "linguagem2": "python",
    "saldo": 45.435
    }


#metodo antigo (nao utilizar)
print("Ola meu nome e %s. Eu tenho %d anos, trabalho como %s com a linguagem %s" %(nome, idade, profissao, linguagem),"\n")

#nao muito usada
print("Ola meu nome e {3}. Eu tenho {2} anos, trabalho como {1} com a linguagem {0}".format(nome, idade, profissao,linguagem))

#ideal para uso
print(f"Ola meu nome e {nome}. Eu tenho {idade} anos, trabalho como {profissao} com a linguagem {linguagem}.")


print("nome: {nome2}, idade: {idade2}, profissao: {profissao2}, saldo: {saldo: 10.2f}".format(**pessoa))