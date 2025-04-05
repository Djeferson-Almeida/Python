
```Python

#Exemplo de expressão regular:
phone_number = re.compile(r'(\(\d{2}\)? (\d{5}-\d{4})') # Os () delimitam os grupos

#\d -> Substitui um digito
#\d{2} -> Substitui dois dígitos e consequentemente alterando o número ele vai substituindo mais dígitos.
# '?' -> Torna opcional o elemento que vem antes deste sinal
# * Completa o que tiver após 

#Exemplo:
palavra = re.compile('py*thon')
mol = palavra.search('Python é uma ótima linguagem de programação')

mol.group() # Busca o grupo que tiver py no inicío da palavra

result = phone_number.search('My number is (48) 99658-4456, please call me after 7pm')

A linha de código acima busca o padrão de dígitos informado anteriormente dentro da frase em questão


#Imprime na tela os "Grupos definidos na linha 3 - phone_number"

print('DDD: ' + result.group(1))
print('Phone number:' + result.group(2))

#Outras maneiras de chamar os grupos   
ddd,phone = result.groups()

print(ddd)
print(phone)

#Outros exemplos de expressão regular utilizando outros elementos da classe de caracteres (/d-/s/w)

import re
frutas = re.compile('\d+\s\w+') # /s substitui espaço e \w substitui letras

frutas.findall('10 maçãs, 7 peras, 5 bananas, 1 melancia')#Busca tudo que tem dígitos, espaços e letras

#re.I ignora minúsculas e maiúsculas na busca
#Exemplo

frutas = re.compile('Maçãs',re.I)

