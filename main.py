import os

cadastros = []

while True:
    novo_cadastro = input('Inserir novo cadastro de pessoa na lista: ')

    if novo_cadastro != '':
        cadastros.append(novo_cadastro)
        continue
    else:
        break

os.system("cls")

for cadastro in cadastros:
    print(cadastro)

print(f'{'-'*35}LISTA DE PESSOAS{'-'*35}')

cadastro = input('Digite o nome a ser pesquisado: ').capitalize()
cadastros.sort()

try:
    indice = cadastros.index(cadastro)
    print(f'Nome encontrado: {cadastro} no índice {indice}.')
except:
    print(f'{cadastro} não encontrado na lista.')

for cadastro in cadastros:
    print(cadastro)

while True:
    cadastros.sort()
    novo_nome = input('Insira novos nomes se desejar: ')
    
    if novo_nome != '':
        cadastros.append(novo_nome)
        continue
    else:
        break

for novo_nome in cadastros:
    print(novo_nome)

indice = int(input('Informe o índice que deseja alterar: '))
indice -= 1

# usuário informa o novo nome
cadastros[indice] = input('Informe o novo nome: ')

# exibe a lista
for cadastro in cadastros:
    print(cadastro)