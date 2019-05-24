import requests
import json
import os
from hashlib import sha1

url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='
token = '62ebf2cee933356a5e46eb480772725b55b3af4f'
url_envio = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token="

response = requests.get(url + token)

dados_api = response.content
conteudo_json_api = json.loads(dados_api) 

def salvar_json(conteudo):
  conteudo_json = json.dumps(conteudo, indent=4)

  # remove se já existir
  os.remove('answer.json')

  arquivo = open('answer.json', 'a')
  arquivo.write(conteudo_json)
  arquivo.close()

def decifrar(texto, casas):
  alfabeto = "abcdefghijklmnopqrstuvwxyz"
  texto_decifrado = ""

  for i in texto:
    if (i == " ") or (i.isdigit()) or (i == "."):
      texto_decifrado += i
    else:
      index = alfabeto.index(i) - casas
      texto_decifrado += alfabeto[index]  
  
  return texto_decifrado

def enviar_arquivo(arquivo):
  response = requests.post(url_envio + token, files={'answer': open(arquivo, 'rb')})
  print(response.content)

# salva o arquivo localmente
salvar_json(conteudo_json_api)

# lendo os dados do arquivo local
dados_local = open('answer.json').read()
conteudo_json_local = json.loads(dados_local)

# obtendo texto decifrado e resumo
decifrado = decifrar(conteudo_json_local['cifrado'], conteudo_json_local['numero_casas'])
resumo = sha1(decifrado.encode('utf-8')).hexdigest()

# incluindo texto decifrado e resumo no json
conteudo_json_local['decifrado'] = decifrado
conteudo_json_local['resumo_criptografico'] = resumo

# atualizando json
salvar_json(conteudo_json_local)

# enviando arquivo 
enviar_arquivo('answer.json')



