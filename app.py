import requests
import json
import functions
from hashlib import sha1

url = 'https://api.codenation.dev/v1/challenge/dev-ps/'
token = '?token=62ebf2cee933356a5e46eb480772725b55b3af4f'
obter = 'generate-data'
enviar = "submit-solution"

response = requests.get(url + obter + token)

dados_api = response.content
conteudo_json_api = json.loads(dados_api) 

# salva o arquivo localmente
functions.salvar_json(conteudo_json_api)

# lendo os dados do arquivo local
dados_local = open('answer.json').read()
conteudo_json_local = json.loads(dados_local)

# obtendo texto decifrado e resumo
decifrado = functions.decifrar(conteudo_json_local['cifrado'], conteudo_json_local['numero_casas'])
resumo = sha1(decifrado.encode('utf-8')).hexdigest()

# incluindo texto decifrado e resumo no json
conteudo_json_local['decifrado'] = decifrado
conteudo_json_local['resumo_criptografico'] = resumo

# atualizando json
functions.salvar_json(conteudo_json_local)

# enviando arquivo 
functions.enviar_arquivo('answer.json', url + enviar + token)



