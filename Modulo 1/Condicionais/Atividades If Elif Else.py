# Exercício 1
# Verifique se um número é positivo. Se for maior que zero, imprima "Positivo".
# Exercício 3
# Leia dois números e imprima o maior deles.
# Exercício 4
# Solicite a nota de um aluno. Se for maior ou igual a 6, imprima "Aprovado"; caso
# contrário, "Reprovado".
# Exercício 5
# Peça ao usuário para digitar uma senha. Se for "1234", imprima "Acesso
# permitido"; senão, "Acesso negado".
# Exercício 6
# Classifique uma idade em:
# ● "Criança" (0-12 anos),
# ● "Adolescente" (13-17 anos),
# ● "Adulto" (18+ anos).
# Exercício 8
# Calcule o valor final de uma compra com 10% de desconto se o valor for maior que
# R$100.
# Exercício 10
# Dê um número de 1 a 7 e imprima o dia da semana correspondente (ex: 1 =
# Domingo, 2 = Segunda, etc.).


# print('1) Verifique se um número é positivo. Se for maior que zero, imprima "Positivo".')
# numero=int(input('Digite um número: '))

# if numero >0:
#      print('Positivo.')
# else:
#      print('Negativo.')
# print('------------------------------------------------')
# print('3) Qual é o maior número?')
# numero1=int(input('Digite um número: '))
# numero2=int(input('Digite outro número: '))

# if numero1 > numero2:
#      print('O primeiro número é maior que o segundo')
# elif numero2 > numero1:
#      print('O segundo número é maior que o primeiro!')
# else: 
#      print('Os números são iguais.')
# print('------------------------------------------------') 
# print('4) Solicite a nota de um aluno. Se for maior ou igual a 6, imprima "Aprovado"')
# nota=int(input('Quanto você tirou na prova? '))

# if nota >= 6: 
#     print('Parabéns! Você passou.')
# else:
#     print('Você não passou, solicite a recuperação.')
# print('------------------------------------------------')
# print('5) Peça ao usuário para digitar uma senha. Se for "1234", imprima "Acesso permitido"')

# senha1=int(input('Olá! Digite sua senha: '))

# if senha1 == 1234:
#     print('Seja bem-vindo!')
# else:
#     print('Ocorreu um erro, tente novamente.')
# print('------------------------------------------------')
# print('6) Classifique uma idade em:"Criança" (0-12 anos), "Adolescente" (13-17 anos),"Adulto" (18+ anos).')
# idade=int(input('Olá! Quantos anos tens? '))

# if idade > 18:
#     print('Você é um adulto.')
# elif idade >= 13:
#     print('Você é um adolescente.')
# else:
#     print('Você é uma criança.')
# print('------------------------------------------------')
print('8) Calcule o valor final de uma compra com 10% de desconto se o valor for maior que R$100')
valor=float(input('Digite o valor da tua compra: '))
desconto = 10.00
valordesconto = valor - (valor * desconto /100 )

if valor >=100:
    print(f'Ganhou {valor*0.10} de desconto. O valor total é R${valordesconto}!')
elif valor >90:
    print('Poxa, quase lá! Em uma compra de 100 reais, você ganha um descontinho ;).')
    print('(1) Retornar para carrinho (2) Finalizar compra')
else:
    print('Compra finalizada, obrigada pela preferência.')

print('------------------------------------------------')
print('10) Dê um número de 1 a 7 e imprima o dia da semana correspondente')
dia=int(input('Que dia é hoje? '))

if dia == 1:
    print('Hoje é Segunda-Feira :(')
elif dia == 2:
    print('Hoje é Terça-feira!')
elif dia == 3:
    print('Hoje é Quarta-feira!')
elif dia == 4:
    print('Hoje é Quinta-feira!')
elif dia == 5:
    print('Hoje é Sexta-feira!')
elif dia == 6:
    print('Hoje é Sábado! Ufa.')
else: 
    print('Hoje é Domingo.')

