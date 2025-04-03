def is_phone_number(text):
  if len(text) != 15:
    return False
  if text[0] != ')':
    return False
  for i in range(1,3):
    if not text[i].isdecimal():
      return False
  if text[4] != ' ':
    return False
  for i in range(5,10):
    if not text[i].isdecimal():
      return False
  if text[10] != '-':
    return False
  for i in range(10,15):
    if not text[i].isdecimal():
      return False
  return True

print(is_phone_number('(48) 99658-4456'))