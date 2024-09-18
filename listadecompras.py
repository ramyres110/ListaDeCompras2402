#!/bin/python3

lista = []

# 1. Adicionar item
# * Descrição
# * Preço (0.00 para não compro)
def add_item():
    print("Informe as informações do item")
    descricao = input("Descrição:")
    preco = input("Preço:")
    item = {
        "descricao":descricao,
        "preco":preco
    }
    lista.append(item)

# 2. Listar items da lista
def lista_items():
    #TODO: Listar itens em formato de tabela. Ex:
    # | Indice | Descrição | Preço |
    # +-------+-----------+-------+
    for item in lista:
        print(item)


# 3. Remover item pelo indice
def remover_item():
    # TODO: mostrar items, pegar indice e remover o item
    pass

# 4. Informar preço de um item compro
def informar_preco():
    lista_items()
    indice = input("Informe o indice:")
    preco = input("Informe o preco:")
    lista[int(indice)]["preco"] = preco

# 5. Mostrar total da lista.
def total_da_lista():
    # TODO: Retornar total da lista: R$ 9009.00
    pass

# Mostrar opções de funcionalidade para o usuário
def mostrar_menu():
    # TODO: Mostrar demais opções de funcionalidades
    print("0 - Sair")

while True:
    mostrar_menu()
    opcao = input("Opção:")
    if opcao == "0":
        break
    
    #TODO: Chamar opções


