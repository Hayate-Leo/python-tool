names = ['Taro', 'John', 'Hanako', 'Vegeta']
powers = [35, 45, 23, 18000]

for i, name in enumerate(names):
    print(i, name)

for name, power in zip(names, powers):
    print(f'{name}の戦闘力は{power}だよ')

for i, (name, power) in enumerate(zip(names, powers)):
    print(f'{i}: {name}の戦闘力は{power}だよ')

