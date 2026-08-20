# 1
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_nomes = ['Brenda', 'Paula', 'Sabrina', 'Maria']
lista_ano = [1995, 2026]
# 2
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista_de_numeros:
    print(numero)
# 3
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_impares = 0

for numero in lista_de_numeros:
    if numero % 2 == 1:
    soma_impares = soma_impares + numero

print(soma_impares)

# 4
for i in range(10, 0, -1):
    print(i)

#5
tabuada = int(input('Digite um numero para a tabuada: '))
for i in range(1, 11):
    resultado = tabuada  * i
    print(f'{tabuada} x {i} = {resultado}')

#6
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f'A soma dos elementos é: {soma}')
except TypeError:
    print('Erro: a lista contém um valor que não é número.')

    