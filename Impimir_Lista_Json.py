
def imprimir_lista():

    lista = [
        {'nome':'Arroz', 'preco': 6.99, 'quantidade': 1},
        {'nome':'Feijao', 'preco': 8.99, 'quantidade': 5},
        {'nome':'Macarrao', 'preco': 4.99, 'quantidade': 10}
    ]

    print(f'{"nome":^10} | {"preco":^10} | {"quantidade":^10}')
    print(f'{lista[0]["nome"]:^10} | {lista[0]["preco"]:^10} | {lista[0]["quantidade"]:^10}')
    print(f'{lista[1]["nome"]:^10} | {lista[1]["preco"]:^10} | {lista[1]["quantidade"]:^10}')
    print(f'{lista[2]["nome"]:^10} | {lista[2]["preco"]:^10} | {lista[2]["quantidade"]:^10}')

imprimir_lista()