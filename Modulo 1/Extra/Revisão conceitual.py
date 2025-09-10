# Exercício 1: If/Else (Múltiplas Condições)
# Enunciado: Escreva um programa que determine o preço do ingresso de cinema baseado
# na idade do cliente e se é estudante. As regras são:
# Crianças até 12 anos: R$ 8,00
# Estudantes (com carteirinha) de qualquer idade: R$ 12,00
# Idosos (65+ anos): R$ 10,00
# Adultos (13-64 anos) não estudantes: R$ 20,00
# O programa deve perguntar idade e se é estudante.
# Exemplo de Saída:
# text
# Digite sua idade: 18
# É estudante? (s/n): s
# Preço do ingresso: R$ 12.00

# Exercício 2: For + If/Else
# Enunciado: Escreva um programa que analise uma lista de números fornecida pelo usuário.
# Para cada número na lista, o programa deve determinar e exibir se ele é positivo, negativo
# ou zero. Além disso, no final, deve contar e mostrar a quantidade de números positivos,
# negativos e zeros encontrados.
# Exemplo de Saída:
# text
# Digite os números separados por espaço: 5 -2 0 8 -1 0
# 5 é positivo.
# -2 é negativo.
# 0 é zero.
# 8 é positivo.
# -1 é negativo.
# 0 é zero.
# Relatório:
# Positivos: 2
# Negativos: 2
# Zeros: 2

# Exercício 3: While + If/Else
# Enunciado: Crie um programa que simule um caixa eletrônico simples. O programa deve
# iniciar com um saldo de R$ 1000,00. Ele deve apresentar um menu com as opções: (1)
# Sacar, (2) Depositar, (3) Ver Saldo e (4) Sair. O loop deve continuar até que o usuário
# escolha a opção 4. Para saques, não deve ser permitido sacar mais do que o saldo
# disponível.
# Exemplo de Saída:
# text
# Caixa Eletrônico
# (1) Sacar
# (2) Depositar
# (3) Ver Saldo
# (4) Sair
# Opção: 1
# Valor para sacar: 500
# Saque realizado com sucesso!
# ...
# Opção: 4
# Obrigado por usar nossos serviços!

# Exercício 4 : While + If/Else (com acumulador)
# Enunciado: Crie um programa de controle de estoque simples. O programa deve começar
# com 50 unidades de um produto. O usuário pode:
# (1) Adicionar unidades ao estoque
# (2) Remover unidades do estoque
# (3) Verificar estoque atual
# (4) Sair
# Não permita que o estoque fique negativo.

# print('Exercício 1: If/Else (Múltiplas Condições)')
# print('Escreva um programa que determine o preço do ingresso de cinema baseado')

# na idade do cliente e se é estudante. As regras são:
# Crianças até 12 anos: R$ 8,00
# Estudantes (com carteirinha) de qualquer idade: R$ 12,00
# Idosos (65+ anos): R$ 10,00
# Adultos (13-64 anos) não estudantes: R$ 20,00
# O programa deve perguntar idade e se é estudante.
# Exemplo de Saída:
# text
# Digite sua idade: 18
# É estudante? (s/n): s
# Preço do ingresso: R$ 12.00


# idade=int(input('Olá. Quantos anos tens?\n'))
# estudante=input('Você é estudante?\n(Sim/Não)\n')

# if idade > 0 and estudante == 'Sim':
#     print('Seu valor final é R$ 12.00.')
# elif idade <= 12:
#     print('Seu valor final é R$ 8,00.')
# elif idade > 13 and estudante == 'Não':
#     print('Seu valor é R$ 20,00.')
# elif idade >= 65:
#     print('Seu valor final é R$ 10,00')
# else:
#     print('Seu valor final é R$ 20,00')

# print('------------------------------------------------')

# print('Exercício 2: For + If/Else')
# print('Enunciado: Escreva um programa que analise uma lista de números fornecida pelo usuário.')
# Para cada número na lista, o programa deve determinar e exibir se ele é positivo, negativo
# ou zero. Além disso, no final, deve contar e mostrar a quantidade de números positivos,
# negativos e zeros encontrados.
# Exemplo de Saída:
# text
# Digite os números separados por espaço: 5 -2 0 8 -1 0
# 5 é positivo.
# -2 é negativo.
# 0 é zero.
# 8 é positivo.
# -1 é negativo.
# 0 é zero.
# Relatório:
# Positivos: 2
# Negativos: 2
# Zeros: 2

# print('2) Digite cinco números e descubra se eles são: Positivos, negativos ou iguais a zero.')
# numero1=int(input('Digite um número:\n'))
# numero2=int(input('Digite outro número:\n'))
# numero3=int(input('Digite mais um número:\n'))
# numero4=int(input('Digite o penúltimo número:\n'))
# numero5=int(input('Digite o último número:\n'))

# numeros= [numero1, numero2, numero3, numero4, numero5]


# for numero in numeros:  
#     if numero == 0:
#         print(f'O número {numero} é igual a zero.') 
#     elif numero > 0:
#         print(f'O número {numero} é positivo!')
#     else:
#         print(f'O número {numero} é negativo.')
#     if numero % 2 == 0:
#         print('E é par!')
#     else:
#         print('E é impar!')

print('------------------------------------------------')

# print("Exercício 3: While + If/Else")
# print("Enunciado: Crie um programa que simule um caixa eletrônico simples.") 
# O programa deve iniciar com um saldo de R$ 1000,00. Ele deve apresentar um menu com as opções: 
# (1) Sacar, (2) Depositar, (3) Ver Saldo e (4) Sair. O loop deve continuar até que o usuário
# escolha a opção 4. Para saques, não deve ser permitido sacar mais do que o saldo
# disponível.
# Exemplo de Saída:
# text
# Caixa Eletrônico
# (1) Sacar
# (2) Depositar
# (3) Ver Saldo
# (4) Sair
# Opção: 1
# Valor para sacar: 500
# Saque realizado com sucesso!
# ...
# Opção: 4
# Obrigado por usar nossos serviços!



while True:
        saldo1=1000.00
        nome= input('Olá! Confirme sua identidade: Qual é seu nome?\n')
        print(f'Olá, {nome}! Seja bem-vindo. Abrindo o menu, aguarde alguns segundos.')
    # Contagem regressiva de 3 segundos
	    
        print('Menu carregado com sucesso!\n')
        print('[CAIXA ELETRÔNICO]\n(1) Sacar\n(2) Depositar\n(3) Ver Saldo\n(4) Sair')

        escolha=int(input('Aperte UM botão: ( )\b\b'))




