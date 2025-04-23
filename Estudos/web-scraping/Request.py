import requests

url = "https://github.com/Djeferson-Almeida/Python/tree/main/Estudos"

response = requests.get(url)

html = response.content

print(html)

print(response.status_code)