# nome = input("Digite o nome: ")
# email = input("Digite o e-mail: ")

# arquivo = open("pessoa.txt", "a")

# arquivo.write(nome + " | " + email + "\n")
# arquivo.close()
import time
sim = ["Sim", "s", "ss", "sim"]
print('1) Desenvolva um programa que solicite ao usuário os dados de um produto (Nome, Valor e Quantidade) e os armazene.')
nome=input('Seja bem-vindo. Qual é seu nome?\n')
resposta=input(f'É um prazer, {nome}! Já sabe o que vai comprar? (Sim/Não)\n')
if resposta in sim:
    produto=input('Certo, qual é o produto que deseja comprar?\n')
    quantidade=int(input(f'O produto {produto} é uma ótima escolha! Quantas unidades você procura?\n'))
    for i in range(5, 0, -1):
        print(f"Finalizando compra em {i}..")
    time.sleep(5)  
    print(f'Processo finalizado. {quantidade} unidades de {produto} foram adicionados ao seu carrinho. Prossiga para pagar.')
    arquivo = open("compra.txt", "a")
    arquivo.write(nome + " | " + produto + " | " + str(quantidade) + "\n")
    arquivo.close()
elif resposta == "Não":
    print('Tudo bem! Se precisar de ajuda, busque apoio em nossa página principal.')
else:
    print('Desculpe, seja mais claro.')
