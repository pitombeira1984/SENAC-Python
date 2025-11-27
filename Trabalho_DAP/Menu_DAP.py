from Codigo_DAP import result_serv, result_mes, graf_media_atend_mes, graf_media_atend_serv;

def menu_relatorio():
       
    while True:
        print('Escolha a Opção para Cliação do Relatório')
        print('Digite 1 para Relatório Atendimento por Serviço')
        print('Digite 2 para Relatório Atendimento por Mês')
        print('Digite 3 Gráfico Média de Atendimento por Mês')
        print('Digite 4 Gráfico Média de Atendimento por Serviço')
        print('Digite 5 para Sair')
        
        opcao = input('Digite a opção desejada:')

        if opcao == '1':
            result_serv()
        elif opcao == '2':
            result_mes()
        elif opcao == '3':
            graf_media_atend_mes()
        elif opcao == '4':
            graf_media_atend_serv()
        elif opcao == '5':
            print('Saindo do Programa')
            break
        else:
            print('Opção Inválida')

if __name__ == "__main__":                       
    menu_relatorio()