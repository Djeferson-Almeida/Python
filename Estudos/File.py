with open ('D:\Python_estudo\Estudos\Poesia.txt',encoding='utf8') as f:
  lines = f.readlines()

  count=0

#Percorre o conteúdo do arquivo
  for line in lines:
    count += 1
    print(f'line{count}:{line}') 