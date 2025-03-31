print("Digite sua idade: ")
idade = int(input())

if idade < 15:
  print('Criança')
elif(idade>= 15 and idade <= 19):
  print('Adolescente')
elif(idade>=19 and idade<60):
  print('Adulto')
else:
  print('Idoso')