import re

nomeRegex = re.compile(r'Primeiro nome: (.*), Sobrenome: (.*)')

mo = nomeRegex.search("Primeiro nome: João , Sobrenome: Augusto")
print('Nome completo: ',mo.group(1),mo.group(2))