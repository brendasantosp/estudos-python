despensa = ['arroz', 'feijão', 'óleo']
item = input('Digite o itme que você quer verificar: ')

if item in despensa:
    print(f'O item {item} já está na despensa.')

else:
    print(f'O item {item} precisa ser comprado.')
print(despensa)