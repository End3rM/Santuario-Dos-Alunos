# 1. Contagem regressiva: Faça um programa que imprima uma contagem
# regressiva de 10 até 1 e depois imprima "Fogo!".

# 2. Validação de entrada: Peça ao usuário para digitar uma nota entre 0 e 10.
# Continue pedindo até que ele digite um valor válido.


print('1. Faça um programa que imprima uma contagem regressiva de 10 até 1 e depois imprima "Fogo!')

contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print('Fogo!')

print('------------------------------------------------')

print('2. Validação de entrada: Peça ao usuário para digitar uma nota entre 0 e 10. Continue pedindo até que ele digite um valor válido')

nota=int(input('Digite uma nota: '))

while nota <0 or nota >10:
    print('Nota inválida')
    nota=int(input('Digite uma nova nota: '))

