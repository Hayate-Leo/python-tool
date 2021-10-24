# f = open('tools/test.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()

# with open('tools/test.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

f = open('tools/test.txt', 'r', encoding='utf-8')
try:
    print(f.read())
finally:
    f.close()