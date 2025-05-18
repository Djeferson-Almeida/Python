from bs4 import BeautifulSoup as bs
import requests

url = "https://github.com/Djeferson-Almeida/Python/tree/main/Estudos"
response = requests.get(url)
print(response.status_code)

soup = bs(response.content,'html.parser')
print(soup.select('div p'))


