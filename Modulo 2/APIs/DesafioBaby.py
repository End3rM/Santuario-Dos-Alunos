

# 2. Um bebê colocou fogo na mesa 5 😮 pegue todos os pedidos feitos na mesa 5 e
# delete porém a família não desistiu do jantar você terá que passar todos os pedidos
# feitos na mesa 5 e passar para a mesa 6.
# Você vai usar GET, DELETE e POST e também vai usar if e for.

import requests
# dados=requests.get('https://68dea937898434f413559869.mockapi.io/Get/').json()

# requests.delete('https://68dea937898434f413559869.mockapi.io/Get/')
# requests.post("https://68dea937898434f413559869.mockapi.io/Get/")

dados=requests.get('https://68dea937898434f413559869.mockapi.io/Get').json()

# brinde= " | Pudim de Leite | 300g | 4 Pedaços | 00,00"
# refill= "| Refill dos Milkshakes. | R$00,00"

# print("------------------------------")

# for item in dados:
#     mesa = item.get('Mesa')
#     entrada=item.get('Entrada')
#     prato=item.get('Prato')
#     sobremesa=item.get('Sobremesa')
#     bebida=item.get('Bebida')
#     id =  item.get('id')
# if mesa == '5':
#  print("------------[PEDIDOS SOS]------------")
#  print(entrada)
#  print(prato)
#  print(sobremesa)
#  print(bebida)
#  print(id)
#  print("------------[PEDIDO SOS]------------")        
# resposta=input("Olá Senhor e Senhora da Mesa 5. Lamentamos muito pelo acidente que ocorreu no primeiro andar. Você gostaria de ser redirecionado para uma mesa melhor localizada com dois brindes de compensação?\n(1) Sim\n")
            
# if resposta == '1':
#     extra =  entrada+ brinde
#     PedidoNovo={
#     'Entrada': extra,
#     'Prato': prato,
#     'Sobremesa': ,
#     'Bebida': bebida,
#     'Mesa': '5'
#     }  
#     print('estou no seugno if')
#     requests.put(f'https://68dea937898434f413559869.mockapi.io/Get/6',PedidoNovo)
# else: 
#     print("Poxa.. Sentimos muito. Tenham uma boa noite!")
        
continue2 =  True
            
brinde = " | (Compensação) Palitos de mussarela."
refillvita= " | (Compensação) Refill da Vitamina de Banana e Maçã. "



print("------------------------------------")
print("[STORY TIME]")
print("> (Manager) Um dos nossos garçons (tinha que ser estágiario) fez o favor de derrubar uma vela acessa na mesa de um cliente.")
print("> (Supervisor) Deus! Todo dia um problema diferente. Faz assim, passa eles pra mesa seis. Acabou de sair um casal de lá.")
print("> (Manager) Mas a mesa 6 é reservada para os nossos clientes VIP..")
print("> (Supervisor) Eu sei, mas não há nada que eu possa fazer fisicamente para compensar.")
print("> (Manager) Vou providenciar alguns brindes de compensação também.")
print("> (Supervisor) Beleza, justo. Boa sorte.")
print("-----------------[FIM]------------------")
for item in dados:
    mesa = item.get('Mesa')
    entrada=item.get('Entrada')
    prato=item.get('Prato')
    sobremesa=item.get('Sobremesa')
    bebida=item.get('Bebida')
    id =  item.get('id')
    if mesa == '4':
     print("------------[PEDIDOS SOS]------------")
     print(entrada)
     print(prato)
     print(sobremesa)
     print(bebida)
     print(id)
     print("------------[PEDIDO SOS]------------")   
    

entradinha = entrada+brinde
refillz= bebida+refillvita

resposta=input("Olá, Senhor(a). Lamentamos o infortúnio que nosso estagiário causou ao seu jantar. Antes que vá embora, que tal uma oferta?\n(1) Ouvir\n(2) Ir Embora\n") 
if resposta == "1":
   print("> (Garçom experiente) Estamos lhe oferecendo uma Mesa na Ala VIP, com vista privilegiada para a praia. Além disso, terá direito a uma pequena compensação em dois dos seus pedidos. Como isso soa?")
   print("> (Cliente) Hmmm. Me parece bom, mas não estou disposto a pagar por nada além do que já paguei.")
   print("> (Garçom experiente) Certamente, não se preocupe com pagamento. Pode me seguir, irei te guiar até a Ala VIP.")
   print("------------------------------------")
   PedidoNovo={
    'Entrada': entradinha,
    'Prato': prato,
    'Sobremesa': sobremesa,
    'Bebida': refillz,
    'Mesa': '6'
}  
   print('Feedback: Positivo')
   requests.put('https://68dea937898434f413559869.mockapi.io/Get/6',PedidoNovo)
elif resposta =='2':
   print("> (Garçom 2) Tudo bem, respeitamos sua escolha e entendemos sua raiva. Reclamações são bem vindas.")
   print("> (Cliente) Não é necessário, apenas não tenho mais apetite depois do que aconteceu.")
   print("> (Garçom 2) ... Certo, passar bem. Tenha uma boa noite, Senhor(a).")
   print("[O Estagiário foi demitido.]")
   print("------------------------------------")
   continue2 = False

 
if continue2 == True:
    answer=input("Agora, temos que limpar a Mesa 5 para que possamos receber mais clientes naquela mesa. Mande o garçom responsável pela bagunça lidar isso.\n(1) Mandar o Gabriel limpar a mesa\n(2) Limpar você mesmo.\n")
    
    if answer == "1":
        print("> (Supervisor) Vá limpar sua bagunça, seu irresponsável!")
        print("> (Gabriel Desastrado) Tá bom, desculpa!")
        print("> (Supervisor) E que não tenham próximas vezes, se não você está demitido!")
        print("------------------------------------")
        requests.delete('https://68dea937898434f413559869.mockapi.io/Get/5')
    elif answer == "2":
        print("[Você e o estágio desastrado foram punidos por desobediência.]")
        print("[Idiotas.]")
    else:
        print("Erro 404.")









