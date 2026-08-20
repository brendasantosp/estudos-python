""""# 1 e 2
pessoa= [{'nome': 'Brenda','idade': 31, 'cidade': 'São Paulo'}]
pessoa['idade'] = 32
pessoa['profissao'] = 'Desenvolvedora'
del pessoa['cidade']
if 'nome' in pessoa:
    print('A chave 'nome' existe no dicionario')
else:
    print('A chave 'nome' nao existe no dicionario')"""

frase = "o gato viu o cachorro"
resultado = frase.split()
print(resultado)

contagem = {"gato": 1}
print("gato" in contagem)
print("cachorro" in contagem)

frase = "o gato viu o cachorro"
resultado = frase.split()

contagem = {}

for palavra in resultado:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)


