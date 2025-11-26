import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('C:/Users/Aluno/Documents/Tiago Pitombeira/SENAC-Python/Trabalho_DAP/Relatorio DAP.xlsx')
#D:/ESTUDOS/SENAC/Python/Trabalho_DAP/Relatorio DAP.xlsx

#print(df.head())

#Calculo por Serviço:

media_serv = df.groupby('serviço')['qtd'].mean()
#print(media_serv)

mediana_serv = df.groupby('serviço')['qtd'].median()
#print(mediana_serv)

DP_serv = df.groupby('serviço')['qtd'].std().round(2)
#print(DP_serv)


resultado_serv = pd.DataFrame({
    'Média':media_serv,
    'Mediana':mediana_serv,
    'Desvio Padrão':DP_serv
})

#print(resultado_serv)

#Calculo por Mês

media_mes = df.groupby('mês')['qtd'].mean()
#print(media_mes)

mediana_mes = df.groupby('mês')['qtd'].median()
#print(mediana_mes)

DP_mes = df.groupby('mês')['qtd'].std().round(2)
#print(DP_mes)

resultado_mes = pd.DataFrame({
    'Média':media_mes,
    'Mediana':mediana_mes,
    'Desvio Padrão':DP_mes
})

#print(resultado_mes)

#Gráfico Média Atendiemtno por Mês
def graf_media_atend_mes():
    plt.bar(media_mes.index, media_mes.values)
    plt.xlabel('Mês')
    plt.ylabel('Média Atendimento')
    plt.title('Média de Atendimento por Mês')
    plt.show()
#graf_media_atend_mes()

#Gráfico Média Atendimento por Serviço
def graf_media_atend_serv():
    plt.figure(figsize=(8,5))
    plt.bar(media_serv.index, media_serv.values)
    plt.xlabel('Serviço')
    plt.xticks(rotation=15)
    plt.ylabel('Média Atendimento')
    plt.title('Média de Atendimento por Serviço - Janeiro a Maio')
    plt.show()
#graf_media_atend_serv()


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
            print(resultado_serv)
        elif opcao == '2':
            print(resultado_mes)
        elif opcao == '3':
            graf_media_atend_mes()
        elif opcao == '4':
            graf_media_atend_serv()
        elif opcao == '5':
            print('Saindo do Programa')
            break
        else:
            print('Opção Inválida')

menu_relatorio()
    