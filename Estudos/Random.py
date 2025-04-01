import random

secretNumber = random.randint(1,20)
print ("Advinhe o número em que estou pensando, é um número de 1 a 20")

for tentativas in range (1,7):
  print ("Tente advinhar o número")
  guess = int(input())

  if guess < secretNumber:
    print('O número informado é muito baixo')
  elif guess > secretNumber:
    print('O número informado é muito alto')
  else:
      break
  
if guess == secretNumber:
   print('Parabéns!, Você acertou o número em ' + str(tentativas) + " tentativas")
else:
    print("Que pena, você não acertou o número, o número era: " + str(secretNumber))
