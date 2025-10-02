import requests


# print("status", pedido.status_code)

# Cardápio: Entrada ,Prato, Sobremesa, Mesa e Bebida

# Mesa 01

# print(pedido.json())
# result=pedido.json()
# for item in result:
#     print(item.get("Prato"))

entrada=("- Bruschetta de tomate e manjericão\n- Calabresa acebolada\n- Anéis de cebola\n- Bolinho de queijo\n- Palitos de mussarela")
          
PizzasSalgadas=("- Margherita (molho, mussarela e manjericão)\n- Calabresa com cebola\n- Frango com catupiry\n- Portuguesa (presunto, ovo, cebola, ervilha)\n- Quatro queijos\n- Pepperoni")

PizzasDoces=("- Chocolate com morango\n- Banana com canela\n- Romeu e Julieta (goiabada com queijo)\n- Nutella com banana- Doce de leite com coco\n- Prestígio (chocolate com coco")

Salgados=("- Esfiha de carne\n- Esfiha de frango\n- Coxinha\n- Kibe\n- Empada de frango\n- Pastel (Frango, Carne, Bauru, Calabresa)")

Doces=("- Esfiha doce de chocolate\n- Esfiha doce de banana com canela\n- Mini churros com doce de leite\n- Brigadeiro\n- Beijinho\n- Cajuzinho")

Sobremesas=("- Pudim de leite condensado\n- Mousse de maracujá\n- Torta de limão\n- Cheesecake\n- Brownie com sorvete\n- Sorvete (baunilha, chocolate, morango)\n- Pavê de chocolate\n- Bolo de cenoura com cobertura de chocolate\n- Creme de papaya\n- Gelatina com frutas")

Bebidas=("- Refrigerante (250ml, 350ml, 600ml, 1L, 2L)\n- Coca-Cola, Guaraná, Fanta\n- Suco natural (350ml)\n- Laranja, Maracujá, Abacaxi\n- Água mineral (500ml, 1L)\n- Cerveja (lata 350ml)\n- Chá gelado (350ml)")



resposta=input('Olá, Cliente. Seja bem-vindo ao meu restaurante automático. Já recebeu o cardápio?\n(1) Sim\n(2) Não\n')
if resposta == "1":
    print("eba")
elif resposta == "2":
    print("Ora, sentimos muito pela inconveniência. Aqui vai:")
    print(f"[Pratos de Entrada]\n{entrada}")
    print("----------")
    print(f"[Pizza Salgada]\n{PizzasSalgadas}")
    print("----------")
    print(f"[Pizza Doce]\n{PizzasDoces}")
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


