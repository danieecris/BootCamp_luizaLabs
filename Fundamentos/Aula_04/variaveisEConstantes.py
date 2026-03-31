#Variaveis são espaços na memória do computador onde podemos armazenar valores. Elas são usadas para guardar informações que podem ser alteradas
# durante a execução de um programa. Em Python, você pode criar uma variável simplesmente atribuindo um valor a ela.

age = 24
name = "Daniel Cristian de Oliveira"
print(f"Ola, meu nome é {name} e eu tenho {age} anos de idade.")

#---------------------------------------------------------------
#metodo de atribuição múltipla, onde podemos atribuir valores a várias variáveis em uma única linha. Isso pode ser útil para tornar o código mais conciso e legível.
idade, nome = (30, "Emerson Cardozo")
print(f"Ola, meu nome é {nome} e eu tenho {idade} anos de idade.")
    
INFORMACAO = "Esse valor nao muda"
print(f"Informativo: {INFORMACAO}")

#Para usar uma constante, voce necessita apenas coloca - la em letras maiusculas
#Boas praticas sao colocar em "snake_case", ou seja, com letras minusculas e separadas por underscores. 
#No entanto, isso é apenas uma convenção e não é obrigatório. 
#O importante é que o nome da constante seja claro e descritivo para indicar que seu valor não deve ser alterado durante a execução do programa.
#Colocar nomes sugestivos nas variaveis e constantes é uma boa pratica de programacao, pois ajuda a tornar o codigo mais legivel e facil de entender.

PATH = r"C:\BootCamp_DIO\Aula_04\variaveisEConstantes.py"

DEBUG_MODE = True

BRAZILIAN_STATES = [
    "SP",
    "RJ",
    "MG"
]

AMOUNT = 30.2

print(f"Valor atualizado: {AMOUNT}")
