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


