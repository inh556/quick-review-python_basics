import re

# sub('match rule', 'new string', 'str')

phone_num = '123-456-6789 # phone number'
p2 = re.sub(r'#.*$', '', phone_num)
print(p2)
p3 = re.sub(r'\D', '', p2)
print(p3)

p4 = re.findall(r'\d+', p2)
print(p4)