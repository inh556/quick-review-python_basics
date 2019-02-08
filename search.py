import re

p = re.compile(r'(\d+)-(\d+)-(\d+)')
year = p.search('s2019-01-23sdf').groups()

print(year)