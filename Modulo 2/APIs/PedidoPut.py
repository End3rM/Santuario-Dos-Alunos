import requests
dados=requests.get('https://68dea937898434f413559869.mockapi.io/Get')
result=dados.json()
for item in result:
    print('-----------------')
    print("Id:")
    print(item.get('id')) 
    print("Mesas:")
    print(item.get('Mesa'))

# Cardápio: Entrada ,Prato, Sobremesa, Mesa e Bebida


print("-----------------[REPARAÇÃO]-----------------")
id=input("Seja bem-vindo ao nosso sistema de reparação. Qual é o seu ID?\n")
entrada=input(f"Certo. O seu ID {id} foi registrado. Qual será o pedido de entrada?\n")
prato=input("Certo. E o Prato Principal?\n")
sobremesa=input(f"Hmmm.. Boa escolha. Gostaria de uma sobremesa?\n")
bebida=input("E para beber? Temos entre 50ml, 350ml, 600ml, 1L e 2L.\n")
mesa=input("Em qual mesa você está?\n")

PedidoNovo={
    'Entrada': entrada,
    'Prato': prato,
    'Sobremesa': sobremesa,
    'Bebidas': bebida,
    'Mesa': mesa,
}
requests.put(f'https://68dea937898434f413559869.mockapi.io/Get/{id}',PedidoNovo)
    