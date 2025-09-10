# Exercício 1: Calculadora Simples
# Enunciado: Crie uma função que receba dois números e uma operação (+, -,*, /) e retorne o resultado da operação.
# Exercício 2: Criador de Saudação
# Enunciado: Crie uma função que receba um nome e um horário (manhã,
# tarde, noite) e retorne uma saudação personalizada.
# EXEMPLO: Ola Gabriel , Bom dia
# Exercício 3: Crie uma função que valida uma senha enviada pelo usuário

print("Exercício 3: Crie uma função que valida uma senha enviada pelo usuário")
def somar(numeroa, numerob, numeroc, numerod):
    return numeroa + numerob - numeroc // numerod

numeroa=int(input(f'Digite um número: \n'))
numerob=int(input(f'Você escolheu "{numeroa}". Digite outro número: \n'))
numeroc=int(input(f'Você escolheu "{numeroa}" e "{numerob}". Digite mais um número: \n'))
numerod=int(input(f'Você escolheu "{numeroa}" ,"{numerob}" e "{numeroc}". Digite o último número: \n'))

resultado = somar(numeroa, numerob, numeroc, numerod)
print(f"Seu resultado é.. ✨{resultado}✨")

print('----------------------------------')
print("Crie uma função que receba um nome e um horário (manhã, tarde, noite) e retorne uma saudação personalizada")

def saudaçao(a, b):
    
    
    if b == 'Manhã':
        return(f"Bom dia, {a}!")
    elif b == 'Tarde':
        return(f"Boa tarde, {a}!")
    elif b == 'Noite':
        return(f"Boa noite, {a}!")

print(saudaçao('Professor Gabriel','Manhã'))
print(saudaçao('Professor Gabriel','Tarde'))
print(saudaçao('Professor Gabriel','Noite'))

print('----------------------------------')
print('Exercício 3: Crie uma função que valida uma senha enviada pelo usuário')

def validar_senha(senha):
    senha_correta = "123456"
    if senha == senha_correta:
        return "Acesso concedido"
    else:
        return "Acesso negado"

print(validar_senha('123456'))
print(validar_senha('134562'))