import os

cadastros = []

while True:
    cadastros.sort()
    novo_cadastro = input('Inserir novo cadastro de pessoa na lista: ')

    if novo_cadastro != '':
        cadastros.append(novo_cadastro)
        continue
    else:
        break
    
os.system("cls")

print(f'{'-'*35}LISTA DE PESSOAS{'-'*35}')

cadastro = input('Digite o nome a ser pesquisado: ').capitalize()

try:
    indice = cadastros.index(cadastro)
    print(f'Nome encontrado: {cadastro} no índice {indice}.')
except:
    print(f'{cadastro} não encontrado na lista.')


for cadastro in cadastros:
    print(cadastro)
# -------------------------------------------------- ACABA AQUI!!!!!!!!

# lista de frutas
frutas =  ['Maracujá', 'Banana', 'Maçã']

# usiario informa o nome da nova fruta
nova_fruta = input('Informe o nome da nova fruta: ')

# nova fruta é inserida na lista
frutas.append(nova_fruta)

# exibe na tela nova lista
for fruta in frutas:
    print(fruta)


------------------------


cidades = ['Brasília', 'Taguatinga', 'Gama', 'Sobradinho']

cidade_deletada = input('Nome da cidade a ser deletada: ')

try:
    cidades.remove(cidade_deletada)
except:
    print("Não foi possível remover a cidade. ")

for cidade in cidades:
    print(cidade)

-----------------------------

nomes = ['Adão', "Helião", "Chups", 'Carminha', 'Maria Baixinha', 'João Boca Azeda', 'Beltiza', 'Erondina', 'Juninho Lobrega', 'Orizonmarden', 'Zequinha', 'Ninoca', 'Joabe', 'Noemia', 'Rosa', 'Juscelino']

# usuário informa o nome que deseja pesquisar
nome = input('Digite o nome a ser pesquisado: ').capitalize()

# retorna o índice do nome pesquisado

# verifica se o nome está na lista ou não
try:
    indice = nomes.index(nome)
    print(f'Nome encontrado: {nome} no índice {indice}.')
except:
    print(f'{nome} não encontrado na lista.')

------------------------------------------

# importa biblioteca
import os

tarefas = []

while True:
    tarefas.sort()
    nova_tarefa = input('Informe suas tarefas do dia ou deixe vazio para encerrar e exibir a lista: ')

    if nova_tarefa != '':
        tarefas.append(nova_tarefa)
        continue
    else:
        break
    
os.system("cls")

print(f'{'-'*35}LISTA DE TAREFAS DO DIA{'-'*35}')

for tarefa in tarefas:
    print(tarefa)
