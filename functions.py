import json
import os
import requests

# grava conteudo no arquivo answer.json
def salvar_json(conteudo):
  conteudo_json = json.dumps(conteudo, indent=4)

  # se o arquivo já existir, remove para gravar conteudo em arquivo limpo
  os.remove('answer.json')

  arquivo = open('answer.json', 'a')
  arquivo.write(conteudo_json)
  arquivo.close()

# algoritmo para decifrar texto
def decifrar(texto, casas):
  alfabeto = "abcdefghijklmnopqrstuvwxyz"
  texto_decifrado = ""

  for i in texto:
    if (i == " ") or (i.isdigit()) or (i == ".") or (i == ","):
      texto_decifrado += i
    else:
      index = alfabeto.index(i) - casas
      texto_decifrado += alfabeto[index]  
  
  return texto_decifrado

# envia arquivo para url
def enviar_arquivo(arquivo, url):
  response = requests.post(url, files={'answer': open(arquivo, 'rb')})
  print(response.content)