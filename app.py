import requests
import json

url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='
token = '62ebf2cee933356a5e46eb480772725b55b3af4f'

response = requests.get(url + token)

conteudo = response.content
conteudo_decodificado = json.loads(conteudo) 

def salvar_json(conteudo):
  conteudo_json = json.dumps(conteudo)
  arquivo = open('answer.json', 'a')
  arquivo.write(conteudo_json)
  arquivo.close()

salvar_json(conteudo_decodificado)