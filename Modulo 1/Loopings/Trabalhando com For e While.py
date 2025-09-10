# Utilizando do for e while faça as atividades abaixo
# 1. Contar vogais em uma string
# Enunciado:
# Peça ao usuário uma palavra e conte quantas vogais ela contém.

# 2 Somar elementos de uma lista
# Enunciado:
# Dada a lista numeros = [1, 2, 3, 4, 5], calcule e exiba a soma dos elementos.

# 3. Imprimir elementos de uma lista
# Enunciado:
# Dada a lista frutas = ['maçã', 'banana', 'laranja'], imprima cada fruta em
# uma linha.
# 4 . Tabuada de um número

# 5. Calcular a soma dos números de 1 a 100
# Enunciado:
# Crie um programa que calcule e exiba a soma dos números de 1 a 100.

# 6. Imprimir números de 1 a 10
# Enunciado:
# Escreva um programa que imprima os números de 1 a 10, um em cada linha.

# 7. Validação de Senha
# peça ao usuario para digitar uma senha e valida a senha o codigo nao deve parar caso o
# usuario digite a senha incorreta

# 8. Contagem Regressiva
# Escreva um programa que use um loop while para fazer uma contagem regressiva
# de 10 até 1.

# Exemplo: 
# palavra='joao'

# for item in palavra:
#   print(item)   


print('1) Contar vogais em uma string.')
vogais= ['a','e','i','o','u']

palavra = input('Digite uma palavra: ')
contador = 0
for letra in palavra:
    if letra in vogais:
        contador += 1
print(f'A palavra "{palavra}" contém {contador} vogais.')
print('------------------------------------------------')
print('2) Somar elementos de uma lista [1,2,3,4,5]')

numeros = [1,2,3,4,5]
soma = 0
for numero in numeros:
    soma += numero
print(soma)  

print('------------------------------------------------')
print('3) Imprimir elementos de uma lista maçã, banana,laranja, imprima cada fruta em uma linha.')

lista= ['Maçã','Banana','Laranja']
range(3) 
for fruta in lista:
    print(fruta)
    
print('------------------------------------------------')
print('4) Tabuada do 8:')
numero = 8

for item in range(11):
    print(f'{item}x{numero}={item*numero}')
print('------------------------------------------------')
print('5) Crie um programa que calcule e exiba a soma dos números de 1 a 100.')

soma = 0
for numero in range(1,101):
    soma += numero  
print(f'A soma dos números 1 a 100 resulta em {soma}')
print('------------------------------------------------')
print('6) Imprimir números de 1 a 10')

numero= ['1','2','3','4','5','6','7','8','9','10']
range(10)
for item in numero:
    print(item)
print('------------------------------------------------')
print('7) Digitar a senha para acessar o Pc')

senha = input ('digite a senha: ')

senhaCorreta= 'eusoulinda'

if senha== senhaCorreta:
    print('Você está mais do que correto! >///<')
else:
    print('Retire-se!')
print('------------------------------------------------')
print('8) Escreva um programa que use um loop while para fazer uma contagem regressiva de 10 a 1')

contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print('------------------------------------------------')