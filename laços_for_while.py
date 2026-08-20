"""clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)"""

#2
"""contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1"""

"""#3
for i in range(5):
    print('Bem-vindo ao Buscante!')"""

#4
"""valores = [10, 20, 30, 40, 50]

soma = 0

for valor in valores:
    soma += valor
    print(soma)"""

#5
"""projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    print(projeto)
    if projeto == None:
        print('Projeto ausente.')"""

#6
"""livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == 'O Hobbit':
        print(f'Livro encontrado: {livro}')
        break"""

#7
"""estoque = 5

while estoque > 0:
estoque -= 1
print(f'Venda realizada! Estoque restante: {estoque}')

print('Estoque esgotado')  """  

#8
"""for segundos in range(10, 0, -1):
    if segundos % 2 == 0:
        print(f'Faltam apenas {segundos} segundos - Não perca essa oportunidade!')
    else:
        print(f'A contagem continua: {segundos} segundos restantes.')
print('Aproveite a promoção')"""

#9
"""livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] == 0:
        continue
    print(f"Livro disponível: {livro['nome']}")"""

#10

while True:
    usuario = input('digite seu nome de usuário: ')
    senha = input('digite sua senha: ')

    if len(usuario) < 5:
        print('O nome de usuário deve ter pelo menos 5 caracteres.')
    continue

    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        continue
    print("Cadastro realizado com sucesso!")
    break


















