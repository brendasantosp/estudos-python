#1
def calcular_idade(ano_nasc, ano_atual):
    return ano_atual - ano_nasc

ano_nasc = int(input('Digite o ano de nascimento: '))
ano_atual = int(input('Digite o ano atual: '))
idade = calcular_idade(ano_nasc, ano_atual)
print(f'A idade é {idade} anos')

#2
def contar_caracteres(palavra):
    return len(palavra)

texto = input('Digite uma palavra: ')
print(f'Essa palavra tem {contar_caracteres(texto)} caracteres')

#3
def saudacao(hora):
    if hora < 12:
        return 'Bom dia'
    elif hora < 18:
        return 'Boa tarde'
    else:
        return 'Boa noite'

hora_atual = int(input('Digite a hora atual (0-23): '))
print(saudacao(hora_atual))

#4

def converter_telefones(lista):  

   return [int(telefone) for telefone in lista] 

def verifica_tipos(lista):  

   for num in lista:  

       if not isinstance(num, int):  

           return "Erro na conversão."  

   return "Todos os números foram convertidos corretamente!" 

telefones = ["11987654321", "21912345678", "31987654321", "11911223344"] 

telefones_convertidos = converter_telefones(telefones) 

print(verifica_tipos(telefones_convertidos))

#5

valores = input("Digite os valores das vendas: ").split() 
total = sum(map(float, valores)) # sum() para somá-los e map() para converter os valores digitados em números
print(f"O total de vendas foi: {total}")

#6

numeros = input("Digite os números separados por espaço: ").split() 
pares = filter(lambda x: int(x) % 2 == 0, numeros) #filter() com uma função lambda para selecionar apenas os números pares. Os valores são exibidos com join()
print("Números pares:", " ".join(pares))

#7

produtos = input("Digite os produtos separados por vírgula: ").split(",") 
precos = input("Digite os preços separados por vírgula: ").split(",") 
 
for produto, preco in zip(produtos, precos): 
    print(f"{produto.strip()}: {preco.strip()}")

