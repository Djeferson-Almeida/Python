import random

capitais = {
'Amapá': 'Macapá',
'Amazonas': 'Manaus',
'Bahia': 'Salvador',
'Ceará': 'Fortaleza',
'Distrito Federal': 'Brasília',
'Espírito Santo': 'Vitória',
'Goiás':'Goiânia',
'Mato Grosso': 'Cuiabá',
'Mato Grosso do Sul': 'Campo Grande',
'Minas Gerais': 'Belo Horizonte',
'Paraíba': 'João Pessoa',
'Paraná': 'Curitiba',
'Pernambuco': 'Recife',
'Piauí': 'Teresina',
'Rio de Janeiro': 'Rio de Janeiro',
'Rio Grande do Norte': 'Natal',
'Rio Grande do Sul': 'Porto Alegre',
'Rondônia': 'Porto Velho',
'Santa Catarina': 'Florianópolis',
'São Paulo': 'São Paulo'
}

#Gerar as 30 provas
for prova_num in range(30):

  arquivo_prova= open(f'Prova_Geo-{prova_num + 1}.txt','w',encoding='utf8')
  arquivo_respostas= open(f'Prova_Geo_respostas-{prova_num + 1}.txt', 'w', encoding='utf8')

  arquivo_prova.write('Nome:\n\nData:\n\nPeríodo:\n\n')
  arquivo_prova.write(' ' * 20) + f'Prova Capitais Brasileiras(Questionário{prova_num + 1})'
  arquivo_prova.write('\n\n')

#Mistura a ordem dos estados em uma lista
  estados = list(capitais.keys())
  random.shuffle(estados)

#for para percorrer os 26 estados, fazendo uma questão para cada um
  for questao_num in range(26):
    resposta_correta = capitais[estados[questao_num]]
    respostas_erradas = list(capitais.values())
    del respostas_erradas [respostas_erradas.index(resposta_correta)]
    respostas_erradas= random.sample(respostas_erradas, 3)
    respostas = respostas_erradas + [resposta_correta]
    random.shuffle(respostas)

  #Escreve as questões e as opções no arquivo
  arquivo_prova.write(f'{questao_num + 1}. Qual é a capital de {estados[questao_num]}?\n')
  for i in range(4):
    arquivo_prova.write(f"     {'ABCD'[i]}. {respostas[i]}\n")
    arquivo_prova.write("\n")

    #Escreve as respostas no arquivo de resposta
    arquivo_prova.write(f"{questao_num + 1}. {'ABCD' [respostas.index(resposta_correta)]}\n")
arquivo_prova.close()
arquivo_respostas.close()
  




