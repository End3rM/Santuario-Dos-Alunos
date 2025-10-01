import requests

dados=requests.get("https://viacep.com.br/ws/01001000/json/")

# print(dados.json()['CEP,Rua,Bairro'])

# print(dados.json()).get('CEP','Rua','Bairro')

info=(input("Olá! É um prazer estar de volta. Pois bem, poderia me informar seu CEP? Vou te mostrar algo legal. 😸\n"))
print(f"Muito bem! Este aqui é seu CEP {info}, está correto?")
resposta=input("(1) Sim\n(2) Não\n")
if resposta == '1':
  print("Ótimo. Aqui estão suas informações, mestrão!")
  maca=requests.get(f"https://viacep.com.br/ws/{info}/json/")

  print('---------CEP-------------')
  print(maca.json().get('cep')) 
  print('---------BAIRRO----------')
  print(maca.json().get('bairro'))
  print('---------RUA-------------')
  print(maca.json().get('logradouro'))
elif resposta == '2':
  print("Poxa, que pena. Tente novamente:")
  repetir=(input('Digite outro CEP:\n'))
  banana=requests.get(f"https://viacep.com.br/ws/{repetir}/json/")

  print('----------CEP------------')
  print(banana.json().get('cep'))
  print('----------BAIRRO---------')
  print(banana.json().get('bairro'))
  print('----------RUA------------')
  print(banana.json().get('logradouro'))
else:
  print("Encontramos um erro inesperado. Reinicie o serviço. [400]")


