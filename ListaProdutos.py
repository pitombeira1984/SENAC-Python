estoque = [
    {'Cod': '001','Nome': 'Arroz','Quantidade': 2,'Preço': '5.50'},
    {'Cod': '002','Nome': 'Feijão','Quantidade': 5,'Preço': '7.20'},
    {'Cod': '003','Nome': 'Macarrão','Quantidade': 10,'Preço': '4.30'},
    {'Cod': '004','Nome': 'Óleo','Quantidade': 3,'Preço': '8.90'},
    {'Cod': '005','Nome': 'Açúcar','Quantidade': 6,'Preço': '3.80'},
    {'Cod': '006','Nome': 'Café','Quantidade': 4,'Preço': '12.50'},
]

def ListarProdutos():

    print(f'Lista de Produtos')
    print(f'{'Cod':^10} - {'Nome':^10} - {'Quantidade':^10} - {'Preço':^10}')
    print('-'*50)

    for produto in estoque:

        print(f'{produto['Cod']:^10} - {produto['Nome']:^10} - {produto['Quantidade']:^10} - {produto['Preço']:^10} ')

ListarProdutos()
