# Exercício 1: Validação de Entrada Inteira

# Escreva um programa que solicite um número inteiro ao usuário. Use try-except para tratar
# entradas não numéricas e valores não inteiros. Se ocorrer um erro, peça a entrada
# novamente até que seja válida.

# Exercício 2: Divisão com Tratamento de Múltiplas Exceções

# Crie uma função chamada dividir(a, b) que retorne o resultado da divisão a / b.
# Utilize um bloco try-except genérico (sem especificar o tipo de exceção) para tratar
# quaisquer erros que possam ocorrer durante a operação (como divisão por zero ou tipos
# inválidos).
# Em caso de erro, a função deve retornar None.

# Exercício 3: Acesso a Elemento de Lista com Índice

# Peça ao usuário um índice e tente acessar um elemento em uma lista predefinida (ex: [10,
# 20, 30]). Use try-except para tratar IndexError (índice fora do intervalo) e ValueError (se o
# índice não for um inteiro). Exiba mensagens específicas para cada erro.

print('Exercício 1: Validação de Entrada Inteira')
numerointeiro = None
while numerointeiro is None:
    try:
        numerointeiro = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print('------------------------------')
print('Exercício 2: Divisão com Tratamento de Múltiplas Exceções')
def dividir(a, b):
    return a / b


