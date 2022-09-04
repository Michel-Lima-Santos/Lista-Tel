# Dicionário contendo todos os contatos.
Contatos = {}

# Dicionários correspondentes às classificações de acordo com a idade.
Contatos_maior = {}
Contatos_menor = {}

# Estrutura de repetição while que irá se encerrar quando o nome digitado for uma string vazia.
while True:
    nome = input('Digite o nome:')
    if nome == '':
        break

    # Listas e variáveis que serão inseridas nos dicionários.
    lista = []
    lista_menor = []
    lista_maior = []
    idade = int(input('Digite a idade:'))
    lista.append(idade)
    tel = int(input('Digite o telefone para contato:'))
    lista.append(tel)

    # Condição que irá determinar a qual lista corresponderá o contato de acordo com a idade.
    if idade >= 18:
        lista_maior.append(idade)
        lista_maior.append(tel)
    else:
        lista_menor.append(idade)
        lista_menor.append(tel)
    Contatos[nome] = lista
    Contatos_maior[nome] = lista_maior
    Contatos_menor[nome] = lista_menor

# Com os novos dicionários criados, eles estavam contendo listas vazias por conta da condicional da idade,
# gerando um erro de índice, as estruturas while abaixo servem para evitar que este erro aconteça, evitando que,
# na hora do print seja impressa uma chave com lista vazia, gerando assim o Index Error, os códigos abaixo eliminarão
# todas as chaves que tiverem como values listas vazias.
    while Contatos_maior[nome] == []:
        Contatos_maior.pop(nome)
        break
    while Contatos_menor[nome] == []:
        Contatos_menor.pop(nome)
        break

    # Impressão de todos os contatos.
for nome, lista in Contatos.items():
    print('Nome: {} | Idade: {} | Telefone: {}'.format(nome, lista[0], lista[1]))

# Impressão de todos os contatos organizados por ordem alfabética.
print('\nLista organizada em ordem alfabética\n')

for nome, lista in sorted(Contatos.items(), key=Contatos.get(1)):
    print('Nome: {} | Idade: {} | Telefone: {}'.format(nome, lista[0], lista[1]))

# Impressão dos contatos que possuem 18 anos de idade ou mais.
print('\nMaiores de idade\n')

for nome, lista_maior in sorted(Contatos_maior.items(), key=Contatos_maior.get(1)):
    print('Nome: {} | Idade: {} | Telefone: {}'.format(nome, lista_maior[0], lista_maior[1]))

# Impressão dos contatos que possuem menos de 18 anos de idade.
print('\nMenores de idade\n')

for nome, lista_menor in sorted(Contatos_menor.items(), key=Contatos_menor.get(1)):
    print('Nome: {} | Idade: {} | Telefone: {}'.format(nome, lista_menor[0], lista_menor[1]))
