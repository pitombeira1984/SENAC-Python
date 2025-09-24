def MenuSimples():
    while True:
        print('Menu Teste')
        print('Digite 1 para Função A')
        print('Digite 2 para Função B')
        print('Digite 3 para Sair')

        opcao = input('Digite a opção: ')

        if opcao == '1':
            print('Ativado a Função A')
        elif opcao == '2':
            print('Ativado a Função B')
        elif opcao == '3':
            print('Saindo do Programa')
            break
        else:
            print('Opção invalida')

MenuSimples()