print('Exercício 1')
print('Crie uma lista vazia chamada numeros e adicione os números de 1 a 5 usando append().')

# abacaxi = ['maria','joao','lcuas']

# abacaxi[0]='marcos'

# funçoes que adicionam append , insert

# funçeos que deletam ,del ,pop , remove

numeros=[]

numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)
print(numeros)

print('---------------------------------')
print('Exercício 2')
print('Dada a lista [10, 20, 30], insira o número 15 na posição 1 usando insert().')

lista=[10,20,30]

lista.insert(1, 15)
print(lista) 

print('---------------------------------')
print('Exercício 3')
print("Dada a lista ['a', 'b', 'c'], modifique o segundo elemento para 'x'.")

letras = ['a', 'b', 'c']

letras.insert(2, 'x')
print(letras)

print('---------------------------------')
print('Exercício 4')
print('Dada a lista [5, 10, 15, 20], remova o elemento na posição 2 usando del.')

numero=[5,10,15,20]
del numero[2]
print(numero)

print('---------------------------------')
print('Exercício 5')
print("Dada a lista ['maçã', 'banana', 'laranja'], remova 'banana' usando remove().")

frutas=['maçã','banana','laranja']
frutas.remove('banana')

print(frutas)

print('---------------------------------')
print('Exercício 6')
print('Dada a lista [100, 200, 300, 400], remova e retorne o último elemento usando pop().')
grandesnumeros=[100,200,300,400]
deletados=grandesnumeros.pop(3)

print('Número deletado', deletados)

print('---------------------------------')
print('Exercício 7')
print("Dada a lista ('python', 'java', 'cs++'), remova e retorne 'java' usando pop(índice).")
linguagem=['python','java','cs++']
deletados2=linguagem.pop(1)

print('Linguagem deletada', deletados2)

print('---------------------------------')
print('Exercício 8')
print('Dada a lista [1, 2, 3, 4, 5], remova todos os elementos usando clear().')
o=[1, 2, 3, 4, 5]
o.clear()

print('---------------------------------')
print('Exercício 9')
print("Dada a lista ['a', 'b', 'd']:")
print("1. Insira 'c' na posição 2.")
print("2. Depois, remova 'a'.")
a=['a','b','d']

a.insert(2, 'c')
print('Item adicionado', a)

a.remove('c')
print('Item C removido', a)

print('---------------------------------')

print('Exercício 10')

print('Dada a lista [10, 20, 30, 40, 50]:')
print('1. Adicione 60 no final.')
print('2. Insira 15 na posição 1.')
print('3. Remova o elemento 30.')
print('4. Remova o último elemento e guarde-o em uma variável.')

p=[10,20,30,40,50]

p.append(60)
p.insert(1, 15)  
p.remove(30)     
ultimo = p.pop() 

print(p)
print('Último elemento removido:', ultimo)