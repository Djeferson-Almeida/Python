import re

phone_number = re.compile(r'\(\d{2}\) \d{5}-\d{4}')
result = phone_number.search('My number is (48) 99658-4456, please call me after 7pm')

print('Phone number encountered: ' + result.group())
                          