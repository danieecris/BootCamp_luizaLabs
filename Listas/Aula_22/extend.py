linguagem = ['Python', 'JavaScript', 'Java', 'C#']
print(linguagem)

linguagem.extend(['C++', 'Go', 'Rust']) #extend() para adicionar mais elementos a minha lista, ou seja, para adicionar mais linguagens de programação a minha lista.
print(linguagem)

#index
print(linguagem.index('Python'))

print(linguagem.pop())
print(linguagem.pop())
print(linguagem.pop())
print(linguagem)
linguagem.remove('C#') #remove() para remover um elemento da minha lista, ou seja, para remover a linguagem de programação C# da minha lista.
print(linguagem)
linguagem.reverse() #reverse() para inverter a minha lista, ou seja, para inverter a ordem das linguagens de programação na minha lista.
print(linguagem)

#sort

linguagem.sort() #sort() para ordenar a minha lista, ou seja, para ordenar as linguagens de programação na minha lista em ordem alfabética.
print(linguagem)

linguagem.sort(reverse=True) #sort(reverse=True) para ordenar a minha lista em ordem decrescente, ou seja, para ordenar as linguagens de programação na minha lista em ordem alfabética inversa.
print(linguagem)

linguagem.sort(key=lambda x: len(x)) #sort(key=lambda x: len(x)) para ordenar a minha lista pelo tamanho dos elementos, ou seja, para ordenar as linguagens de programação na minha lista pelo tamanho do nome da linguagem.
print(linguagem)

linguagem.sort(key=lambda x: len(x), reverse=True) #sort(key=lambda x: len(x), reverse=True) para ordenar a minha lista pelo tamanho dos elementos em ordem decrescente, ou seja, para ordenar as linguagens de programação na minha lista pelo tamanho do nome da linguagem em ordem decrescente.
print(linguagem)

print(len(linguagem))

