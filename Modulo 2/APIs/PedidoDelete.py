import requests
dados=requests.get('https://68dea937898434f413559869.mockapi.io/Get')
result=dados.json()
for item in result:
    print('-----------------')
    print("Id:")
    id=item.get('id') 
    prato=item.get('Prato')

    if 'pizza' in prato:
        id=item.get('id') 
        requests.delete(f'https://68dea937898434f413559869.mockapi.io/Get/{id}')










# print("--------------[Cancelamento]----------------")
# id=input("Sentimos muito pela inconveniência. Qual seria o ID do pedido que deseja cancelar?\n")

