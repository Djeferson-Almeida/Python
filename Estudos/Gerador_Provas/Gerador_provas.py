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
'São Paulo': 'São Paulo' ,
'Alagoas': 'Maceió',
'Acre': 'Rio Branco',
'Pará': 'Belém',
'Roraima': 'Boa Vista',
'Sergipe': 'Aracaju',
'Tocantins': 'Palmas'
}

#Gerar as 30 provas
for prova_num in range(30):

    # Abre os arquivos de prova e gabarito
    arquivo_prova = open(f'Prova_Geo-{prova_num + 1}.txt', 'w', encoding='utf8')
    arquivo_respostas = open(f'Prova_Geo_respostas-{prova_num + 1}.txt', 'w', encoding='utf8')

    # 🧾 Cabeçalho da prova
    arquivo_prova.write('Nome:\n\nData:\n\nPeríodo:\n\n')
    arquivo_prova.write(' ' * 20 + f'Prova Capitais Brasileiras (Questionário {prova_num + 1})\n\n')

    # Embaralha os estados
    estados = list(capitais.keys())
    random.shuffle(estados)

    # Gera 26 questões
    for questao_num in range(26):
        estado = estados[questao_num]
        resposta_correta = capitais[estado]

        # Gera 3 alternativas incorretas
        respostas_erradas = list(capitais.values())
        respostas_erradas.remove(resposta_correta)
        alternativas = random.sample(respostas_erradas, 3) + [resposta_correta]
        random.shuffle(alternativas)

        # Escreve questão
        arquivo_prova.write(f'{questao_num + 1}. Qual é a capital de {estado}?\n')
        for i in range(4):
            arquivo_prova.write(f"     {'ABCD'[i]}. {alternativas[i]}\n")
        arquivo_prova.write('\n')

        # Escreve resposta correta
        resposta_letra = 'ABCD'[alternativas.index(resposta_correta)]
        arquivo_respostas.write(f'{questao_num + 1}. {resposta_letra}\n')

    # Fecha os arquivos da prova atual
    arquivo_prova.close()
    arquivo_respostas.close()

