from bs4 import BeautifulSoup as bs
import requests

url = "https://www.ev.org.br/trilhas-de-conhecimento"
response = requests.get(url)
html = response.content
soup = bs(html,"lxml")

book_items = soup.find_all("div", class_ = "o-trails-grid")

for t_courses_wrap in book_items:
  print('Título: ' + t_courses_wrap.find("h3", class_ = "m-card_title").get_text(strip = True))
  print('Descrição: ' + t_courses_wrap.find("p", class_ = "m-card_desc").get_text(strip = True))
  cursos = t_courses_wrap.find("p",class_="m-info_desc -small m-card_info")
  duracao = t_courses_wrap.find("div", class_="m-info m-card_foot")
  print('Cursos: ' + cursos.get_text(strip = True).split('Cursos')[1])





