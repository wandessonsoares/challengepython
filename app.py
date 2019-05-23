import requests

url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token='
token = '62ebf2cee933356a5e46eb480772725b55b3af4f'

response = requests.get(url + token);

print(response.content);