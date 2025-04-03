import re

phone_number = re.compile(r'(\(\d{2}\)) (\d{5}-\d{4})')
result = phone_number.search('My number is (48) 99658-4456, please call me after 7pm')

print('DDD: ' + result.group(1))
print('Phone number:' + result.group(2))


#Outras maneiras de chamar os grupos   
ddd,phone = result.groups()

print(ddd)
print(phone)
