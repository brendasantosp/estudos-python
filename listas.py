despensa = ['arroz', 'feijão', 'óleo']
item = input('Digite o item que você quer verificar: ')

if item in despensa:
    print(f'O item {item} já está na despensa.')

else:
    print(f'O item {item} precisa ser comprado.')
print(despensa)

# ex: 02

notas = [85, 70, 90, 60, 75]

notas.sort()
print('Notas ordenadas:', notas)

# ex: 03

voluntarios = []

while True:
    nome = input("Digite o nome do voluntário (ou 'sair' para encerrar): ")
    
    if nome == 'sair':
        break
    
    voluntarios.append(nome)

print('Voluntários registrados:', voluntarios)

# ex: 04

estoque1 = tuple(input("Produtos do estoque 1 (separados por vírgula): ").split(", "))
estoque2 = tuple(input("Produtos do estoque 2 (separados por vírgula): ").split(", "))
estoque_combinado = estoque1 + estoque2  
print(f'Estoque combinado:\n{estoque_combinado}')

# ex: 05

convidados = ['Ana', 'Pedro', 'Carlos']
print(f"Lista atual de convidados: {convidados}")
novo_convidado = input("Digite o nome do novo convidado: ")
posicao = int(input("Digite a posição na qual deseja inserir o convidado: "))
convidados.insert(posicao - 1, novo_convidado)  
print(f"Lista atualizada de convidados: {convidados}")

# ex: 06

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
eventos_registrados.reverse()
print(f'Ordem corrigida: {eventos_registrados}')

# ex: 07

lista_classificacao = ['Ana', 'Maria', 'Paulo']
print('Lista original:', lista_classificacao)

erro = input('Digite o nome incorreto: ')
if erro in lista_classificacao:
    correto = input('Digite o nome correto: ')
    posicao = lista_classificacao.index(erro)
    lista_classificacao.insert(posicao, correto)
    print(f"O nome {erro} foi substituído por {correto}.")
    print('Lista atualizada: ', lista_classificacao)
else:
    print('Nome não encontrado.')

# ex: 08

pedidos = input("Pedidos feitos (separados por vírgula): ").split(", ")
pedidos.pop()
print("Pedidos finais:")
print(pedidos)

# ex:09

notas_alunos = input('Digite as notas dos alunos separadas por vírgula:').split(', ')
notas [float(notas_alunos) for nota in notas_alunos]
media = sum(notas_alunos) / len(notas_alunos)
print(f'Média final da turma: {media:.2f}')

