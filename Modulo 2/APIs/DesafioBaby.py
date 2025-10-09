

# 2. Um bebê colocou fogo na mesa 5 😮 pegue todos os pedidos feitos na mesa 5 e
# delete porém a família não desistiu do jantar você terá que passar todos os pedidos
# feitos na mesa 5 e passar para a mesa 6.
# Você vai usar GET, DELETE e POST e também vai usar if e for.

import requests
# dados=requests.get('https://68dea937898434f413559869.mockapi.io/Get/').json()

# requests.delete('https://68dea937898434f413559869.mockapi.io/Get/')
# requests.post("https://68dea937898434f413559869.mockapi.io/Get/")

dados=requests.get('https://68dea937898434f413559869.mockapi.io/Get').json()

brinde= " | Pudim de Leite | 300g | 4 Pedaços | 00,00"
refill= "| Refill dos Milkshakes. | R$00,00"

print("------------------------------")
print("Manager: Estava tudo correndo bem até que.. Nosso Garçom acabou tropeçando em seus cadarços, assustou um Cão de Assistência da Mesa 6 e ele avançou, assustado, na Mesa 5.\nUm casal comia alegremente em nossa Ala Vip.")
print("Cozinheiro Chefe: Agora temos um problema dos grandes! Como vamos compensar isso? Temos que pensar em uma solução URGENTEMENTE.")
print(".")
print("..")
print("...")
print("(Silencio constrangedor na cozinha)")
print("Estagiário Gabriel: Já sei. Vamos passar o casal para a Mesa 6, no Segundo Andar!\nLá eles terão uma vista melhor e.. Distância do cachorro. Mãos a obra!")
# 0053122887

for item in dados:
    mesa = item.get('Mesa')
    if mesa == '5':
        entrada=item.get('Entrada')
        prato=item.get('Prato')
        sobremesa=item.get('Sobremesa')
        bebida=item.get('Bebida')
        print("------------[PEDIDOS SOS]------------")
        print(entrada)
        print(prato)
        print(sobremesa)
        print(bebida)
        print("------------[PEDIDO SOS]------------")
        
    
        
        PedidoNovo={
            'Entrada': entrada,
            'Prato': prato,
            'Sobremesa': sobremesa + brinde,
            'Bebidas': bebida + refill,
            'Mesa': '6',
        }
        
requests.put('https://68dea937898434f413559869.mockapi.io/Get/6',PedidoNovo)
    
        





