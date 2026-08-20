# 1
"""macas = int(input("Digite a quantidade de maçãs vendidas: "))
bananas = int(input("Digite a quantidade de bananas vendidas: "))

if macas > bananas:
    print('As maças tiveram mais vendas.')
elif bananas > macas:
    print('As bananas tiveram mais vendas.')
else:
    print('As vendas foram iguais.')"""

# 2
"""atividade_A = int(input('Informe os dias para a atividade A: '))
atividade_B = int(input('Informe os dias para a atividade B: '))
atividade_C = int(input('Informe os dias para a atividade C: '))

if atividade_A < 0 or atividade_B < 0 or atividade_C < 0:
    print("Erro: Os dias não podem ser negativos.")
else:
    tempo_total = atividade_A + atividade_B + atividade_C
    print(f"O tempo total do projeto é de {tempo_total} dias.")"""

#3
"""temperatura_atual = int(input('Digite a temperatura atual: '))
if temperatura_atual > 25:
    print('Alerta! Temperatura acima do limite permitido.')
else:
    print("Temperatura dentro do limite seguro.")"""

#4
"""peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso normal.')
else: 
    print('Acima do peso.')"""

#5
"""limite = 3000.0
total_despesas = float(input('Digite o total de despesas no mês (R$): '))

if total_despesas > limite:
    print('Atenção! Você ultrapassou o limite do orçamento.')
else:
    print('Gastos dentro do limite.')"""

#6 
"""hora_atual = float(input('Digite a hora atual (formato 24 horas): '))
if 8 <= hora_atual < 18:
    print('Acesso permitido')
else:
    print('Acesso negado.')"""

#7
"""nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))

media = nota_1 + nota_2 + nota_3 / 3

if media >= 7:
    print('Aprovado')
elif 5 <= media:
    print('Recuperação')
else:
    print('Reprovado')"""

#8
"""numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('Par')
else:
    print('Impar')"""

#9

"""renda_mensal = float(input('Digite sua renda mensal: R$ '))
parcela_desejada = float(input('Digite o valor da parcela desejada: R$ '))

if renda_mensal > 2000 and parcela_desejada <= 0.3 * renda_mensal:
    print('Emprestimo aprovado')
elif renda_mensal <= 2000:
    print('Emprestimo negado: renda insuficiente')
else: 
    print('Emprestimo negado')"""