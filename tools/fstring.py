first = 'Hayate'
last = 'Leo'

print(f'私の名前は{first}{last}です')

import math
print(f'円周率は約 {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')


animals = 'Tiger'
print(f'好きな動物は {animals} なんですよ')

print(f'好きな動物は {animals!r} なんですよ')