
def soma():

    try:
        n1 = int(input('Digite a Primeira Variável: '))
        n2 = int(input('Digite a Segunda variável: '))
        soma = n1 + n2
    except ValueError:

        print('Valor inválido, digite números inteiros.')
        soma = 'Valor Inválido'

    print(f'Soma igual:{soma}') 

soma()