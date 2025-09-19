def imprimir_produtos():
    
    try:
        nome = str(input('Nome do Produto: '))
        qt = int(input('Quantidade Estoque: '))
        pc = float(input('Preço Unitário(ex:5.99): '))

        produto_criado = {'nome':nome,
                          'quantidade':qt, 
                          'preco':pc
                          }
        
        print(f'Nome: {produto_criado['nome']}')
        print(f'Quantidade: {produto_criado['quantidade']}')
        print(f'Preço: {produto_criado['preco']}')

    except ValueError:
        print('Digite um Valor valido!!!')
        produto_criado = "Lista Inválida"

imprimir_produtos()



    


