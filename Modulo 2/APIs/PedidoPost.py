import requests
# print("status", pedido.status_code)

# Cardápio: Entrada ,Prato, Sobremesa, Mesa e Bebida

# Mesa 01

# print(pedido.json())
# result=pedido.json()
# for item in result:
#     print(item.get("Prato"))

entrada=("- Bruschetta de tomate e manjericão\n- Calabresa acebolada\n- Anéis de cebola\n- Bolinho de queijo\n- Palitos de mussarela")
          
PizzasSalgadas=("- Escondidinho de Carne Seca com Purê de Mandioca\n- Risoto de Camarão com Limão Siciliano\n- Lasanha de Berinjela com Molho de Tomate e Queijo\n- Coxinha de Frango com Catupiry\n- Quiche de Alho-Poró com Queijo Gruyère\n- Filé Mignon ao Molho Madeira com Batatas Rústicas\n- Bolinho de Bacalhau com Molho Tártaro\n- Wrap de Frango Grelhado com Abacate e Molho de Iogurte\n- Pizza de Margherita (molho, mussarela e manjericão)\n- Pizza de Calabresa com cebola\n- Pizza de Frango com catupiry\n- Pizza de Portuguesa (presunto, ovo, cebola, ervilha)\n- Pizza de Quatro queijos\n- Pizza de Pepperoni")

PizzasDoces=("- Escondidinho de Carne Seca com Purê de Mandioca\n- Risoto de Camarão com Limão Siciliano\n- Lasanha de Berinjela com Molho de Tomate e Queijo\n- Coxinha de Frango com Catupiry\n- Quiche de Alho-Poró com Queijo Gruyère\n- Filé Mignon ao Molho Madeira com Batatas Rústicas\n- Bolinho de Bacalhau com Molho Tártaro\n- Wrap de Frango Grelhado com Abacate e Molho de Iogurte\n- Pizza de Chocolate com morango\n- Pizza de Banana com canela\n- Pizza de Romeu e Julieta (goiabada com queijo)\n- Pizza de Nutella com banana + Doce de leite com coco\n- Pizza de Prestígio (chocolate com coco)")

Salgados=("- Esfiha de carne\n- Esfiha de frango\n- Coxinha\n- Kibe\n- Empada de frango\n- Pastel (Frango, Carne, Bauru, Calabresa)")

Doces=("- Esfiha doce de chocolate\n- Esfiha doce de banana com canela\n- Mini churros com doce de leite\n- Brigadeiro\n- Beijinho\n- Cajuzinho")

Sobremesas=("- Pudim de leite condensado\n- Mousse de maracujá\n- Torta de limão\n- Cheesecake\n- Brownie com sorvete\n- Sorvete (baunilha, chocolate, morango)\n- Pavê de chocolate\n- Bolo de cenoura com cobertura de chocolate\n- Creme de papaya\n- Gelatina com frutas")

Bebidas=("- Refrigerante (250ml, 350ml, 600ml, 1L, 2L)\n- Coca-Cola, Guaraná, Fanta\n- Suco natural (350ml)\n- Laranja, Maracujá, Abacaxi\n- Água mineral (500ml, 1L)\n- Cerveja (lata 350ml)\n- Chá gelado (350ml)")



resposta=input('Olá, Cliente. Seja bem-vindo ao meu restaurante automático. Já recebeu o cardápio?\n(1) Sim\n(2) Não\n')
if resposta == "1":
    pratoentrada=input("Certo! Então qual será seu prato de entrada?\n")
    pratoprincipal=input("Anotadíssimo. E qual será o prato principal?\n")
    sobremesa=input(f"A nossa {pratoprincipal} é maravilhosa. Combina muito com {pratoentrada}. Pois bem, e para sobremesa?\n")
    drink=input("Olha, faz tempo que não me pedem esse. O que vai querer beber?\n")
    tamanhobebida=input("Quantos Ml? Ou litros? (250ml, 350ml, 600ml, 1L, 2L)\n")
    mesai=input("Em que mesa está sentado?\n")
    pedido={
    'Entrada': (f'{pratoentrada}'),
    'Prato': (f'{pratoprincipal}'),
    'Sobremesa': (f"{sobremesa}"),
    'Bebida':(f'{drink}'),
    'Mesa': (f'{mesai}'),    
}

elif resposta == "2":
    print("Ora, sentimos muito pela inconveniência. Aqui vai:")
    print(f"[Pratos de Entrada]\n{entrada}")
    print("----------")
    print(f"[Cardápio Principal Salgado]\n{PizzasSalgadas}")
    print("----------")
    print(f"[Cardápio Principal Doce]\n{PizzasDoces}")
    print("----------")
    print(f"[Salgados]\n{Salgados}")
    print("----------")
    print(f"[Doces]\n{Doces}")
    print("----------")
    print(f"[Sobremesas]\n{Sobremesas}")
    print("----------")
    print(f"[Bebidas]\n{Bebidas}")
    print("----------")
    pratoentrada=input("Você gostaria de realizar um pedido? Deixe-me anotar seu pedido. Qual será o prato de entrada?\n")
    pratoprincipal=input("E qual será o seu prato principal? Escolha entre uma [Pizza Salgada] ou uma [Pizza Doce]\n")
    sobremesa=input(f"Boa escolha, nosso(a) pizza de {pratoprincipal} é maravilhoso(a)! E agora, para a sobremesa?\n")
    drink=input("Para finalizarmos, qual será sua bebida?\n")
    tamanhobebida=input("Quantos ML? Ou Litros? (250ml, 350ml, 600ml, 1L, 2L)\n")
    print(f"Certo. Seu pedido é: {pratoentrada}, {pratoprincipal}, {sobremesa} e um(a) {drink} de {tamanhobebida}.")
    mesai=input("Pois bem, tenha uma boa noite. Seu pedido chegará em breve! Uma última pergunta, em que mesa gostaria de se sentar?\n")

pedido={
    'Entrada': (f'{pratoentrada}'),
    'Prato': (f'{pratoprincipal}'),
    'Sobremesa': (f"{sobremesa}"),
    'Bebida':(f'{drink}'),
    'Mesa': (f'{mesai}'),    
}


requests.post("https://68dea937898434f413559869.mockapi.io/Get",pedido)

