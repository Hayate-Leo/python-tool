a = [123, 65, 4, 8, 3, 9, 5, 6, 8, 14, 5]

# python3.7まで
# n = len(a)
# if n > 10:
#     print(f'このリストの要素数は10より長いです')

# セイウチ演算子
if (n:= len(a)) > 10:
    print(f'このリストの要素数は10より長いです')


d = {'a': 'aです', 'b': 'bです'}

# python3.7まで
# m = d.get('a')
# if m:
#     print(m)

# セイウチ演算子
if m:=d.get('a'):
    print(m)