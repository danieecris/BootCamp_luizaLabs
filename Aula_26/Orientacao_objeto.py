#Conceito de casse e objeto 
#Classe é um molde para criar objetos, é uma estrutura que define as características e comportamentos de um objeto.
#Objeto é uma instância de uma classe, é uma entidade concreta que possui as características e comportamentos definidos pela classe.
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def latir(latir):
        print("Au Au!")
        
    def dormir(self):
        self.acordado = False    
        print("Zzzzz...")

cao_1 = Cachorro("Rex", "Marrom", True)
cao_2 = Cachorro("Pacoca", "branco", True)

print(cao_1.latir())
print(cao_2.latir())
print(cao_1.dormir())