import re 

frutas= re.compile(r'\d+\s\w+')

visualizar = frutas.findall('5 bananas, 3 melancias, 4 maças, 5 morangos')

print(visualizar)
