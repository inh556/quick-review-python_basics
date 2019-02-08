import re
p = re.compile('.{3}')
print(p.match('cat'))


p = re.compile('....-..-..')
print(p.match('2019-01-23'))

p = re.compile('\d+-\d+-\d+')
print(p.match('2019-01-23'))


p = re.compile('(\d+)-(\d+)-(\d+)')
print(p.match('2019-01-23').groups())

p = re.compile('(\d+)-(\d+)-(\d+)')
year, month, day = p.match('2019-01-23').groups()

print('%s %s %s' %(year, month, day))